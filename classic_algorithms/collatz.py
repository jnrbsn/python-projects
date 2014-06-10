"""
Collatz Conjecture
==================

Start with a number n > 1. Find the number of steps it takes to reach
one using the following process: If n is even, divide it by 2. If n is
odd, multiply it by 3 and add 1.

-----

>>> collatz(1)
[1]
>>> collatz(2)
[2, 1]
>>> collatz(3)
[3, 10, 5, 16, 8, 4, 2, 1]
>>> collatz(4)
[4, 2, 1]
>>> collatz(5)
[5, 16, 8, 4, 2, 1]

"""


def collatz(n):
    """Return a list of steps to demonstrate the Collatz Conjecture.

    This can take an integer or a list of steps so far in order to make
    recursion a little better.
    """
    if isinstance(n, int):
        # An integer was passed in
        steps = [n]
    else:
        # A list of steps was passed in
        steps, n = n, n[-1]
    if n == 1:
        # We're done
        return steps
    if n % 2 == 0:
        steps.append(n / 2)
    else:
        steps.append((3 * n) + 1)
    return collatz(steps)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
