"""
A demonstration of using the centralized RNG-state system in a multi-process environment which uses a simple
master-worker setup such that the master knows in advance how many workers it needs to spawn ("nworkers").
"""

import rngtest
from rngtest.sub1.sub1test import f1, f2
from numpy.random import SeedSequence, Philox

seed = 100
nworkers = 10

ss = SeedSequence(seed)

for wid, seed in ss.spawn(nworkers):
    bit_generator = Philox(seed)
    rngtest.set_rng(bit_generator)

    a = [f1() for _ in range(10)]
    rngtest.set_rng([wid, seed])
    b = [f1() for _ in range(5)] + [f2() for _ in range(5)]
    print(a == b)
    print(a)
