
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Input:
The first line contains 'T' denoting the number of testcases. Then follows description of testcases. The next T lines contains a single integer N denoting the value of N.


Output:
Output the sum of all its digit until the result has only one digit.


Constraints:
1<=T<=30
1<=n<=10^9


Example:
Input :
2
1
98


Output :
1
8

Explanation:  For example, if we conisder 98, we get 9+8  = 17 after first addition. Then we get 1+7 = 8.  We stop at this point because we are left with one digit.
** For More Input/Output Examples Use 'Expected Output' option **
"""
def sep_sum(num):
 sum1=0
 num=int(num)
 while(num>0):
 	rem=int(num%10)
 	sum1=sum1+rem
 	num=int(num/10)
 return sum1

num=input('enter the integer>>>')
sum2=0
if(len(num)>1):
	sum2=sep_sum(num)
	print(sum2)
	while(len(str(sum2))>1):
		sum2=sep_sum(sum2)
		print(sum2)
else:
	sum2=num
print('the sum of all its digit until the result has only one digit',sum2)	



