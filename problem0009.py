# -*- mode: python; encoding:utf-8-unix -*- -*-
#
#

import os, sys
from math import sqrt
#from numpy import sqrt

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# 200 375 425 1000

#     1234567890123
# 197 5576689664895 23514624000
#
if __name__ == "__main__":
    limit = 1000
    for i in range(1, limit):
        for j in range(i+1, limit):
            tmp = i*i + j*j
            k = sqrt(tmp)
            if ((k == int(k)) and ( (i+j+int(k)) == 1000)):
                print (i, j, int(k), (i+j+int(k)))
                print (i* j*int(k))
