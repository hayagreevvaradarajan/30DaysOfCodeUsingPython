#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    reversed_array = arr[::-1]
    output_string = ''
    for i in range(len(reversed_array)):
        output_string+= str(reversed_array[i]) + ' '
    print(output_string)