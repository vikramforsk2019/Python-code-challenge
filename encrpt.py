import string
s=input('enter a string>>')
s=list(s.lower())
print(s)
for i in range(len(s)):
    if i%2==0:
       s[i]='!'*(string.ascii_lowercase.index(s[i])+1)
    else:
        s[i]='@'*(string.ascii_lowercase.index(s[i])+1)
n=''        
p=n.join(s)        
print(''.join(s))   

"""
Examples:

Input: string = "Ab" 
Output: !@@
Explanation:
Position of 'A' in alphabetical order is 1
and in String is odd position 
so encrypted message will have 1 '!'

Position of 'b' in alphabetical order is 2
and in String is even position 
so encrypted message will have 2 '@'

Therefore, the output "!@@"

Input: string = "CDE"
Output: !!!@@@@!!!!!


##help
m=input('enter a string>>')
p=m
m=list(m.lower())
for i in range(len(m)):
   mul=string.ascii_lowercase.index(m[i])+1 #position
   print(mul)
   print(p[i]*mul);
""" 