import json
from app import app, users, contract_state, blockchain

def print_header(title):
    print("\n" + "="*50)
    print(f" {title}")
    print("="*50)

def run_demo():
    client = app.test_client()
    
    print_header("1. USER REGISTRATION")
    # Register Admin
    resp = client.post('/register', json={'username': 'admin', 'password': 'admin123', 'role': 'Admin', 'email': 'admin@example.com', 'mobile': '9999999999'})
    print(f"Admin Registration: {resp.get_json()['message']}")
    
    # Register Charity
    resp = client.post('/register', json={'username': 'SaveTheKids', 'password': 'pwd123', 'role': 'Charity', 'email': 'charity@example.com', 'mobile': '9876543210'})
    print(f"Charity Registration: {resp.get_json()['message']}")
    
    # Register Donor
    resp = client.post('/register', json={'username': 'Alice', 'password': 'pwd123', 'role': 'Donor', 'email': 'alice@example.com', 'mobile': '1234567890'})
    print(f"Donor Registration: {resp.get_json()['message']}")
    
    print_header("2. AUTHENTICATION & JWT")
    # Login Donor
    auth_resp = client.post('/login', json={'username': 'Alice', 'password': 'pwd123'})
    donor_token = auth_resp.get_json().get('token')
    print(f"Alice Logged In. JWT: {donor_token[:20]}... (truncated)")

    # Login Charity
    auth_resp = client.post('/login', json={'username': 'SaveTheKids', 'password': 'pwd123'})
    charity_token = auth_resp.get_json().get('token')
    print(f"Charity Logged In. JWT: {charity_token[:20]}... (truncated)")
    
    # Login Admin
    auth_resp = client.post('/login', json={'username': 'admin', 'password': 'admin123'})
    admin_token = auth_resp.get_json().get('token')
    
    print_header("3. CHARITY REQUESTS FUNDS")
    # Charity requests $500
    headers = {'Authorization': f'Bearer {charity_token}'}
    resp = client.post('/request_funds', json={'amount': 500}, headers=headers)
    print(f"Request Status: {resp.get_json()['message']}")
    print(f"Smart Contract Logs: {resp.get_json()['smart_contract_logs']}")
    
    print_header("4. DONOR DONATES FUNDS")
    # Alice donates $600
    headers = {'Authorization': f'Bearer {donor_token}'}
    resp = client.post('/donate', json={'charity': 'SaveTheKids', 'amount': 600}, headers=headers)
    print(f"Donation Status: {resp.get_json()['message']}")
    print(f"Transaction: {resp.get_json().get('transaction')}")
    print(f"Smart Contract Logs: {resp.get_json()['smart_contract_logs']}") 
    # Logic: 600 donated > 500 requested -> Should release
    
    print_header("5. ADMIN AUDIT (LEDGER VIEW)")
    headers = {'Authorization': f'Bearer {admin_token}'}
    resp = client.get('/ledger', headers=headers)
    chain = resp.get_json()['chain']
    print(f"Blockchain length: {len(chain)}")
    for block in chain:
        print(f"Block {block['index']} | Hash: {block['hash'][:10]}... | Tx Count: {len(block['transactions'])}")
        
    print_header("6. VERIFY INTEGRITY (BEFORE ATTACK)")
    resp = client.get('/verify_chain')
    print(f"Verification Result: {resp.get_json()['message']}")
    
    print_header("7. SIMULATE HACKING ATTACK (TAMPERING)")
    resp = client.post('/tamper_demo')
    print(f"Attack Status: {resp.get_json()['message']}")
    print(f"Tampered Block Index: {resp.get_json()['block_index']}")
    print(f"Tampered Data: {resp.get_json()['new_data_sample']}")
    
    print_header("8. VERIFY INTEGRITY (AFTER ATTACK)")
    resp = client.get('/verify_chain')
    print(f"Verification Result: {resp.get_json()['message']}")
    if 'errors' in resp.get_json():
        print("Detailed Errors:")
        for err in resp.get_json()['errors']:
            print(f" - {err}")
            
    print_header("9. BANK DETAILS & OTP FLOW")
    # 1. Fetch IFSC
    print("Fetching IFSC details for 'SBIN0004343'...")
    resp = client.post('/get_ifsc', json={'ifsc': 'SBIN0004343'})
    print(f"IFSC Lookup: {resp.get_json()}")
    
    # 2. Generate OTP
    print("Requesting OTP for Alice...")
    resp = client.post('/generate_otp', json={'username': 'Alice'})
    print(f"Response: {resp.get_json()['message']}")
    
    # 3. Cheat: Get OTP from backend storage
    # Since we imported 'users' from app, we can inspect it directly in this simulation
    alice_otp = users['Alice']['otp']
    print(f"Verified (simulated) Email: Received OTP {alice_otp}")
    
    # 4. Save Bank Details (requires OTP verification logic usually, 
    # but here we separate verify and save or do them together based on flow)
    # Our frontend flow verifies first, then saves. Let's do that.
    
    # Verify
    verify_resp = client.post('/verify_otp', json={'username': 'Alice', 'otp': alice_otp})
    print(f"OTP Verification: {verify_resp.get_json()['message']}")
    
    if verify_resp.get_json()['success']:
        # Save
        headers = {'Authorization': f'Bearer {donor_token}'}
        bank_data = {
            'account_number': '1234567890',
            'ifsc': 'SBIN0004343',
            'bank_name': 'STATE BANK OF INDIA',
            'branch': 'DUMMY BRANCH'
        }
        save_resp = client.post('/save_bank_details', json=bank_data, headers=headers)
        print(f"Save Bank Details: {save_resp.get_json()['message']}")
        
        # Check Profile
        prof_resp = client.get('/get_user_profile', headers=headers)
        print(f"Updated Profile Bank Data: {prof_resp.get_json()['bank_details']}")

    print("\nDEMO COMPLETED.")

if __name__ == "__main__":
    run_demo()
