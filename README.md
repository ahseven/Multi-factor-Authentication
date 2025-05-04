
# **Multi-Factor Authentication (MFA) System Using Google Authenticator**  
**A secure authentication solution using TOTP (Time-Based One-Time Password)**  

## **Overview**  
This project implements **Multi-Factor Authentication (MFA)** to enhance security beyond traditional password-based logins. By requiring a **time-sensitive six-digit code** (generated via **Google Authenticator** or similar apps), the system ensures that even compromised credentials cannot grant unauthorized access.  

### **Key Features**  
✔ **Secure User Registration** – Generates a unique **secret key** and QR code for MFA setup.  
✔ **TOTP-Based Authentication** – Uses **pyotp** to generate and validate time-based one-time passwords.  
✔ **QR Code Integration** – Users scan a QR code with an authenticator app (e.g., Google Authenticator) to sync codes.  
✔ **No SMS/Email Dependency** – Eliminates risks associated with insecure delivery methods.  
✔ **Developer Mode** – Optional debug mode to inspect stored user data (for testing purposes).  

## **How It Works**  
### **1. User Registration**  
- User provides a **username** and **password**.  
- The system generates a **secret key** (Base32) and stores it securely.  
- A **QR code** is displayed for the user to scan with Google Authenticator app.  
- The app begins generating **6-digit codes** that refresh every **30 seconds**.  

### **2. User Login**  
1. User enters **username** and **password**.  
2. If credentials are valid, the system prompts for the **current 6-digit code** from their Google Authenticator app.  
3. The server verifies the code against its own TOTP calculation.  
4. **Access is granted only if all credentials match.**  

## **Security Benefits**  
🔒 **Protection Against Credential Theft** – Even if a password is stolen, attackers cannot log in without the TOTP code.  
🔒 **No Network Dependency** – Unlike SMS/email-based 2FA, this method works offline.  
🔒 **Time-Sensitive Codes** – Generated codes expire quickly, reducing the risk of replay attacks.  

## **Installation & Usage**  
### **Prerequisites**  
- Python 3.x  
- Required libraries:  
  ```sh
  pip install pyotp qrcode pandas
  ```  

### **Running the Application**  
1. Clone the repository.  
2. Run the Python script:  
   ```sh
   python mfa_system.py
   ```  
3. Follow the on-screen instructions to **register** and **log in**.  

## **Limitations**  
⚠ **Does not protect against compromised authenticator apps** (e.g., if a user's Google account is hacked).  
⚠ **Secret key backup is essential** – Losing access to the authenticator app requires a recovery process.  

## **Future Improvements**  
- **Encrypted database storage** for enhanced security.  
- **Backup codes** for account recovery.  
- **Biometric integration** (e.g., fingerprint/FaceID) for additional authentication layers.  

---  
**Contributions welcome!** Feel free to fork, test, and submit pull requests.  

📌 **Note:** This project is for educational/demonstration purposes. Always follow best security practices in production environments.  

---  
Would you like any refinements or additional sections?
