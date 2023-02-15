import numpy as np
from typing import Sequence

_rng = np.random.default_rng()

def get_rng():
    return _rng


def set_rng(seed: [None, int, Sequence[int], np.random.SeedSequence, np.random.BitGenerator, np.random.Generator]):
    global _rng
    _rng = np.random.default_rng(seed)
