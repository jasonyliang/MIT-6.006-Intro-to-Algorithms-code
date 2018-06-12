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

def RSA(public, p, q):

