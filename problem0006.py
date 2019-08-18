# -*- mode: python; encoding:utf-8-unix -*- -*-
#
#

import os, sys


# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.


def sumofsquare( top ):
    result = 0
    for i in range(1, top+1):
        result = result + i * i
    return result

def problem( top ):
    sumofs = sumofsquare(top)
    sum = 0
    for i in range(1, top+1):
        sum = sum + i
    print (sum * sum - sumofs)

#    
#
#
if __name__ == "__main__":
    problem( 100 )
