#readout
product=[]
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'product,price' in line:
			continue
		name, price = line.strip().split(',')
		product.append([name, price])
print(product)
#input
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
#record
for p in products:
	print(p[0],'price is :',p[1])
#write in
with open('products.csv','w', encoding = 'utf-8') as f:
	f.write('product,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')



