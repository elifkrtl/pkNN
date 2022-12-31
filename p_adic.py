# -*- coding: utf-8 -*-
"""
Created on December 31, 2022
@author: Elif Kartal
@title: p-adic Module
"""
import numpy as np
from functools import partial
from fractions import Fraction

# V1.2
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def is_div(num, div):
    counter = 0
    while num % div == 0:
        num /= div
        counter += 1
    return counter

# Calculates the p-adic value. p should be a prime number.
def p_adic_val(my_num, p_num):
    if is_prime(p_num):
        if my_num != 0:
            f = Fraction(str(my_num))
            return p_num ** (is_div(f.denominator, p_num) - is_div(f.numerator, p_num))
        else:
            return 0
    else:
        print("p should be a prime number!")


# Calculates the p-adic distance of given 1D arrays.
def p_adic_dist(x_vec, y_vec, p_adic_p, dist_dec):
    return np.sum(np.array(list(map(partial(p_adic_val, p_num=p_adic_p), np.round(np.fabs(x_vec - y_vec), dist_dec)))))


