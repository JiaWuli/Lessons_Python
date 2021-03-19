# hello_world_0319_2
a=int(input())
str1="Hello World"
if a==0:
	print(str1)
elif a>0:
	for i in range(0,len(str1),2):
		print(str1[i:i+2])
else:
	for s in str1:
		print(s)