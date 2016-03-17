import multiprocessing

import math

from mapreduce import SimpleMapReduce


def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"


def factorize(n):
    return n, factorize_naive(n)


def find_primes(data):
    p, factors = data
    return p, len(factors) == 1


def get_the_primes(lista):
    ret = []
    for p, is_prime in lista:
        if is_prime:
            ret.append(p)
    return ret


if __name__ == '__main__':
    lista = SimpleMapReduce(factorize, find_primes)(range(2 ** 20, 2 ** 20 + 2 ** 15))
    l = len(multiprocessing.Pool().apply(get_the_primes, [lista]))
    print 2 ** 12 / math.log(2 ** 12, math.e), 2 ** 10, l
