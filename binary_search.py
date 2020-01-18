
sort_list=[-1,3,5,8,11]
low=0
flag=0
high=len(sort_list)-1
print(high)
item=input('enter the search element>>')
while low<=high:
	mid=(low+high)/2
	#print(sort_list[mid])
	if sort_list[mid]==item:
		flag=1;break
	elif item>sort_list[mid]:
		low=mid+1
	else:
		high=mid-1
if flag==1:
	print('item found')
else:
	print('not found item')


#binarary search by using recursive function
def bin_search(low,high,arr,item):
	while low<=high:
		mid=(low+high)/2
		if arr[mid]==item:
			return item;break
		elif item>arr[mid]:
			low=mid+1
		else:
			high=mid-1
	return -1;
item=input('enter the searcht item>>')
arr=[2,4,6,11,15,19,25]
result=bin_search(0,len(arr)-1,arr,item)
if result !=-1: 
    print ("Element is present", result) 
else: 
    print ("Element is not present in array")

