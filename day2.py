import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = (meal_cost * tip_percent)/100
    tax_cost = (meal_cost * tax_percent)/100
    total_cost = meal_cost + tip_cost + tax_cost
    print(round(total_cost))

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
