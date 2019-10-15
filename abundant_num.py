input_num=int(input('enter the divisors number>'))
divisor_sum=0
for i in range(1,int(input_num/2)+1) :
		if(input_num%i==0) :
			divisor_sum+=i
if divisor_sum>input_num:			
 print('it is abundant number')
else:
 print('it is not a abundant number')			
