# Automated and Accountable Charity Donation Framework Using Blockchain

A secure academic prototype demonstrating a blockchain-based charity donation system with JWT authentication and Smart Contracts.

## Tech Stack
- **Languages**: Python 3
- **Framework**: Flask
- **Security**: JWT (JSON Web Tokens), SHA-256 Hashing
- **Storage**: In-memory (Academic Simulation)

## Project Structure
- `blockchain.py`: Core Blockchain implementation (Block, SecureBlockchain classes).
- `app.py`: Flask API with User Auth, Smart Contract simulation, and Endpoints.
- `demo_execution.py`: Simulation script to demonstrate the full workflow including "Hacking" attempt.

## Features
1. **User Roles**: Admin, Charity, Donor.
2. **JWT Authentication**: Secure login and protected endpoints.
3. **Smart Contract Logic**: Auto-releases funds when donations cover the request.
4. **Tamper Detection**: Verifies chain integrity and detects data modification.
5. **Bank Integration**: IFSC lookup and account linking.
6. **OTP Verification**: Secure 2-step verification for sensitive changes.

## How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Full Demo (Simulation)**:
   ```bash
   python demo_execution.py
   ```
   This will simulate:
   - Registration & Login
   - Donation & Fund Request flows
   - Smart Contract Execution
   - **Blockchain Tampering & Detection**

3. **Run the Server Manually**:
   ```bash
   python app.py
   ```
   Then open your browser at `http://localhost:5000`.

## API Endpoints

### Public Endpoints
- `GET /charities`: Get list of registered charities
- `GET /stats`: Get platform statistics (total donations, charity count, etc.)
- `GET /verify_chain`: Check blockchain integrity

### Authentication
- `POST /register`: Register new user
- `POST /login`: Get JWT token
- `POST /generate_otp`: Generate OTP for user
- `POST /verify_otp`: Verify OTP

### Protected Endpoints (Require JWT)
- `POST /donate`: Donate to a charity (Donor only)
- `POST /request_funds`: Request funds (Charity only)
- `GET /ledger`: View Blockchain (Authenticated users)
- `POST /get_ifsc`: Fetch bank details from IFSC
- `POST /save_bank_details`: Link bank account
- `GET /get_user_profile`: Fetch user profile and bank info

### Admin Endpoints
- `GET /admin/donors`: Get all donors info
- `GET /admin/charities`: Get all charities info
- `GET /admin/transactions`: Get all transactions
- `GET /admin/pending_requests`: Get pending fund requests

### Demo/Testing
- `POST /tamper_demo`: Simulate a blockchain attack
