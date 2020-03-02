
import json
list_final=[]
list_final2=[]
def toString(List): 
	return ''.join(List) 
def permute(a, l, r): 
	if l==r: 
		list_final.append(toString(a)) 
	else: 
		for i in range(l,r+1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l+1, r) 
			a[l], a[i] = a[i], a[l] # backtrack 

# Driver program to test the above function 
string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 

list_final.sort(reverse=True)
for i in list_final:
	list_final2.append('"{0}"'.format(i))
for i in list_final:
	print(i,end=",")



