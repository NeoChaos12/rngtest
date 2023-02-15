"""
A demonstration of using the centralized RNG-state system in an ultra simpmle single-process use-case.
"""

import rngtest
from rngtest.sub1.sub1test import f1, f2

seed = 100

rngtest.set_rng(seed)
a = [f1() for _ in range(10)]

rngtest.set_rng(seed)
b = [f1() for _ in range(5)] + [f2() for _ in range(5)]  # Demonstration of automatic sharing of the current RNG state

print(a == b)
print(a)
