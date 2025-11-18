def xor_encrypt(data, key):
    encrypted = bytearray()
    for byte in data:
        encrypted.append(byte ^ key)
    return encrypted


def run():
    print("\n--- File Encryption ---")

    file_path = input("Enter path of text file to encrypt: ")

    try:
        with open(file_path, "rb") as f:
            data = f.read()

        key = int(input("Enter encryption key (0-255): "))

        encrypted_data = xor_encrypt(data, key)

        output_file = "data/encrypted_files/output.enc"
        with open(output_file, "wb") as f:
            f.write(encrypted_data)

        print(f"\nEncrypted file saved as: {output_file}")

    except FileNotFoundError:
        print("File not found!")
