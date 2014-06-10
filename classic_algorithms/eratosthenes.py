"""
Sieve of Eratosthenes
=====================

The sieve of Eratosthenes is one of the most efficient ways to find all
of the smaller primes (below 10 million or so).

-----

>>> eratosthenes1(50)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> eratosthenes2(50)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

"""


def eratosthenes1(n):
    """Generate a list of prime numbers below the specified value.

    This was my original idea, but as I started writing it, I realized
    it was a bad idea. This basically removes non-primes from the list
    until all that's left are primes. This one is slightly more memory
    efficient, but the difference lowers as you scale.
    """
    numbers = range(2, n)
    i = 0
    while i < len(numbers):
        k = i + 1
        while k < len(numbers):
            if numbers[k] % numbers[i] == 0:
                del numbers[k]
            k += 1
        i += 1
    return numbers


def eratosthenes2(n):
    """Generate a list of prime numbers below the specified value.

    This one is waaaaay more efficient. It took about 240 milliseconds
    on my laptop when n = 1 million. Plus it uses some cool Python
    slicing magic. I tested the equivalent with a loop, and it didn't
    scale as well. So there's definitely some optimization with the
    slicing magic. This is also definitely more Pythonic.
    """
    switches = [True] * n
    primes = []
    i = 2
    while i < n:
        primes.append(i)
        switches[i * 2::i] = [False] * (((n - 1) / i) - 1)
        i += 1
        while i < n and not switches[i]:
            i += 1
    return primes


if __name__ == '__main__':
    import doctest
    doctest.testmod()
