"""
Find PI to the Nth Digit
========================

Enter a number and have the program generate PI up to that many decimal
places. Keep a limit to how far the program will go.

These solutions all use the Bailey-Borwein-Plouffe formula.

-----

>>> pi_mpmath(50)
'3.1415926535897932384626433832795028841971693993751'
>>> pi_decimal(50)
'3.1415926535897932384626433832795028841971693993751'

"""

import decimal

from mpmath import inf, mp, nsum


def pi_mpmath(n):
    """Calculate PI to the Nth digit.

    I figured using mpmath would work well, but this is not very
    efficient. With n = 1000, it took over a minute on my laptop.
    """
    mp.dps = n
    return str(nsum(lambda k: (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6)) / 16**k, (0, inf)))


def pi_decimal(n):
    """Calculate PI to the Nth digit.

    This one uses the native python Decimal type that allows arbitrary
    precision. With n = 1000, it took less than a second on my laptop.
    """
    D = decimal.Decimal
    decimal.getcontext().prec = n+10
    pi = D(0)
    k = 0
    tail_prev = ''
    while True:
        pi += (D(4)/D(8*k+1) - D(2)/D(8*k+4) - D(1)/D(8*k+5) - D(1)/D(8*k+6)) / D(16)**D(k)
        tail = str(pi)[n+1:-1]
        if tail == tail_prev:
            break
        tail_prev = tail
        k += 1
    decimal.getcontext().prec = n
    return str(pi * D(1))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
