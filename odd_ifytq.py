def odder(eve_list,odd_list,last2):
   if len(eve_list)>=len(odd_list):
      for i in range(len(eve_list)):
         last2.append(eve_list[i])
         if(i<len(odd_list)):
            last2.append(odd_list[i])
      print(last2)
   else:
        for i in range(len(odd_list)):
         if(i<len(eve_list)):
            last2.append(eve_list[i])
         last2.append(odd_list[i])
        print(last2)


def fun(input_str):
   upper,lower,dig,sp=0,0,0,0
   for i in range(len(input_str)):
      if input_str[i]>='A' and input_str[i]<='Z':
        upper+=1
      elif input_str[i]>='a' and input_str[i]<='z':
         lower+=1
      elif input_str[i]>='0' and input_str[i]<='9':
         dig+=1
         last.append(int(input_str[i]))
      else :
         sp+=1
   return(sp)
   print('upper case letter:',upper)
   print('lower case letter:',lower)
   print('digits case letter:',dig)
   print('special case letter:',sp)

import numpy as np
odd_list=[]
eve_list=[]
last=[]
last2=[]

input_str=input('enter a string>>')
sp = int (fun(input_str))

for i in last:
   if i%2!=0:
      odd_list.append(i)
   else:
      eve_list.append(i)
print(sp)
if sp%2==0:
 odder(eve_list,odd_list,last2)
else:
 odder(odd_list,eve_list,last2)


