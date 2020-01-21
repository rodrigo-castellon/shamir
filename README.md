# shamir

This short Python program implements Shamir's Secret Sharing Scheme (SSS).

## Usage

First, make sure that NumPy is installed.

To run with the default configuration (n=50, k=20, K=1337, p=2**127-1), run
```
$ python shamir.py
```

Run with the help command to find how to configure
```
$ python shamir.py --help
```

Run with the `-v` flag for verbose mode, which prints out all of the keys:

## Example

Running in verbose mode with 5 individuals and 3 necessary to unlock the secret key:

```
$ python shamir.py -v -n 10 -k 3
```

```
#### Shamir's Secret Sharing Scheme ####

p=170141183460469231731687303715884105727
K=1337 (the key)

#########################################

Distributed public keys:
[159295934112048856104943720797459882023
 3897499456721215129662485829517641142
 106359069303894237915449798553830341915
 96436624917505388534534964576808954655
 82558760913992608939958392144080638617]
Distributed secret keys:
[47118056962547522296047871559126950388
 60504585901425677614619790584313779760
 104434369299853073791090724686225969560
 161648570216194248714687996555632176004
 49688957303007089389437824881931699753]

submitted:
public keys: [159295934112048856104943720797459882023
 96436624917505388534534964576808954655
 82558760913992608939958392144080638617]
private keys: [47118056962547522296047871559126950388
 161648570216194248714687996555632176004
 49688957303007089389437824881931699753]
recovered K=1337
```

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
