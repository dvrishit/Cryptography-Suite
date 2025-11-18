import numpy as np
from utils.matrix_math import matrix_mod_inv

# Convert A=0, B=1, ... Z=25
def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))


def prepare_text(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"  # padding for odd length
    return text


def encrypt(text, key_matrix):
    text = prepare_text(text)
    result = ""

    for i in range(0, len(text), 2):
        pair = np.array([[char_to_num(text[i])],
                         [char_to_num(text[i+1])]])

        encrypted = np.dot(key_matrix, pair) % 26

        result += num_to_char(int(encrypted[0][0]))
        result += num_to_char(int(encrypted[1][0]))

    return result


def decrypt(cipher, key_matrix):
    inv_matrix = matrix_mod_inv(key_matrix, 26)
    result = ""

    for i in range(0, len(cipher), 2):
        pair = np.array([[char_to_num(cipher[i])],
                         [char_to_num(cipher[i+1])]])

        decrypted = np.dot(inv_matrix, pair) % 26

        result += num_to_char(int(decrypted[0][0]))
        result += num_to_char(int(decrypted[1][0]))

    return result


def run():
    print("\n--- Hill Cipher (2x2) ---")

    text = input("Enter text: ").upper()
    print("\nEnter 2x2 key matrix values:")

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))

    key_matrix = np.array([[a, b],
                           [c, d]])

    encrypted = encrypt(text, key_matrix)
    decrypted = decrypt(encrypted, key_matrix)

    print("\nEncrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
