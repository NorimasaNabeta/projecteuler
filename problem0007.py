# -*- mode: python; encoding:utf-8-unix -*- -*-
#
#

import os, sys

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


def isprime( check ):
    flag = True
    for i in range(2, check-1):
        if (check % i == 0):
            flag = False
            break
    return flag


def problem( cnt ):
    primes = []
    number = 2
    while( len(primes) < cnt):
        if isprime(number):
            primes.append(number)
        number = number + 1
        

    print (primes)
    return (list(reversed(primes))[0])

#    
#
#
if __name__ == "__main__":
    
    result = problem( 10001 )
    print ( "RSLT: ", result)
