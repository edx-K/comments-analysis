products=[]
while True:
	name = input('product:')
	if name =='q':
		break
	price = input('price:')
	price = int(price)
	#p=[]
	#p.append(name)
	#p.append(price)
	#p = [name,price]
	products.append([name,price])
print(products)
print(products[0][0])
for p in products:
	print(p[0],'price is :',p[1])
with open('products.csv','w',encoding = 'utf-8') as f:
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
