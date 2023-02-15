"""
A demonstration of using the centralized RNG-state system in a multi-process environment which uses a simple
master-worker setup such that the master knows in advance how many workers it needs to spawn ("nworkers").
"""

import rngtest
from rngtest.sub1.sub1test import f1, f2
from numpy.random import SeedSequence, Philox

main_seed = 100
nworkers = 10

ss = SeedSequence(main_seed)
arrs = []
for wid, worker_seed in enumerate(ss.spawn(nworkers)):
    bit_generator = Philox(worker_seed)
    rngtest.set_rng(bit_generator)
    a = [f1() for _ in range(10)]

    bit_generator = Philox(worker_seed)
    rngtest.set_rng(bit_generator)
    b = [f1() for _ in range(5)] + [f2() for _ in range(5)]

    print(f"Worker [{wid}] - Verifying if the RNG state was shared across functions of the same library: {a == b}")
    arrs.append(a)

print(f"Verifying if the workers generated different numbers: {not any([x == y for x in arrs[:-1] for y in arrs[1:]])}")
# TODO: Fix
