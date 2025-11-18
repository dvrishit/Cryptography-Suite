def xor_decrypt(data, key):
    decrypted = bytearray()
    for byte in data:
        decrypted.append(byte ^ key)
    return decrypted


def run():
    print("\n--- File Decryption ---")

    file_path = input("Enter path of .enc file to decrypt: ")

    try:
        with open(file_path, "rb") as f:
            data = f.read()

        key = int(input("Enter decryption key (0-255): "))

        decrypted_data = xor_decrypt(data, key)

        output_file = "data/decrypted_files/output.txt"
        with open(output_file, "wb") as f:
            f.write(decrypted_data)

        print(f"\nDecrypted file saved as: {output_file}")

    except FileNotFoundError:
        print("File not found!")
