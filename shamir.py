"""
Shamir's Secret Sharing Scheme
Author: Rodrigo Castellon

This short Python program implements Shamir's Secret Sharing Scheme (SSS), which goes like this:

Suppose you have nuclear launch codes that should stay locked with a key, K, unless k of
n generals decide to obtain the launch codes and use them. SSS allows a dealer to distribute
public and private keys (one pair per general) such that when k private keys and their corresponding
public keys are known, one can recover the key K.

This relies on the fact that a polynomial interpolation given n points is unique.

------------- ALGORITHM -------------
The algorithm proceeds by the following steps:

# Part 1: Generate keys
1. Randomly generate n x_i's (public keys).

2. Randomly generate k a_i's (except for a_0, which is designated to be THE secret key a_0 = K),
which correspond to the coefficients in

f(x) = a_0 + a_1 x + a_2 x^2 + ... + a_{k-1} x^{k-1}

3. Compute f(x_i) = y_i for all x_i's and designate those as secret keys to be
distributed for every individual.

# Part 2: Recover the secret key K
4. Obtain any combination k of the n y_i's and their corresponding x_i's.

5. Define the Lagrange Polynomial basis for such a data set:

{f_0(x), ... f_i(x), ..., f_k(x) | f_i(x) = \prod_{j=0, j!=i}^k (x - x_j) / (x_i - x_j)}

6. Determine that the polynomial interpolation must be

p(x) = \sum_{i=0}^k y_i f_i(x)

7. Determine K = a_0, which will be K = p(0)
------------- END ALGORITHM -------------

This implementation uses a finite field of cardinality p = 2**127 - 1 by default (can be changed with
an argument)

See more explanation about how it works here:
https://en.wikipedia.org/wiki/Shamir's_Secret_Sharing
"""
import argparse

from utils import *

def parse_arguments():
    parser = argparse.ArgumentParser(description='Shamir\'s Secret Sharing Scheme', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', help='number of individuals', type=int, default=50)
    parser.add_argument('-k', help='number of individuals necessary to obtain key', type=int, default=20)
    parser.add_argument('-K', help='the secret key', type=int, default=1337)
    parser.add_argument('-p', help='the prime used for the field', type=int, default=2**127 - 1)
    parser.add_argument('-v', help='verbose mode', action='store_true', default=False)
    args = parser.parse_args()

    return args

def main(config):
    print('#### Shamir\'s Secret Sharing Scheme ####\n')
    print('p={}'.format(config['p']))
    print('K={} (the key)\n'.format(config['K']))
    print('#########################################\n')
    
    public_keys = choose_public_keys(config)
    secret_keys = choose_secret_keys(public_keys, config)

    if config['v']:
        print('Distributed public keys:\n{}'.format(public_keys))
        print('Distributed secret keys:\n{}\n'.format(secret_keys))

    # choose k random keys
    boolean_mask = np.random.permutation([False]*(secret_keys.shape[0] - config['k']) + [True]*config['k'])
    chosen_secret_keys = secret_keys[boolean_mask]
    chosen_public_keys = public_keys[boolean_mask]

    if config['v']:
        print('submitted:')
        print('public keys: {}'.format(chosen_public_keys))
        print('private keys: {}'.format(chosen_secret_keys))

    # recover a_0 = K
    K = recover(chosen_secret_keys, chosen_public_keys, config)

    print('recovered K={}'.format(K))

if __name__ == '__main__':
    args = parse_arguments()
    config = {'n': args.n, 'k': args.k, 'K': args.K, 'p': args.p, 'v': args.v}

    main(config)

