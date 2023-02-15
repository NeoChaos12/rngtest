from rngtest import get_rng

def f1():
    # It is important to import the RNG this way in each atomic function call for the same reasons as why SciKit-Learn
    # asks users to pass either a RandomState or an entire RNG at each function call.
    rng = get_rng()
    return rng.random()

def f2():
    rng = get_rng()
    return rng.random()

if __name__ == "__main__":
    print(type(get_rng()))
    print(f1())