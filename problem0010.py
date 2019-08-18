
# -*- mode: python; encoding:utf-8-unix -*- -*-
#
#

import os, sys
import datetime

from math import sqrt
#from numpy import sqrt

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


# 1999957 142907828981
# 1999969 142909828950
# 1999979 142911828929
# 1999993 142913828922
# 142913828922

def isprime( check ):
    flag = True
    for i in range(2, check-1):
        if (check % i == 0):
            flag = False
            break
    return flag

## 高速版
# p(0), p(1) p(2) ,,, p(n) が判っているときに、p(n+1) であることの判定に
# p(n)+1 からp(n+1) -1 の剰余判定は必要か？
#
def isprime_aux( db, top, check ):
    flag = True
    if check < top:
        if not check in db:
            flag = False
    else:
        for p in db:
            if (check % p == 0):
                flag = False
                break
        if flag:
            for i in range(top, check-1):
                if (check % i == 0):
                    flag = False
                    break
            
    return flag


#
#
#
if __name__ == "__main__":
    #limit = 2000000
    limit = 100000 # --> 454396537

    elapse_start = datetime.datetime.now()
    sum   = 0
    prime_top = 1
    prime_db = []
    for i in range(2, limit):
        if isprime_aux(prime_db, prime_top, i):
            prime_db.append(i)
            prime_top = i
            sum = sum + i
            print (i, sum)

    elapse_end = datetime.datetime.now()
    #print (primes)
    print ((elapse_end - elapse_start), sum)
