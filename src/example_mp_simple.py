"""
A demonstration of using the centralized RNG-state system in a simple multi-process environment where the RNG is being
initialized by a worker which knows its own worker id ("wid") and was given a seed common to all workers ("seed"). This
is a somewhat usable but not really the most robust way of handling this use-case.
"""

import rngtest
from rngtest.sub1.sub1test import f1, f2

seed = 100
wid = 10

# This seeding method is quite good, definitely better than using "seed+wid", but not state-of-the-art in terms of
# theoretical guarantees.
rngtest.set_rng([wid, seed])
a = [f1() for _ in range(10)]

rngtest.set_rng([wid, seed])
b = [f1() for _ in range(5)] + [f2() for _ in range(5)]

print(f"Verifying if the RNG state was shared across functions of the same library: {a == b}")
