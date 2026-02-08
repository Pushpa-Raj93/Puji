# 🚀 PujithaMP Deployment Guide

## Deployment Options

### Option 1: **Render** (Recommended - Free & Easy)

### Option 2: **Heroku** (Paid)

### Option 3: **Azure** (Free tier available)

### Option 4: **AWS Lightsail** (Affordable)

### Option 5: **PythonAnywhere** (Simple)

---

## 📋 Pre-Deployment Checklist

Before deploying, do these steps:

### Step 1: Create `requirements.txt`

```bash
cd "c:\Users\PUSHPARAJ\OneDrive\Desktop\PujithaMP"
pip freeze > requirements.txt
```

**Or manually create with:**

```
Flask==3.0.0
Flask-CORS==6.0.2
PyJWT==2.8.0
gunicorn==21.2.0
```

### Step 2: Create `.env` file (for production)

```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here-change-this
DEBUG=False
```

### Step 3: Update `app.py` for production

Change the last line from:

```python
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

To:

```python
if __name__ == '__main__':
    import os
    debug = os.getenv('DEBUG', 'False') == 'True'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug, port=port)
```

### Step 4: Create `Procfile` (for production servers)

```
web: gunicorn app:app
```

### Step 5: Create `runtime.txt` (specify Python version)

```
python-3.11.7
```

---

## 🎯 **RECOMMENDED: Deploy to Render (Free & Easy)**

### Steps

1. **Push code to GitHub**

   ```bash
   git init
   git add .
   git commit -m "Initial commit: PujithaMP Blockchain Charity"
   git remote add origin https://github.com/YOUR_USERNAME/PujithaMP.git
   git push -u origin main
   ```

2. **Create Render Account**
   - Go to <https://render.com>
   - Sign up (free account)

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the PujithaMP repo

4. **Configure Settings**
   - **Name:** PujithaMP
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free

5. **Add Environment Variables**
   - Click "Environment"
   - Add:

     ```
     FLASK_ENV=production
     SECRET_KEY=your-random-secret-key
     DEBUG=False
     ```

6. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Your app will be live at: `https://pujithamp-xxxxx.onrender.com`

---

## 🔷 **Alternative: Deploy to Heroku (Paid)**

### Steps

1. **Create Heroku Account**
   - Go to <https://www.heroku.com>
   - Sign up and verify email

2. **Install Heroku CLI**

   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   heroku login
   ```

3. **Initialize Heroku App**

   ```bash
   heroku create pujithamp
   heroku config:set FLASK_ENV=production
   heroku config:set SECRET_KEY=your-secret-key
   ```

4. **Deploy**

   ```bash
   git push heroku main
   ```

5. **Access Your App**

   ```bash
   heroku open
   ```

---

## ☁️ **Alternative: Deploy to Azure (Free Tier)**

### Steps

1. **Create Azure Account**
   - Go to <https://azure.microsoft.com>
   - Sign up (free tier with $200 credit)

2. **Create App Service**
   - In Azure Portal → Create Resource → App Service
   - Select Python 3.11
   - Choose "Free" tier

3. **Configure Deployment**
   - Set up GitHub Actions or ZIP deployment
   - Upload your code

4. **Set Environment Variables**
   - Application Settings → Add:
     - `FLASK_ENV = production`
     - `SECRET_KEY = your-secret-key`

5. **Start Your App**
   - Browse to your Azure App URL

---

## 📦 **Local Production Test**

Before deploying, test locally:

```bash
# Install production server
pip install gunicorn

# Run production server
gunicorn app:app --bind 0.0.0.0:5000

# Test at http://localhost:5000
```

---

## 🔒 **Production Security Checklist**

- [ ] Change `SECRET_KEY` to a random string
- [ ] Set `DEBUG=False` in production
- [ ] Use environment variables for secrets
- [ ] Add HTTPS/SSL certificate
- [ ] Enable CORS properly (not '*')
- [ ] Set strong database passwords
- [ ] Add rate limiting
- [ ] Monitor errors with Sentry

---

## 🗄️ **Database for Production**

Current setup uses in-memory storage (resets on restart).

### For Persistent Data

**Option A: PostgreSQL on Render**

```bash
pip install psycopg2-binary
```

Update `app.py`:

```python
import os
db_url = os.getenv('DATABASE_URL')
if db_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
```

**Option B: MongoDB Atlas**

```bash
pip install pymongo
```

**Option C: Keep SQLite (Simple)**
Update blockchain storage to use file-based SQLite

---

## 📊 **Post-Deployment**

1. **Monitor Logs**

   ```bash
   # Render
   # View in Render dashboard
   
   # Heroku
   heroku logs --tail
   ```

2. **Add Domain (Optional)**
   - Render/Heroku provide free domain
   - Add custom domain in settings

3. **Set Up Backups**
   - Database backups
   - Code backups (GitHub)

4. **Enable Analytics**
   - Monitor traffic
   - Track errors

---

## ⚡ **Quick Deploy Commands**

### Render (After GitHub Push)

```
1. Go to: https://render.com
2. Click "New +" → "Web Service"
3. Select your GitHub repo
4. Click "Create"
5. Wait for deployment
```

### Heroku (If installed)

```bash
heroku create pujithamp
git push heroku main
heroku open
```

---

## 🆘 **Troubleshooting**

| Issue | Solution |
|-------|----------|
| Build fails | Check `requirements.txt` has all dependencies |
| App crashes | Check logs, verify `Procfile` syntax |
| Port error | Ensure using `PORT` environment variable |
| CORS errors | Update CORS_ORIGINS in production |
| Database error | Check database connection string |

---

## 📝 **Files You Need for Deployment**

Ensure these files exist:

```
PujithaMP/
├── app.py                    ✓ Main application
├── blockchain.py             ✓ Blockchain logic
├── templates/
│   └── index.html           ✓ Frontend
├── requirements.txt         ✓ Dependencies
├── Procfile                 ✓ Server config
├── runtime.txt              ✓ Python version
├── .env                     ✓ Environment vars
└── .gitignore              ✓ Git ignore
```

---

## 🎉 **Your App Will Be Live!**

After deployment:

- ✅ Live URL provided
- ✅ Custom domain option
- ✅ Free SSL certificate
- ✅ Auto-scaling
- ✅ GitHub CI/CD integration

**Estimated Deployment Time:** 5-15 minutes

---

## 💡 **Next Steps**

1. **Create `requirements.txt`**

   ```bash
   pip freeze > requirements.txt
   ```

2. **Create `Procfile`**
   - Add text: `web: gunicorn app:app`

3. **Push to GitHub**
   - Create repo and push code

4. **Deploy to Render**
   - Connect GitHub account
   - Select repository
   - Deploy!

---

**Ready to deploy? Start with Render (easiest)!** 🚀
