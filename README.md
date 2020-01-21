# shamir

This short Python program implements Shamir's Secret Sharing Scheme (SSS).

## High-level Overview of SSS

Suppose you have nuclear launch codes that should stay locked with a key, K, unless k of
n generals decide to obtain the launch codes and use them. SSS allows a dealer to distribute
public and private keys (one pair per general) such that when k private keys and their corresponding
public keys are known, one can recover the key K.

# Algorithm Step-by-Step Explanation

The algorithm proceeds by the following steps.

## Part 1: Generate keys

1. Randomly generate n x_i's (public keys).

2. Randomly generate k a_i's (except for a_0, which is designated to be THE secret key a_0 = K),
which correspond to the coefficients in

![equation](http://www.sciweavers.org/upload/Tex2Img_1579595743/render.png)

3. Compute f(x_i) = y_i for all x_i's and designate those as secret keys to be
distributed for every individual.

## Part 2: Recover the secret key K
4. Obtain any combination k of the n y_i's and their corresponding x_i's.

5. Define the Lagrange Polynomial basis for such a data set:

![equation](http://www.sciweavers.org/upload/Tex2Img_1579595968/render.png)

6. Determine that the polynomial interpolation must be

![equation](http://www.sciweavers.org/upload/Tex2Img_1579595772/render.png)

7. Determine K = a_0, which will be K = p(0)

This implementation uses a finite field of cardinality p = 2**127 - 1 by default (can be changed with
an argument). See more explanation about how SSS works here:
https://en.wikipedia.org/wiki/Shamir's_Secret_Sharing
