from utils.number_theory import mod_exp

def run():
    print("\n--- Diffie-Hellman Key Exchange ---")

    # Public values
    p = 263  # prime
    g = 5    # primitive root

    print(f"\nPublic Prime (p): {p}")
    print(f"Public Base (g): {g}")

    # Private keys
    a = int(input("\nEnter Alice's private key (a): "))
    b = int(input("Enter Bob's private key (b): "))

    # Compute public values
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)

    print(f"\nAlice sends A = {A}")
    print(f"Bob sends B = {B}")

    # Compute shared secret
    shared_A = mod_exp(B, a, p)
    shared_B = mod_exp(A, b, p)

    print(f"\nShared Secret (Alice computes): {shared_A}")
    print(f"Shared Secret (Bob computes):   {shared_B}")
