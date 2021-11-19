products=[]
while True:
	name = input('product:')
	if name =='q':
		break
	price = input('price:')
	#p=[]
	#p.append(name)
	#p.append(price)
	p = [name,price]
	products.append(p)
print(products)
print(products[0][0])