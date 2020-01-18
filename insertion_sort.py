sort_list=[]
while True:
	user_input=raw_input('enter the element>>')
	if user_input!='':
		sort_list.append(user_input)
	if not user_input:
		break

def insert_sort(sort_list):
	print(sort_list)
	for i in range(1,len(sort_list)):
		temp=sort_list[i]
		j=i-1
		while((j>=0)&(sort_list[j]>temp)):
			sort_list[j+1]=sort_list[j]
			j=j-1
		sort_list[j+1]=temp					
insert_sort(sort_list)
print(sort_list)