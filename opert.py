#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:10:43 2020

@author: jagveer

Using one line of code in python print the prime numbers in the range of
 1 to 150 *
"""



[value for value in range (1,150) if all(value%n!=0 for n in range(2,value))]
    
import pandas as pd
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                       'B': ['B0', 'B1', 'B2', 'B3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                       index=[0, 1, 2, 3])
    

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                       'B': ['B4', 'B5', 'B6', 'B7'],
                      'C': ['C4', 'C5', 'C6', 'C7'],
                       'D': ['D4', 'D5', 'D6', 'D7']},
                     index=[4, 5, 6, 7])

result=pd.concat([df1,df2])

pd.concat([epl1.append(epl2, ignore_index = True), epl_addn], axis = 1)




Assignment Q3: Given a 2D NumPy array, write a code to sort it by the 
1st column. Print the final sorted array as a NumPy array only. *

import numpy as np
arr2D = np.array([[11, 12, 13, 22], [11, 7, 23, 14], [31, 10, 33, 7]])
print('*** Sort 2D Numpy array by 1st column i.e. column at index 0 ***')
 
  # Sort 2D numpy array by first column
sortedArr = arr2D[arr2D[:,[0,1]].argsort()]



a = a[a[:,1].argsort(kind='mergesort')]
a = a[a[:,0].argsort(kind='mergesort')]






















