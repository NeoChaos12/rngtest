"""
A demonstration of using the centralized RNG-state system in a multi-process environment where each worker is assumed
to have no knowledge of the other workers except for having a unique worker ID ("wid") and a common initial seed
("seed")
"""

import rngtest
from rngtest.sub1.sub1test import f1, f2
from numpy.random import SeedSequence, Philox

# Ideally, the shared seed itself should be a very large value (64- or 128-bit integer) that has itself been randomly
# generated and frozen
seed = 2**88 + 2**42 + 2**37 + 2**22 + 2**13
wid = 420

bit_generator = Philox(seed + wid)  # Unlike MT19937 (np.random.RandomState), this is safe to do with Philox
rngtest.set_rng(bit_generator)
a = [f1() for _ in range(10)]

bit_generator = Philox(seed + wid)  # Unlike MT19937 (np.random.RandomState), this is safe to do with Philox
rngtest.set_rng(bit_generator)
b = [f1() for _ in range(5)] + [f2() for _ in range(5)]
print(f"Verifying if the reseeding was successful: {a == b}")
