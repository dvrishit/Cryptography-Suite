from utils.number_theory import gcd, mod_inverse, mod_exp
import random

# Generate a random prime (small primes for demo)
def generate_prime():
    primes = [
        101, 103, 107, 109, 113, 127, 131, 137, 139,
        149, 151, 157, 163, 167, 173, 179, 181, 191
    ]
    return random.choice(primes)


def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # standard RSA public exponent

    # ensure e and phi(n) are coprime
    while gcd(e, phi) != 1:
        e += 2

    d = mod_inverse(e, phi)

    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    cipher_numbers = []

    for char in message:
        cipher_numbers.append(mod_exp(ord(char), e, n))

    return cipher_numbers


def decrypt(cipher_list, private_key):
    d, n = private_key
    plain = ""

    for num in cipher_list:
        plain += chr(mod_exp(num, d, n))

    return plain


def run():
    print("\n--- RSA Encryption/Decryption ---")

    public_key, private_key = generate_keys()

    print("\nGenerated Public Key:", public_key)
    print("Generated Private Key:", private_key)

    message = input("\nEnter message to encrypt: ")

    cipher = encrypt(message, public_key)
    print("\nEncrypted (numbers):", cipher)

    decrypted = decrypt(cipher, private_key)
    print("Decrypted Text:", decrypted)
