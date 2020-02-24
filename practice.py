#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:22:34 2020
@author: jagveer

"""
list_ok=[]
input_name=input('enter the sentence>>')

list_ok=input_name.split()

#'ramma'.join(input_name)
print(list_ok[:-1])




print(list_ok[-1],end="")
for i in list_ok:
    print(i,end=" ")
print(list_ok[-2])



#reverse of a string in python
def reverse(s): 
  str = "" 
  for i in s:
    print(i) 
    str = i + str
  return str

ok=reverse("my name is ram")
print(ok)


# A stack based function to reverse a string 
def createStack():
    stack=[]
    return stack
def push(stack,item):
    stack.append(item)
    return stack
def pop(stack):
    return stack.pop()
    
def reverse(string): 
    n = len(string) 
    print(n)
    # Create a empty stack 
    stack = createStack() 
   
    # Push all characters of string to stack 
    for i in range(0,n,1): 
        push(stack,string[i]) 
   
    # Making the string empty since all 
    # characters are saved in stack     
    string="" 
   
    # Pop all characters of string and put 
    # them back to string 
    for i in range(0,n,1): 
        string+=pop(stack) 
           
    return string 

ok=reverse("my name is ram")
print(ok)




def reverse(string): 
    string = "".join(reversed(string)) 
    print(string)
    return string 

ok=reverse("my name is ram")
print(ok)
