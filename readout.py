import os 
product=[]
if os.path.isfile('products.csv'):
	print('Yes')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'product,price' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
	print(product)
else:
	print('No')
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
	product.append([name,price])
print(product)
#record
for p in product:
	print(p[0],'price is :',p[1])
#write in
with open('products.csv','w', encoding = 'utf-8') as f:
	f.write('product,price\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) + '\n')



