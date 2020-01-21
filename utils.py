"""
A utilities file
Author: Rodrigo Castellon
"""

import random
import numpy as np

from wiki import _divmod, _extended_gcd

# necessary for cryptographically secure
# random numbers
cryptogen = random.SystemRandom()

def choose_public_keys(config):
    """
    Choose n public keys randomly from the finite field.
    """
    # a hacky way to choose with replacement
    pubs = []
    while len(pubs) < config['n']:
        pubs += list(set(cryptogen.randint(0, config['p'] - 2) for i in range(config['n'] - len(pubs))))
        pubs = list(set(pubs))
    return np.array(pubs)

def choose_secret_keys(public_keys, config):
    """
    Randomly generate the polynomial and compute the secret keys
    given the known public keys.
    """
    A = np.array([cryptogen.randint(0, config['p'] - 2) for i in range(config['k'])])
    A[0] = config['K']

    # the lambda expression inside is just the polynomial function
    private_keys = np.array([np.sum([A[i] * (x ** i) for i in range(config['k'])]) % config['p'] for x in public_keys])

    return private_keys

# recover a_0 from the given secret keys
def recover(secret_keys, public_keys, config):
    """
    Recover the secret key from the given key pairs.
    """
    # since we only need a_0, no need to deal with
    # expanding everything

    # using numerators and denominators to avoid floating point imprecision
    nums = [np.prod([-public_keys[j] for j in range(config['k']) if i != j]) for i in range(config['k'])]
    dens = [np.prod([(public_keys[i] - public_keys[j]) for j in range(config['k']) if i != j]) for i in range(config['k'])]
    den = np.prod(dens)

    num = np.sum([_divmod((secret_keys[i] * nums[i] * den) % config['p'], dens[i], config['p']) for i in range(config['k'])])

    num = (_divmod(num, den, config['p']) + config['p']) % config['p']

    return int(round(num))

