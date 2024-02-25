# -*- coding: utf-8 -*-
"""
Created on February 16, 2024
@authors: 
    Elif KARTAL, Istanbul University, Faculty of Economics, Department of Management Information Systems
    Beyaz Basak ESKISEHIRLI, Faculty of Science, Department of Mathematics
    Fatma CALISKAN, Faculty of Science, Department of Mathematics
    Zeki OZEN, Istanbul University, Faculty of Economics, Department of Management Information Systems
    
@title: Examples with p-adic calculations 
"""

import p_adic

x = 25

# p_adic_val() function returns the p-adic absolute value of a given number.
x_p2 = p_adic.p_adic_val(x, p_num=2)
print("2-adic value of ", x, " is ", x_p2)

x_p3 = p_adic.p_adic_val(x, p_num=3)
print("3-adic value of ", x, " is ", x_p3)

x_p5 = p_adic.p_adic_val(x, p_num=5)
print("5-adic value of ", x, " is ", x_p5)

y = 16
y_p2 = p_adic.p_adic_val(y, p_num=2)
print("2-adic value of ", y, " is ", y_p2)

# p_adic_pow_val() function returns both the ord and the the p-adic absolute value of the given number.

y_p2_ord, y_p2_val = p_adic.p_adic_pow_val(y, p_numb=2)
print(y_p2_ord)
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

r1 = -54
print("3-adic value of ", r1, " is ", p_adic.p_adic_val(r1, p_num=3))


s = -(24/16)
print("2-adic value of ", s, " is ", p_adic.p_adic_val(s, p_num=2))

print(p_adic.p_adic_pow_val(s, p_numb=2))

s1 = 8
print(p_adic.p_adic_pow_val(s1, p_numb=2))

s2 = 100
print(p_adic.p_adic_pow_val(s2, p_numb=5))

s3 = 0.270
print(p_adic.p_adic_pow_val(s3, p_numb=3))

s4 = 0.270
print(p_adic.p_adic_pow_val(s4, p_numb=5))

# p-parameter of p_adic_val() function must be prime!
m = 16
print(p_adic.p_adic_val(m, p_num=4))
