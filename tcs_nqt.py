
def fun_fib(a,b):
 c=a+b
 return (c)

def fun_prime(i,input_no):
	for num in range(i,input_no + 1):
	   # prime numbers are greater than 1
	       for i in range(2,num):
	           if (num % i) == 0:
	               break
	       else:
	           list_final.append(num)
	
list_final=[1,1]
input_no=int(input('enter the no location'))
if input_no%2!=0:
	for i in range(2,input_no):
			list_final.append(fun_fib(list_final[i-2],list_final[i-1]))
	loc=input_no/2
	print(list_final[int(loc)])  	

else:
 list_final=[]
 fun_prime(2,2*input_no)
 loc=input_no/2           
 print(list_final[int(loc-1)])  	


print(list_final)

