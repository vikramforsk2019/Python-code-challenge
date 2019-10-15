#using BRUTE-FORCE APPROACH
#we can reduce loop iterarion by using length of pattern to increase the iteration
#time complexity 0 ( (n-m+1)*m ) .
 
#ROBIN-KalP algo by using hash value we can reduce complexity 0 (n+m) .

text="vikramsinghgurja"
match_text="ram"
loop_iter=len(text)-len(match_text)

for i in range(0,loop_iter+1):
	print(i)
	j=0
	while(j<len(match_text) and match_text[j]==text[i+j]):
		print(text[i+j],end='')
		j+=1
	if (j==len(match_text)):
		print('\nmatched length:',j)
		print('it is match all')
		break	
