"""
A demonstration of using the centralized RNG-state system to share the current random state with other libraries.
"""

import rngtest
from rngtest.sub1.sub1test import f1, f2

seed = 100

rngtest.set_rng(seed)
a = [f1() for _ in range(10)]

# Demonstration of importing the seeded RNG to this module.
rngtest.set_rng(seed)
rng = rngtest.get_rng()
b = [rng.random() for _ in range(10)]
print(f"Verifying if importing the RNG worked: {a == b}")

# Demonstration of creating new RNGs with a common shared random state, e.g. by passing this random state to other
# libraries.
import numpy as np
rngtest.set_rng(seed)
rng1 = np.random.default_rng(rngtest.get_rng().bit_generator)
rng2 = np.random.default_rng(rngtest.get_rng().bit_generator)
c = [rng1.random() for _ in range(5)] + [rng2.random() for _ in range(5)]
print(f"Verifying if the random state was indeed shared: {a == c}")
