#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * int(factorial(n-1))
    
#Stub code:
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()
