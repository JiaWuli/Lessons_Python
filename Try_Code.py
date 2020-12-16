try:
	n = eval(input("输入一个数字：")) 
	# evaluste(求值),故将input的输入变成数字
	print("输入数字的3次方为：",n**3)
except:
	print("输入错误，请输入一个数字")