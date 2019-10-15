
def fun(input_str):
   upper,lower,dig,sp=0,0,0,0
   for i in range(len(input_str)):
   	if input_str[i]>='A' and input_str[i]<='Z':
   	  upper+=1
   	elif input_str[i]>='a' and input_str[i]<='z':
   		lower+=1
   	elif input_str[i]>='0' and input_str[i]<='9':
   		dig+=1
   	else :
   		sp+=1
   print('upper case letter:',upper)
   print('lower case letter:',lower)
   print('digits case letter:',dig)
   print('special case letter:',sp)
import numpy as np
input_str=input('enter a string>>')

fun(input_str)

