import string

# Create 5x5 Playfair matrix from key
def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    # Fill with remaining letters A-Z except J
    for char in string.ascii_uppercase:
        if char != "J" and char not in used:
            matrix.append(char)
            used.add(char)

    # Convert to 5x5
    return [matrix[i:i+5] for i in range(0, 25, 5)]


# Locate position of a letter in matrix
def find_pos(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return None


# Prepare text into digraphs
def prepare_text(text):
    text = text.upper().replace("J", "I")
    cleaned = ""

    # Remove non-letters
    for ch in text:
        if ch.isalpha():
            cleaned += ch

    # Insert X between repeating letters in a pair
    i = 0
    result = ""
    while i < len(cleaned):
        a = cleaned[i]
        b = ""

        if i + 1 < len(cleaned):
            b = cleaned[i+1]
        else:
            b = "X"  # padding

        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2

    return result


def encrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)

    if r1 == r2:
        # Same row → shift right
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]

    elif c1 == c2:
        # Same column → shift down
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]

    else:
        # Rectangle → take opposite corners
        return matrix[r1][c2] + matrix[r2][c1]


def decrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)

    if r1 == r2:
        # Same row → shift left
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

    elif c1 == c2:
        # Same column → shift up
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

    else:
        # Rectangle rule reversed
        return matrix[r1][c2] + matrix[r2][c1]


def encrypt(text, key):
    matrix = generate_matrix(key)
    text = prepare_text(text)

    result = ""
    for i in range(0, len(text), 2):
        result += encrypt_pair(matrix, text[i], text[i+1])
    return result


def decrypt(cipher, key):
    matrix = generate_matrix(key)

    result = ""
    for i in range(0, len(cipher), 2):
        result += decrypt_pair(matrix, cipher[i], cipher[i+1])
    return result


def run():
    print("\n--- Playfair Cipher ---")
    text = input("Enter text: ")
    key = input("Enter key: ")

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("\nMatrix used:")
    matrix = generate_matrix(key)
    for row in matrix:
        print(row)

    print("\nEncrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
