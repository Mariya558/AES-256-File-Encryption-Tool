import os
import sys
import argparse
from cryptography.fernet import Fernet

def generate_key():
    """Generates a secure encryption key and saves it to a file."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] New secure key generated and saved as 'secret.key'. Keep this safe!")

def load_key(key_path):
    """Loads an existing encryption key from disk."""
    if not os.path.exists(key_path):
        print(f"[!] Error: Key file '{key_path}' not found!")
        sys.exit(1)
    with open(key_path, "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    """Encrypts a target file using the loaded key."""
    if not os.path.exists(file_path):
        print(f"[!] Error: Target file '{file_path}' not found!")
        return
        
    f = Fernet(key)
    with open(file_path, "rb") as file_to_encrypt:
        file_data = file_to_encrypt.read()
        
    encrypted_data = f.encrypt(file_data)
    
    output_file = file_path + ".encrypted"
    with open(output_file, "wb") as file_to_save:
        file_to_save.write(encrypted_data)
    print(f"[+] File successfully encrypted! Saved as: {output_file}")

def decrypt_file(file_path, key):
    """Decrypts a target file using the loaded key."""
    if not os.path.exists(file_path):
        print(f"[!] Error: Encrypted file '{file_path}' not found!")
        return
        
    f = Fernet(key)
    with open(file_path, "rb") as file_to_decrypt:
        encrypted_data = file_to_decrypt.read()
        
    try:
        decrypted_data = f.decrypt(encrypted_data)
        
        # Save under a distinct name to show it was successfully unlocked
        output_file = "restored_" + file_path.replace(".encrypted", "")
        with open(output_file, "wb") as file_to_save:
            file_to_save.write(decrypted_data)
        print(f"[+] File successfully decrypted! Restored as: {output_file}")
    except Exception as e:
        print(f"[!] Decryption failed: {e}")

def main():
    print("""
=====================================================
    🔐 AES FILE ENCRYPTION & DECRYPTION TOOL 🔐
=====================================================
    """)
    
    parser = argparse.ArgumentParser(description="Secure File Encryption Utility")
    parser.add_argument("-g", "--generate-key", action="store_true", help="Generate a new secret encryption key")
    parser.add_argument("-e", "--encrypt", help="Path to the file you want to encrypt")
    parser.add_argument("-d", "--decrypt", help="Path to the file you want to decrypt")
    parser.add_argument("-k", "--key", default="secret.key", help="Path to the key file (default: secret.key)")
    
    args = parser.parse_args()
    
    if args.generate_key:
        generate_key()
    elif args.encrypt:
        key = load_key(args.key)
        encrypt_file(args.encrypt, key)
    elif args.decrypt:
        key = load_key(args.key)
        decrypt_file(args.decrypt, key)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
