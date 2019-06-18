p, q = 37, 13

def is_prime(x):
    if x >= 2:
        for n in range(2, x):
            if x%n == 0:
                return False
            else:
                return True
    else:
        return True

def RSA_e(plaintext, p, q):
    if not is_prime(p) or not is_prime(q):
        return False
    n = p * q
    public = (p - 1) * (q - 1)
    ct = plaintext**pk%n
    return ct

def RSA_d(ciphertext, p, q):
    if not is_prime(p) or not is_prime(q):
        return False
    n = p * q
    private = #

