# -*- coding: utf-8 -*-
"""
Created on January 24, 2023
@authors: 
    Elif KARTAL, Istanbul University, Faculty of Economics, Department of Management Information Systems 
    Beyaz Basak ESKISEHIRLI, Faculty Of Science, Department Of Mathematics
    Fatma CALISKAN, Faculty Of Science, Department Of Mathematics
    
@title: A Simple k-Nearest Neighbor Example with p-adic Distance, considering decimals before calculating p-adic values.
@data: In this example data is created by authors with random numbers.
"""

import p_adic
import numpy as np
import pandas as pd

my_data = pd.read_csv("data2.csv")

# Creating training and test datasets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(my_data.iloc[:,0:4], my_data.iloc[:,4], test_size=0.3, random_state=123)

# p-adic distance matrix of X_test and X_train
my_dist_matrix = p_adic.p_adic_dist_matrix(X_test, X_train, 2)

my_dist_matrix1 = p_adic.p_adic_dist_dec_matrix(X_test, X_train, 2, 1)

my_dist_matrix2 = p_adic.p_adic_dist_dec_matrix(X_test, X_train, 2, 2)

my_dist_matrix3 = p_adic.p_adic_dist_dec_matrix(X_test, X_train, 2, 3)

my_dist_matrix4 = p_adic.p_adic_dist_dec_matrix(X_test, X_train, 2, 4)

# MODELING
from sklearn.neighbors import KNeighborsClassifier

# Plain p-adic distance function.
knn_classifier = KNeighborsClassifier(n_neighbors = 3, metric=p_adic.p_adic_dist, metric_params={"p_adic_p": 2})
knn_classifier.fit(X_train, y_train)
y_pred = knn_classifier.predict(X_test)

# Using p_adic_dist_dec() function rounding numbers using 1 decimals, before calculating their p-adic values.
knn_classifier1 = KNeighborsClassifier(n_neighbors = 3, metric=p_adic.p_adic_dist_dec, metric_params={"p_adic_p": 2, "dist_dec": 1})
knn_classifier1.fit(X_train, y_train)
y_pred1 = knn_classifier1.predict(X_test)

# Using p_adic_dist_dec() function rounding numbers using 2 decimals, before calculating their p-adic values.
knn_classifier2 = KNeighborsClassifier(n_neighbors = 3, metric=p_adic.p_adic_dist_dec, metric_params={"p_adic_p": 2, "dist_dec": 2})
knn_classifier2.fit(X_train, y_train)
y_pred2 = knn_classifier2.predict(X_test)

# PERFORMANCE EVALUATION
from sklearn import metrics
metrics.accuracy_score(y_test,y_pred)
metrics.accuracy_score(y_test,y_pred1)
metrics.accuracy_score(y_test,y_pred2)
