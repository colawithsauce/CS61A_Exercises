def prime_factors(n):
    """Print all prime factors of n
    >>> prime_factors(2)
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(4)
    2
    2
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(858)
    2
    3
    11
    13
    """

    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)


# The idea here is if n can not evenly divided by k(prime), then it also cannot
# evenly divided by i*k, where i belongs to integers. And if n can evenly divide
# i*k, then n must evenly divide k, where k is prime (even not needed).
def smallest_prime_factor(n):
    k = 2
    while n % k != 0:
        k = k + 1

    return k
