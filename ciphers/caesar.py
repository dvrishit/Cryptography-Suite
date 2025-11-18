def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def run():
    print("\n--- Caesar Cipher ---")
    text = input("Enter text: ")
    shift = int(input("Enter shift value: "))

    encrypted = encrypt(text, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted Text: ", encrypted)
    print("Decrypted Text: ", decrypted)

