import sys
def main_menu():
    while True:
        print("\n=========================")
        print(" CRYPTOGRAPHY SUITE ")
        print("===========================")
        print("1. Caesar Cipher")
        print("2. Vigenere Cipher")
        print("3. Playfair Cipher")
        print("4. Hill Cipher")
        print("5. RSA Encryption/Decryption")
        print("6. Diffie-Hellman Key Exchange")
        print("7. Hashing (SHA-256)")
        print("8. Digital Signature")
        print("9. File Encryption")
        print("10. File Decryption")
        print("11. Exit")

        choice = input("\n Enter choice: ")

        if choice == '1':
            from ciphers import caesar
            caesar.run()

        elif choice == '2':
            from ciphers import vigenere
            vigenere.run()

        elif choice == '3':
            from ciphers import playfair
            playfair.run()

        elif choice == '4':
            from ciphers import hill
            hill.run()

        elif choice == '5':
            from ciphers import rsa_module
            rsa_module.run()

        elif choice == "6":
            from ciphers import diffie_hellman
            diffie_hellman.run()

        elif choice == "7":
            from ciphers import hashing
            hashing.run()

        elif choice == "8":
            from ciphers import digital_signature
            digital_signature.run()

        elif choice == "9":
            from file_ops import file_encrypt
            file_encrypt.run()

        elif choice == "10":
            from file_ops import file_decrypt
            file_decrypt.run()

        elif choice == "11":
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()