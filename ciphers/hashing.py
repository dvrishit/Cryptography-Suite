import hashlib

def run():
    print("\n--- SHA-256 Hashing ---")
    message = input("Enter message to hash: ")

    hash_obj = hashlib.sha256(message.encode())
    digest = hash_obj.hexdigest()

    print("\nSHA-256 Digest:")
    print(digest)
