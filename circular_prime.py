all_prime=[]
num=input('enter the number>')
l=len(num)
num=int(num)
for i in range(l):
	rem=int(num%10)
	num2=rem*pow(10,l-1)+int(num/10)
	print(num2)
	all_prime.append(num2)
	num=num2
print(all_prime)


def fun(n):
	flag=1
	print(n)
	for i in range(2,int(n/2)):
		if(n%i==0):
			flag=0
			break
	if flag==0:
	   return 1
	   #print('not circular prime')			
	else:
		return 0
		#print('print prime')	
y=list(filter(fun,all_prime))
print(y)
