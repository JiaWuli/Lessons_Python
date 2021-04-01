# continue
product_scores=[89,90,23,45,87,97,67]
print(len(product_scores))
for i in range(len(product_scores)):
	if product_scores[i]>=90:
		continue
	print("第{}个产品， 分数为{}，不合格".format(i,product_scores[i]))

