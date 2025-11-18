# 🔐 Cryptography Suite

A complete cryptography toolkit built in Python that implements classical and modern cryptographic algorithms.  
This project includes encryption, decryption, hashing, digital signatures, key exchange, and file security — all inside a clean and interactive CLI interface.

---

## 🚀 Features Implemented

### ✅ Classical Ciphers
- Caesar Cipher  
- Vigenere Cipher  
- Playfair Cipher  
- Hill Cipher (2×2)

### ✅ Modern Cryptography
- RSA Encryption & Decryption  
- Diffie–Hellman Key Exchange  
- SHA-256 Hashing  
- Digital Signatures (RSA + SHA-256)

### ✅ File Security
- File Encryption (XOR-based)  
- File Decryption  

---

## 📁 Project Structure

```

crypto_suite/  
│  
├── main.py  
│  
├── ciphers/  
│   ├── caesar.py  
│   ├── vigenere.py  
│   ├── playfair.py  
│   ├── hill.py  
│   ├── rsa_module.py  
│   ├── diffie_hellman.py  
│   ├── hashing.py  
│   ├── digital_signature.py  
│  
├── file_ops/  
│   ├── file_encrypt.py  
│   ├── file_decrypt.py  
│  
├── utils/  
│   ├── text_cleaner.py  
│   ├── matrix_math.py  
│   ├── number_theory.py  
│  
└── data/  
    ├── keys/  
    ├── encrypted_files/  
    ├── decrypted_files/  

```
---

## ▶️ How to Run the Project

1. Open a terminal inside the project folder:
   ```
   cd crypto_suite  
   ```
3. Run the main program:
   ```
   python main.py
   ```
5. Select any option from the menu:  
   1. Caesar Cipher  
   2. Vigenere Cipher  
   3. Playfair Cipher  
   4. Hill Cipher  
   5. RSA Encryption/Decryption  
   6. Diffie–Hellman Key Exchange  
   7. Hashing (SHA-256)  
   8. Digital Signature  
   9. File Encryption  
   10. File Decryption  
   11. Exit  

Each module prompts you with clean, interactive input.

---

## 🧠 Learning Outcomes

By using this project, you will understand:

- How classical substitution and polyalphabetic ciphers work  
- Digraph encryption using Playfair rules  
- Matrix multiplication and modular inverses in Hill Cipher  
- RSA public-key cryptography (key generation, encryption, decryption)  
- Digital signatures using RSA and SHA-256  
- Secure key exchange using the Diffie–Hellman protocol  
- Hashing fundamentals and properties of SHA-256  
- File-level symmetric encryption using XOR  
- Clean project architecture and modular Python development  

---

## 🗂 Requirements

- Python 3.x  
- NumPy (for Hill Cipher)

Install NumPy using:  
```
pip install numpy
```

All other modules used are from Python’s standard library.

---

## ✅ Example Usage Scenarios

- Demonstrating RSA encryption and decryption to beginners  
- Teaching how digital signatures verify authenticity and integrity  
- Showing Diffie–Hellman shared secret generation  
- Encrypting and decrypting files (XOR demo)  
- Teaching modular arithmetic and matrix operations in crypto  
- Using the toolkit as a teaching or learning resource  

---

## 🔧 Notes & Limitations

- RSA uses small primes for demonstration and **is not secure for real-world use**  
- XOR file encryption is for learning only; for real projects use AES-GCM  
- Playfair merges “J” with “I” as per classical rules  
- Hill cipher requires an invertible key matrix modulo 26  
- This project is educational — not a replacement for professional crypto libraries  

---

## 🛠 Future Improvements

- Replace XOR file encryption with AES-GCM (cryptography library)  
- Save and load RSA keypairs into the `data/keys/` folder  
- Add unit tests for each cipher  
- Implement Miller–Rabin primality test for large RSA primes  
- Add a GUI (Tkinter or web-based)  
- Add AES, DES, or ChaCha20 support  

---

## ❤️ Credits

Developed as a hands-on cryptography learning project to explore classical and modern encryption techniques through direct implementation, experimentation, and modular code design.  
Use responsibly and extend it as a portfolio or educational project.
