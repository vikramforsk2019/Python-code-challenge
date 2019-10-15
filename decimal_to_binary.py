final_list=[]
print("1:decimal_to_binary\n"
	"2:binary to decimal\n"
	"3:decimal to hexadecmal\n")
choice=int(input('enter the one choice>'))

def decimal_to_binary():
	input_num=int(input('enter the decimal number>'))
	while input_num>0:
		rem=input_num%2
		input_num=int(input_num/2)
		final_list.append(rem)	
	return (final_list[::-1])	

def binary_to_decimal():
	base=1
	sum_er=0
	input_num=int(input('enter the binary number>'))
	while input_num>0:
		rem=input_num%10
		sum_er+=base*rem
		base*=2
		input_num=int(input_num/10)
	return sum_er

def decimal_to_hexadecimal():
	hexa_list=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
	input_num=int(input('enter the decimal number>'))
	while input_num>0:
		rem=input_num%16
		input_num=int(input_num/16)
		#print(hexa_list[rem])
		final_list.append((hexa_list[rem]))
	return final_list[::-1]

switcher={
	1:decimal_to_binary,
	2:binary_to_decimal,
	3:decimal_to_hexadecimal
         }
fun=switcher.get(choice,'nothing')
print(fun())