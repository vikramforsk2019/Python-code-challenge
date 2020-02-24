#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 17:13:34 2020

@author: jagveer
"""

def fib():
    a=0
    b=1
    print(a)
    sum_of=a+b
    a=b
    b=sum_of

size=int(input('enter nth term>>'))
a=0
b=1
for i in range(0,size):
    print(a)
    c=a+b
    a=b
    b=c
