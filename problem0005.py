# -*- mode: python; encoding:utf-8-unix -*- -*-
#
#

import os, sys

# 2520 = 5, 2, 2, 2, 3, 3, 7
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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
def gcd(number1, number2):
    result = 1
    tmp = int(number2)
    if (number1 > number2):
        tmp = int(number1)
        
    for i in range(2, tmp):
        if isprime(i):
            if (i > number1) or (i>number2):
                break
            print ( i, result, number1, number2)
            while ((number1 != 1) and (number2 != 1) and
                   ((number1 % i) == 0) and ((number2 % i) == 0)):
                result = result * i
                number1 = int(number1 / i)
                number2 = int(number2 / i)
                print ("QQ",  i, result, number1, number2)
    result = int(result * number1 * number2)            
    return (result)


#
#
#
#    
#
#
if __name__ == "__main__":
    # print ( smallestmultiple(2520)) 

    #print( gcd( 2*3*5*7, 2*2*11 ), 2*2*3*5*7*11)
    work = 2
    for i in range(3, 21):
        work = gcd(work, i)
        print (">>", i , work)
    print( work )
