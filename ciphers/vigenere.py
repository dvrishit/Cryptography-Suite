def generate_key(text, key):
    key = key.upper()
    key_extended = ""

    key_index = 0
    for char in text:
        if char.isalpha():
            key_extended += key[key_index % len(key)]
            key_index += 1
        else:
            key_extended += char

    return key_extended


def encrypt(text, key):
    text = text.upper()
    key = generate_key(text, key)
    result = ""

    for t, k in zip(text, key):
        if t.isalpha():
            shift = ord(k) - ord('A')
            result += chr((ord(t) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += t

    return result


def decrypt(cipher, key):
    cipher = cipher.upper()
    key = generate_key(cipher, key)
    result = ""

    for c, k in zip(cipher, key):
        if c.isalpha():
            shift = ord(k) - ord('A')
            result += chr((ord(c) - ord('A') - shift + 26) % 26 + ord('A'))
        else:
            result += c

    return result


def run():
    print("\n--- Vigenere Cipher ---")
    text = input("Enter text: ").upper()
    key = input("Enter key word: ").upper()

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("\nEncrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
