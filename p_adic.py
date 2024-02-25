# -*- coding: utf-8 -*-
"""
Created on February 16, 2024
@authors: 
    Elif KARTAL, Istanbul University, Faculty of Economics, Department of Management Information Systems
    Beyaz Basak ESKISEHIRLI, Faculty of Science, Department of Mathematics
    Fatma CALISKAN, Faculty of Science, Department of Mathematics
    Zeki OZEN, Istanbul University, Faculty of Economics, Department of Management Information Systems
    
@title: p-adic Module
@ver: 1.1
"""

import numpy as np
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

# This function calculates the p-adic absolute value of the given number.
def p_adic_val(m_num, p_num):
    if is_prime(p_num):
        if m_num != 0:
            fraction = Fraction(m_num).limit_denominator()
            return np.round(p_num ** (is_div(fraction.denominator, p_num) - is_div(fraction.numerator, p_num)),6)
        else:
            return 0    
    else:
        print("p should be a prime number!")


# This function calculates the order and the p-adic absolute value of the given number.
def p_adic_pow_val(my_num, p_numb):
    if is_prime(p_numb):
        if my_num != 0:
            fraction = Fraction(my_num).limit_denominator()
            my_alpha = (is_div(fraction.denominator, p_numb) - is_div(fraction.numerator, p_numb))
            return -my_alpha, np.round(p_numb ** my_alpha, 6)
        else:
            return 0
    else:
        print("p should be a prime number!")
