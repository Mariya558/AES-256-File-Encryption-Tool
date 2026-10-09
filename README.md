# 🔐 AES File Encryption & Decryption Tool

A lightweight, robust command-line cryptographic engine written in Python. It leverages the industry-standard `cryptography` library to safely handle secure file locking and decoding using symmetric key architectures.

---

## ⚡ Core Functionality

- 🔑 **Secure Key Generation:** Automatically computes high-entropy key pairings saved locally as `secret.key`.
- 🔒 **Tamper-Proof Encryption:** Locks target files into unreadable blocks using protected symmetric ciphers.
- 🔓 **Clean Decryption Recovery:** Restores encrypted data sets back to their initial state using matching local keys.
- 🚫 **Safe Directory Scoping:** Pre-configured Git rules prevent accidental leaks of secret keys or confidential target documents.

---

## 💻 How To Run

### 📦 Dependencies Setup
```bash
git clone https://github.com
cd AES-256-File-Encryption-Tool
pip install -r requirements.txt
```

### 🚀 Commands
1. **Generate a Secret Key:**
   ```bash
   python encryptor.py -g
   ```
2. **Encrypt a Target File:**
   ```bash
   python encryptor.py -e test.txt
   ```
3. **Decrypt the Cipher File:**
   ```bash
   python encryptor.py -d test.txt.encrypted
   ```
