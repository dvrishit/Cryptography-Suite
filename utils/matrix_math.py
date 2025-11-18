import numpy as np

# Find modular inverse of determinant
def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Modular inverse of 2x2 matrix
def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det = det % modulus

    det_inv = mod_inv(det, modulus)
    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod 26.")

    # Adjugate matrix for 2x2
    adj = np.array([[matrix[1][1], -matrix[0][1]],
                    [-matrix[1][0], matrix[0][0]]])

    return (det_inv * adj) % modulus
