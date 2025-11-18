import hashlib
from utils.number_theory import mod_exp
from ciphers.rsa_module import generate_keys

def sha256_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

def sign(message, private_key):
    d, n = private_key
    hash_value = sha256_hash(message)
    hash_int = int(hash_value, 16)

    signature = mod_exp(hash_int, d, n)
    return signature

def verify(message, signature, public_key):
    e, n = public_key
    hash_value = sha256_hash(message)
    hash_int = int(hash_value, 16)

    decrypted = mod_exp(signature, e, n)

    # Match lower bits because RSA modulus n is smaller than 256-bit hash
    return decrypted == (hash_int % n)

def run():
    print("\n--- Digital Signature Demo ---")

    # Generate RSA keys for signing
    public_key, private_key = generate_keys()

    print("\nPublic Key:", public_key)
    print("Private Key:", private_key)

    message = input("\nEnter message to sign: ")

    signature = sign(message, private_key)

    print("\nGenerated Signature (number):")
    print(signature)

    print("\nVerifying signature...")
    valid = verify(message, signature, public_key)

    if valid:
        print("Signature Verified: VALID")
    else:
        print("Signature Verified: INVALID")
