# 🚀 TrustFlow - Quick Start Guide

## ✅ Prerequisites

Make sure Python 3.8+ is installed on your system.

## 📦 Step 1: Install Dependencies

Open a terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

If you have issues, try:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 🔧 Step 2: Start the Flask Server

Run this command:

```bash
python app.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: off
```

**Keep this terminal window open!**

## 🌐 Step 3: Open the Application

Open your web browser and go to:

```
http://127.0.0.1:5000
```

You should see the TrustFlow login page.

## 👤 Step 4: Test Registration & Login

### Create a Test Account

1. Click **"Create Account"**
2. Enter:
   - **Username**: `testuser` (minimum 3 characters)
   - **Password**: `password123` (minimum 6 characters)
   - **Role**: Select `Donor` or `Charity`
3. Click **"Register"**
4. You'll see success message → Click **"Back to Login"**

### Login with Your Account

1. Enter your username and password
2. Click **"Login"**
3. You should see the Dashboard ✅

## 🎯 Try These Features

### If You're a Donor

- Go to **"Actions"** tab
- Enter charity name: `SaveTheKids`
- Enter amount: `100`
- Click **"Donate Funds"**

### If You're a Charity

- Go to **"Actions"** tab
- Enter amount needed: `500`
- Click **"Submit Request"**

### View Blockchain

- Click **"Blockchain Ledger"** to see all transactions
- Click **"Verify Blockchain Integrity"** to check security

## ⚠️ Troubleshooting

### "Connection Error" when trying to login/register?

- Make sure Flask server is **still running** (check the terminal)
- Make sure you're visiting `http://127.0.0.1:5000` (not `localhost` or different port)
- Try refreshing the page (Ctrl+R or Cmd+R)

### "Token is missing" or "Invalid credentials"?

- Clear your browser's local storage:
  - Press F12 (Developer Tools)
  - Go to Application → Local Storage
  - Delete the `token` entry
  - Refresh the page

### Form shows error immediately?

- Check browser console (F12) for error messages
- Make sure all required fields are filled
- Email/IFSC fields are optional (not required for login/register)

## 🛑 To Stop the Server

Press `Ctrl+C` in the terminal where Flask is running.

---

**Need help?** Check the error message shown on screen - it will tell you what went wrong!
