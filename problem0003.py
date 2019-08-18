# -*- mode: python; encoding:utf-8-unix -*- -*-
#
#

import os, sys

#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# python problem0003.py
# 1 13195.0
# 5 2639.0
# 7 377.0
# 13 29.0
# 29 1.0
# [1, 5, 7, 13, 29]

#
#
#
def isprime( check ):
    flag = True
    for i in range(2, check-1):
        if (check % i == 0):
            flag = False
            break
    return flag

#
#
#
def problem( number ):
    work = number
    divs = []
    for i in range(2, number-1):
        if isprime(i):
            if ((work % i) == 0):
                work = work/i
                divs.append(i)
                print ("True:  ", i, work)
                if work == 1:
                    break
            else:
                print ("False: ", i, work)
                
    print (divs)
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# IndexError: list index out of range

#
#
if __name__ == "__main__":
    # execute only if run as a script
    # print ( isprime(13) )
    #problem( 13195 )
    # print ( 600851475143 / 2 )
    problem( 600851475143 )

    
