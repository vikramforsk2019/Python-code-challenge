# Taking multiple input from user
sort_list=[]
while True:
    user_input = raw_input("Enter values >")
    if user_input!='':
    	sort_list.append(user_input	)
    if not user_input:
        break
print(sort_list)


def selection_search(sort_list):
	h=len(sort_list)
	for i in range(0,h-1):
		loc=i
		min=sort_list[i]
		for j in range((i+1),h):
			if(min>sort_list[j]):
				min=sort_list[j]
				loc=j 
#take it bcoz j is goto end,i need only min j location.
		temp=sort_list[i]
		sort_list[i]=min
		sort_list[loc]=temp
selection_search(sort_list)
print(sort_list)