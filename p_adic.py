# -*- coding: utf-8 -*-
"""
Created on January 24, 2023
@authors: 
    Elif KARTAL, Istanbul University, Faculty of Economics, Department of Management Information Systems 
    Beyaz Basak ESKISEHIRLI, Faculty Of Science, Department Of Mathematics
    Fatma CALISKAN, Faculty Of Science, Department Of Mathematics
    
@title: p-adic Module V1.2
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
        num /= div
        counter += 1
    return counter

# This function calculates the p-adic value of the given number.
def p_adic_val(my_num, p_num):
    if is_prime(p_num):
        if my_num != 0:
            f = Fraction(str(my_num))
            return p_num ** (is_div(f.denominator, p_num) - is_div(f.numerator, p_num))
        else:
            return 0
    else:
        print("p should be a prime number!")
        
# This function calculates the p-adic power and value of the given number.
def p_adic_pow_val(my_num, p_num):
    if is_prime(p_num):
        if my_num != 0:
            f = Fraction(str(my_num))
            alpha = (is_div(f.denominator, p_num) - is_div(f.numerator, p_num))
            return -alpha, p_num ** alpha
        else:
            return 0
    else:
        print("p should be a prime number!")

# This function calculates the p-adic distance of given 1D arrays.
def p_adic_dist(x_vec, y_vec, p_adic_p):
    return np.sum(np.array(list(map(partial(p_adic_val, p_num=p_adic_p), np.fabs(x_vec - y_vec)))))

# This function calculates the p-adic distance of given 1D arrays, considering the decimals before calculating the p-adic values.
def p_adic_dist_dec(x_vec, y_vec, p_adic_p, dist_dec):
    return np.sum(np.array(list(map(partial(p_adic_val, p_num=p_adic_p), np.round(np.fabs(x_vec - y_vec), dist_dec)))))


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