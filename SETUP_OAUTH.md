# Google OAuth2 Setup Guide

## Step-by-Step Instructions to Get Google Credentials

### 1. Go to Google Cloud Console
- Visit: https://console.cloud.google.com/
- Sign in with your Google account

### 2. Create a New Project
- Click on the project dropdown at the top
- Click "NEW PROJECT"
- Enter a project name: `Email Management System`
- Click "CREATE"

### 3. Enable Required APIs
- In the left sidebar, go to "APIs & Services" → "Library"
- Search for and enable these APIs:
  - **Gmail API**
  - **Google Calendar API**
  - **Google People API**
- Click on each and select "ENABLE"

### 4. Create OAuth2 Credentials
- Go to "APIs & Services" → "Credentials"
- Click "+ CREATE CREDENTIALS" → "OAuth client ID"
- If prompted, first create an OAuth Consent Screen:
  - User Type: Select "External"
  - Fill in required fields (App name, User support email, etc.)
  - Add scopes: `gmail.modify`, `calendar`, `contacts`
  - Add test users (your email)
  - Complete and save

### 5. Get Your Credentials
- Back to Credentials page
- Click "+ CREATE CREDENTIALS" → "OAuth client ID"
- Application Type: **Web Application**
- Name: `Email Management System`
- Authorized redirect URIs: Add these:
  ```
  http://localhost:5000/callback
  http://localhost:5000/auth/callback
  ```
- Click "CREATE"

### 6. Copy Your Credentials
You'll see a popup with:
- **Client ID** → Copy to GOOGLE_CLIENT_ID
- **Client Secret** → Copy to GOOGLE_CLIENT_SECRET

### 7. Update Your .env File
```bash
cp .env.example .env
```

Then edit `.env` and replace:
- `GOOGLE_CLIENT_ID=your_actual_client_id`
- `GOOGLE_CLIENT_SECRET=your_actual_client_secret`
- `SECRET_KEY=generate_random_key_below`

### Generate a Random Secret Key
Run this in Python:
```python
import secrets
print(secrets.token_hex(32))
```

That's it! Your OAuth2 setup is complete. 🎉
