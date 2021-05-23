#Stub code:
import math
import os
import random
import re
import sys

#Solution begins here:
def hourGlass(mat,n):
    max = -99999999999999999
    for i in range(n-2):
        for j in range(n-2):
            sum = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+1] + mat[i+2][j] + mat[i+2][j+1] + mat[i+2][j+2]
            if sum > max:
                max = sum
    return max

#Stub code:
if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split(' '))))
    print(hourGlass(arr,6))
