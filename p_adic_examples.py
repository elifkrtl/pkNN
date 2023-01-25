# -*- coding: utf-8 -*-
"""
Created on January 24, 2023
@authors: 
    Elif KARTAL, Istanbul University, Faculty of Economics, Department of Management Information Systems 
    Beyaz Basak ESKISEHIRLI, Faculty Of Science, Department Of Mathematics
    Fatma CALISKAN, Faculty Of Science, Department Of Mathematics
    
@title: Examples with p-adic Values and p-adic Distance
"""

import p_adic

# p-adic Values

x = 25

# p_adic_val() function returns p-adic value of a given number.
x_p2 = p_adic.p_adic_val(x, p_num=2)
print("2-adic value of ", x, " is ", x_p2)

x_p3 = p_adic.p_adic_val(x, p_num=3)
print("3-adic value of ", x, " is ", x_p3)

x_p5 = p_adic.p_adic_val(x, p_num=5)
print("5-adic value of ", x, " is ", x_p5)

y = 16
y_p2 = p_adic.p_adic_val(y, p_num=2)
print("2-adic value of ", y, " is ", y_p2)

# p_adic_pow_val() function returns both p-adic power and p-adic value.
y_p2_pow, y_p2_val = p_adic.p_adic_pow_val(y, p_num=2)
print(y_p2_pow)
print(y_p2_val)

y_p3 = p_adic.p_adic_val(y, p_num=3)
print("3-adic value of ", y, " is ", y_p3)

y_p5 = p_adic.p_adic_val(y, p_num=5)
print("5-adic value of ", y, " is ", y_p5)

z = -16
z_p = p_adic.p_adic_val(z, p_num=5)
print("5-adic value of ", z, " is ", z_p)

t = 0
print("2-adic value of ", t, " is ", p_adic.p_adic_val(t, p_num=2))
print("3-adic value of ", t, " is ", p_adic.p_adic_val(t, p_num=3))
print("5-adic value of ", t, " is ", p_adic.p_adic_val(t, p_num=5))
print("17-adic value of ", t, " is ", p_adic.p_adic_val(t, p_num=17))

p = 1
print("2-adic value of ", p, " is ", p_adic.p_adic_val(p, p_num=2))
print("3-adic value of ", p, " is ", p_adic.p_adic_val(p, p_num=3))
print("5-adic value of ", p, " is ", p_adic.p_adic_val(p, p_num=5))
print("17-adic value of ", p, " is ", p_adic.p_adic_val(p, p_num=17))

r = -54
print("3-adic value of ", r, " is ", p_adic.p_adic_val(r, p_num=3))


s = -(24/16)
print("2-adic value of ", s, " is ", p_adic.p_adic_val(s, p_num=2))
print(p_adic.p_adic_pow_val(s, p_num=2))


# p-parameter of p_adic_val() function must be prime!
m = 16
print(p_adic.p_adic_val(m, p_num=4))

# p-adic Distance

import numpy as np

# Example - 1
# create two numpy arrays
a = np.array([1, 5, -20])
b = np.array([1, 10, 20])

dist_ab2 = p_adic.p_adic_dist(x_vec=a, y_vec=b, p_adic_p=2)
print("2-adic distance between ", a, " and ", b, " is ", dist_ab2)

dist_ab3 = p_adic.p_adic_dist(x_vec=a, y_vec=b, p_adic_p=3)
print("3-adic distance between ", a, " and ", b, " is ", dist_ab3)

dist_ab5 = p_adic.p_adic_dist(x_vec=a, y_vec=b, p_adic_p=5)
print("5-adic distance between ", a, " and ", b, " is ", dist_ab5)

dist_ab7 = p_adic.p_adic_dist(x_vec=a, y_vec=b, p_adic_p=7)
print("7-adic distance between ", a, " and ", b, " is ", dist_ab7)

dist_ab11 = p_adic.p_adic_dist(x_vec=a, y_vec=b, p_adic_p=11)
print("11-adic distance between ", a, " and ", b, " is ", dist_ab11)

dist_ab29 = p_adic.p_adic_dist(x_vec=a, y_vec=b, p_adic_p=29)
print("29-adic distance between ", a, " and ", b, " is ", dist_ab29)

# Example - 2
# create two numpy arrays
np.set_printoptions(suppress=True)

c = np.array([0.1, 50, 101.2, -23])
d = np.array([0.028, -40, 150.20, 35])

dist_cd2 = p_adic.p_adic_dist(x_vec=c, y_vec=d, p_adic_p=2)
print("2-adic distance between ", c, " and ", d, " is ", dist_cd2)

dist_cd3 = p_adic.p_adic_dist(x_vec=c, y_vec=d, p_adic_p=3)
print("3-adic distance between ", c, " and ", d, " is ", dist_cd3)

dist_cd5 = p_adic.p_adic_dist(x_vec=c, y_vec=d, p_adic_p=5)
print("5-adic distance between ", c, " and ", d, " is ", dist_cd5)

dist_cd7 = p_adic.p_adic_dist(x_vec=c, y_vec=d, p_adic_p=7)
print("7-adic distance between ", c, " and ", d, " is ", dist_cd7)

dist_cd11 = p_adic.p_adic_dist(x_vec=c, y_vec=d, p_adic_p=11)
print("11-adic distance between ", c, " and ", d, " is ", dist_cd11)

dist_cd29 = p_adic.p_adic_dist(x_vec=c, y_vec=d, p_adic_p=29)
print("29-adic distance between ", c, " and ", d, " is ", dist_cd29)









