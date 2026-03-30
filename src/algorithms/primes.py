import math


def is_prime(n):
    """Returnera True om n är ett primtal.
    """
    if n < 2:
        return False
    if n == 2:
        return True

    limit = math.ceil( math.sqrt(n) )
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def get_primes(amount):
    """Returnera en lista med de amount första primtalen.
    Tidskomplexitet: O(n * log n)
    """
    primes = []
    i = 2
    while len(primes) < amount:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes
