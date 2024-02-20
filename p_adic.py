# -*- coding: utf-8 -*-
"""
Created on February 20, 2024
@authors: 
    Elif KARTAL, Istanbul University, Faculty of Economics, Department of Management Information Systems
    Fatma CALISKAN,  Istanbul University, Faculty of Science, Department of Mathematics
    Beyaz Basak ESKISEHIRLI, Istanbul University, Faculty of Science, Department of Mathematics
    Zeki OZEN, Istanbul University, Faculty of Economics, Department of Management Information Systems
    
@title: p-adic calculations
@ver: 1.1
"""

import numpy as np
import pandas as pd
from functools import partial
from fractions import Fraction

# p-parameter of p-adic distance must be prime.
# This function controls if the p is prime or not.
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

# The output of this function is the total number of p's in the given number.
def is_div(num, div):
    counter = 0
    while num % div == 0:
        num //= div
        counter += 1
    return counter

# This function calculates the p-adic value of the given number.
def p_adic_val(my_num, p_num):
    if is_prime(p_num):
        if my_num != 0:
            fraction = Fraction(my_num).limit_denominator()
            if fraction.numerator != 0:
                return p_num ** (is_div(fraction.denominator, p_num) - is_div(fraction.numerator, p_num))
            else:
                return 0
        else:
            return 0
        
    else:
        print("p should be a prime number!")


# This function calculates the p-adic power and value of the given number.
def p_adic_pow_val(my_num, p_num):
    if is_prime(p_num):
        if my_num != 0:
            fraction = Fraction(my_num).limit_denominator()
            if fraction.numerator != 0:
                alpha = (is_div(fraction.denominator, p_num) - is_div(fraction.numerator, p_num))
                return -alpha, p_num ** alpha
            else:
                return 0
        else:
            return 0
    else:
        print("p should be a prime number!")
