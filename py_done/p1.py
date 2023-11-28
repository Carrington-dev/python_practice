#!/bin/python3

import math
import os
import random
import re
import sys

"""
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""

# def numCheck2(number):
#     print (number % 2, number)
#     if number >= 1 and number <= 100:
#         if number % 2 == 0:
#             if number >= 2 and number <= 5 and number % 2 == 0:
#                 print('Not Weird')
#             elif number >= 5 and number <= 20 and number % 2 == 0:
#                 print('Weird')
#             elif number >= 20 and number % 2 == 0:
#                 print('Not Weird')
#             else:
#              print('Weird')   
#         else:
#             print('Weird')
    
#     else:
#         print("Out of range")

def numCheck(number):
    print (number % 2, number)
    if number % 2 == 0:
        if number >= 2 and number <= 5:
                print('Not Weird')
        elif number >= 5 and number <= 20:
            print('Weird')
        elif number >= 20:
            print('Not Weird')
    else:
        print('Weird')
        

if __name__ == '__main__':
    # n = int(input().strip())
    n = random.randint(1,100)
    # print(n)
    numCheck(n)
