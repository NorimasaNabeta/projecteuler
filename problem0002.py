
import os, sys

sum = 0
f1 = 1
f2 = 2
fseq = [1, 2]
for i in range(1,100):
    next = fseq[i-1] + fseq[i]
    if next < 4000000:
        fseq.append(next)
        print (i, next)
    else:
        break

sum = 0    
for idx in range(0, len(fseq)):
    if ((fseq[idx] % 2) == 0):
        sum = sum + fseq[idx]
        
print (sum)
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# IndexError: list index out of range
