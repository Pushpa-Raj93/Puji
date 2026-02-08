from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from blockchain import SecureBlockchain, Block
import jwt
import datetime
from functools import wraps
import urllib.request
import json
import random
import requests
import os


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'academic_secure_key_123')
app.config['ALGORITHM'] = 'HS256'
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')

# --- Storage ---
blockchain = SecureBlockchain()
users = {} # {username: {password, role, balance, bank_details: {}}}
# Pre-seed admin and dummy users? We'll do it via endpoints or init.


# --- Smart Contract State ---
# Track funds available for charities
# In a real contract this would be derived from the chain, for speed we cache it.
contract_state = {
    "charity_balances": {}, # charity_username: total_received
    "pending_requests": []
}



# --- Helper Functions ---
@app.route('/')
def home():
    return render_template('index.html')

# --- Auth Decorator ---
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            # Remove 'Bearer ' if present
            if token.startswith('Bearer '):
                token = token.split(" ")[1]
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=[app.config['ALGORITHM']])
            current_user = users.get(data['user'])
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 403
        return f(current_user, *args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if current_user['role'] != 'Admin':
            return jsonify({'message': 'Admin access required!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# --- Smart Contract Logic ---
def execute_smart_contract():
    """
    Scans pending requests and funds. Releases if conditions met.
    """
    logs = []
    # Recalculate balances from blockchain to be safe/verified
    # For now, we trust the contract_state cash for simplicity or iterate chain
    
    # Simple iterator over requests
    remaining_requests = []
    for req in contract_state['pending_requests']:
        charity = req['charity']
        amount = req['amount']
        
        balance = contract_state['charity_balances'].get(charity, 0)
        
        if balance >= amount:
            # EXECUTE RELEASE
            tx = {
                'type': 'FUND_RELEASE',
                'charity': charity,
                'amount': amount,
                'timestamp': str(datetime.datetime.now())
            }
            blockchain.add_new_transaction(tx)
            blockchain.mine()
            
            # Deduct locally
            contract_state['charity_balances'][charity] -= amount
            logs.append(f"SMART CONTRACT: Released {amount} to {charity}")
        else:
            remaining_requests.append(req)
            logs.append(f"SMART CONTRACT: Low funds for {charity}. Request {amount}, Bal {balance}")
            
    contract_state['pending_requests'] = remaining_requests
    return logs

# --- Routes ---

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    role = data.get('role', 'Donor')
    
    # Validations
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    
    if len(username) < 3:
        return jsonify({'message': 'Username must be at least 3 characters'}), 400
    
    if len(password) < 6:
        return jsonify({'message': 'Password must be at least 6 characters'}), 400
    
    if username in users:
        return jsonify({'message': 'Username already exists'}), 400
    
    # Create new user
    users[username] = {
        'password': password, 
        'role': role,
        'balance': 1000 if role == 'Donor' else 0,
        'bank_details': {}
    }
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = users.get(username)
    if user and user['password'] == password:
        token = jwt.encode({
            'user': username,
            'role': user['role'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm=app.config['ALGORITHM'])
        return jsonify({'token': token})
    
    return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/donate', methods=['POST'])
@token_required
def donate(current_user):
    if current_user['role'] != 'Donor':
        return jsonify({'message': 'Only donors can donate'}), 403
    
    data = request.get_json()
    charity = data.get('charity')
    amount = float(data.get('amount'))
    
    if current_user['balance'] < amount:
        return jsonify({'message': 'Insufficient funds'}), 400
        
    # Process Donation
    transaction = {
        'sender': current_user.get('password'), # using password as placeholder ID for now or just username
        'sender_name': 'Unknown', # Fixed later

        # wait, decorator passes the user object. Let's fix decorator to pass username too or just object.
        # simpler: just use key from payload
        'recipient': charity,
        'amount': amount,
        'type': 'DONATION',
        'timestamp': str(datetime.datetime.now())
    }
    
    # Store in blockchain
    blockchain.add_new_transaction(transaction)
    blockchain.mine()
    
    # Update local states
    current_user['balance'] -= amount
    contract_state['charity_balances'][charity] = contract_state['charity_balances'].get(charity, 0) + amount
    
    # Trigger smart contract check (auto-execution)
    logs = execute_smart_contract()
    
    return jsonify({
        'message': 'Donation successful', 
        'transaction': transaction,
        'smart_contract_logs': logs
    })

@app.route('/request_funds', methods=['POST'])
@token_required
def request_funds(current_user):
    if current_user['role'] != 'Charity':
        return jsonify({'message': 'Only charities can request funds'}), 403
        
    data = request.get_json()
    amount = float(data.get('amount'))
    
    # Find username
    username = None
    for k, v in users.items():
        if v == current_user:
            username = k
            break
            
    print(f"Request from {username} for {amount}")
    
    req = {'charity': username, 'amount': amount}
    contract_state['pending_requests'].append(req)
    
    # Try execute
    logs = execute_smart_contract()
    
    return jsonify({'message': 'Fund request logged', 'smart_contract_logs': logs})

@app.route('/ledger', methods=['GET'])
@token_required
def ledger(current_user):
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return jsonify({'length': len(chain_data), 'chain': chain_data})

@app.route('/verify_chain', methods=['GET'])
def verify_chain():
    # This endpoint runs the integrity check
    result = blockchain.check_chain_validity()
    
    if result['is_valid']:
        return jsonify({'message': 'Blockchain is VALID', 'status': 'Secure'})
    else:
        return jsonify({'message': 'Blockchain integrity VIOLATED', 'errors': result['details']}), 400

@app.route('/tamper_demo', methods=['POST'])
def tamper_demo():
    """
    Intentionally corrupt a block to demonstrate security.
    """
    if len(blockchain.chain) < 2:
        return jsonify({'message': 'Not enough blocks to tamper'}), 400
        
    # Tamper with the data of the second block (index 1)
    target_block = blockchain.chain[1]
    original_hash = target_block.hash
    
    # Modify transaction data
    if target_block.transactions:
        target_block.transactions[0]['amount'] = 999999999 # Fraud!
        target_block.transactions[0]['type'] = 'FRAUD'
    else:
        target_block.transactions.append({'type': 'FRAUD_INSERTION'})
        
    # Note: We do NOT recompute the hash on the block object itself to simulate checking mismatch
    # The verify function will recompute and compare.
    
    return jsonify({
        'message': 'Tampering executed successfully',
        'block_index': target_block.index,
        'original_stored_hash': original_hash,
        'new_data_sample': target_block.transactions
    })

# --- New Features: IFSC & OTP ---

@app.route('/get_ifsc', methods=['POST'])
def get_ifsc():
    data = request.get_json()
    ifsc = data.get('ifsc')
    
    if not ifsc:
        return jsonify({'message': 'IFSC code required'}), 400
        
    try:
        url = f"https://ifsc.razorpay.com/{ifsc}"
        with urllib.request.urlopen(url) as response:
            if response.getcode() == 200:
                bank_data = json.loads(response.read().decode())
                return jsonify({'found': True, 'data': bank_data})
            else:
                return jsonify({'found': False, 'message': 'Invalid IFSC'}), 404
    except Exception as e:
        return jsonify({'found': False, 'message': 'API Error or Invalid Code', 'error': str(e)}), 400

@app.route('/save_bank_details', methods=['POST'])
@token_required
def save_bank_details(current_user):
    data = request.get_json()
    
    bank_details = {
        'account_number': data.get('account_number'),
        'ifsc': data.get('ifsc'),
        'bank_name': data.get('bank_name'),
        'branch': data.get('branch')
    }
    
    current_user['bank_details'] = bank_details
    return jsonify({'message': 'Bank details saved successfully', 'details': bank_details})

@app.route('/get_user_profile', methods=['GET'])
@token_required
def get_user_profile(current_user):
    # Helper to retrieve saved details
    return jsonify({
        'username': dict(filter(lambda x: x[1] == current_user, users.items())).get('username', 'Unknown'), # Clean this up later
        'role': current_user['role'],
        'balance': current_user['balance'],
        'bank_details': current_user.get('bank_details', {})
    })

# --- Admin Endpoints ---
@app.route('/admin/donors', methods=['GET'])
@token_required
@admin_required
def get_donors(current_user):
    """Get all donor information"""
    donors = []
    for username, user in users.items():
        if user['role'] == 'Donor':
            donors.append({
                'username': username,
                'balance': user['balance'],
                'bank_details': user.get('bank_details', {}),
                'role': 'Donor'
            })
    return jsonify({'donors': donors})

@app.route('/admin/charities', methods=['GET'])
@token_required
@admin_required
def get_charities(current_user):
    """Get all charity information"""
    charities = []
    for username, user in users.items():
        if user['role'] == 'Charity':
            total_received = contract_state['charity_balances'].get(username, 0)
            charities.append({
                'username': username,
                'balance': user['balance'],
                'total_received': total_received,
                'bank_details': user.get('bank_details', {}),
                'role': 'Charity'
            })
    return jsonify({'charities': charities})

@app.route('/admin/transactions', methods=['GET'])
@token_required
@admin_required
def get_transactions(current_user):
    """Get all transactions from blockchain"""
    transactions = []
    for block in blockchain.chain:
        if block.transactions:
            for tx in block.transactions:
                transactions.append({
                    'block': block.index,
                    'transaction': tx,
                    'timestamp': block.timestamp
                })
    return jsonify({'transactions': transactions})

@app.route('/admin/pending_requests', methods=['GET'])
@token_required
@admin_required
def get_pending_requests(current_user):
    """Get all pending fund requests from charities"""
    return jsonify({'pending_requests': contract_state['pending_requests']})


if __name__ == '__main__':
    debug = os.getenv('DEBUG', 'False') == 'True'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug, host='0.0.0.0', port=port)

