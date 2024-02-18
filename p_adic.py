# -*- coding: utf-8 -*-
"""
Created on February 16, 2024
@authors: 
    Elif KARTAL, Istanbul University, Faculty of Economics, Department of Management Information Systems
    Fatma CALISKAN,  Istanbul University, Faculty of Science, Department of Mathematics
    Beyaz Basak ESKISEHIRLI,  Istanbul University, Faculty of Science, Department of Mathematics
    Zeki OZEN, Istanbul University, Faculty of Economics, Department of Management Information Systems
    
@title: p-adic Module
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


# This function calculates the p-adic distance of given 1D arrays.
def p_adic_dist(x_vec, y_vec, p_adic_p):
    diff = np.round(np.fabs(x_vec - y_vec),6)
    p_adic_vals = np.vectorize(partial(p_adic_val, p_num=p_adic_p),  otypes=[float])(diff)
    return np.sum(p_adic_vals)


# This function calculates the p-adic distance of given 1D arrays, considering the decimals before calculating the p-adic values.
def p_adic_dist_dec(x_vec, y_vec, p_adic_p, dist_dec):
    r_diff = np.round(np.fabs(x_vec - y_vec), dist_dec)
    p_adic_vals_dec = np.vectorize(partial(p_adic_val, p_num=p_adic_p),  otypes=[float])(r_diff)
    return np.sum(p_adic_vals_dec)


# This function calculates the p-adic distance of given nxm dataframes.
def p_adic_dist_matrix(X, Y, p_adic_p):
    my_distMatrix = pd.DataFrame()
    i=0
    j=0
    for i in range(0,X.shape[0]):
        for j in range(0, Y.shape[0]):
            my_distMatrix.loc[i,j] = p_adic_dist(X.iloc[i,:].to_numpy(), Y.iloc[j,:].to_numpy(), p_adic_p=2)
    return my_distMatrix

# This function calculates the p-adic distance of given nxm dataframes, considering the decimals before calculating the p-adic values.
def p_adic_dist_dec_matrix(X, Y, p_adic_p, dec):
    my_distMatrix = pd.DataFrame()
    i=0
    j=0
    for i in range(0,X.shape[0]):
        for j in range(0, Y.shape[0]):
            my_distMatrix.loc[i,j] = p_adic_dist_dec(X.iloc[i,:].to_numpy(), Y.iloc[j,:].to_numpy(), p_adic_p=2, dist_dec=dec)
    return my_distMatrix
