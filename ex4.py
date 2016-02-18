"""
def newfunc(*args):
    x = 1
    p = [x**i for i in args]
    return p
print newfunc(1,2,3)

newfunc(2,2,3)

def feb(*args):
	p = [args ** args for args in args]
	return p

print feb(2,2,3)
"""
from __future__ import division
import math

def fib(n):
    SQRT5 = math.sqrt(5)
    PHI = (SQRT5 + 1) / 2
    return int(PHI ** n / SQRT5 + 0.5)

print fib(50)