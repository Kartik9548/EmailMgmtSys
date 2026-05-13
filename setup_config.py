#!/usr/bin/env python3
"""
Generate configuration values for the Email Management System
"""

import secrets
import sys

def generate_secret_key():
    """Generate a random secret key for Flask"""
    return secrets.token_hex(32)

def main():
    print("\n" + "="*50)
    print("Email Management System - Configuration Helper")
    print("="*50 + "\n")
    
    print("📝 Follow these steps:\n")
    
    print("1️⃣  GET GOOGLE OAUTH CREDENTIALS:")
    print("   - Open: https://console.cloud.google.com/")
    print("   - Follow instructions in SETUP_OAUTH.md")
    print("   - Copy Client ID and Client Secret\n")
    
    print("2️⃣  GENERATE SECRET KEY:")
    secret_key = generate_secret_key()
    print(f"   Random SECRET_KEY: {secret_key}\n")
    
    print("3️⃣  EDIT .env FILE:")
    print("   Edit the .env file and add:")
    print(f"   - GOOGLE_CLIENT_ID=<your_client_id>")
    print(f"   - GOOGLE_CLIENT_SECRET=<your_client_secret>")
    print(f"   - SECRET_KEY={secret_key}\n")
    
    print("4️⃣  RUN THE APP:")
    print("   source venv/bin/activate")
    print("   python3 run.py\n")
    
    print("5️⃣  OPEN IN BROWSER:")
    print("   http://localhost:5000\n")
    
    print("="*50 + "\n")

if __name__ == "__main__":
    main()
