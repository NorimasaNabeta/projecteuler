# -*- mode: python; encoding:utf-8-unix -*- -*-
#
#

import os, sys


# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrome( number ):
    flag = True
    strrep = "%i" % number
    for i in range(0, int(len(strrep)/2)):
        if (strrep[i] != strrep[len(strrep)-1-i]):
            flag = False
            break

    # print ( number, flag )
    return flag
#
#
#
if __name__ == "__main__":
    # ispalindrome( 123321 )
    # ispalindrome( 1234321 )
    maxvalue = 0
    for i in range(999, 101, -1):
        for j in range(i-1, 102, -1):
            rslt = i * j
            tmp = ispalindrome( rslt )
            if tmp :
                if maxvalue < rslt:
                    maxvalue = rslt
                print (tmp, i, j, rslt )

    print ("MAX:", maxvalue)
    # True 993 913 906609
