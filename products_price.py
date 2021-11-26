import os
#read in original file
def read_file(filename):
	products=[]
	with open (filename,'r',encoding = 'utf-8') as f:
		for line in f:
			if 'products,price' in line:
				continue
			name, price =line.strip().split(',')
			products.append([name, price])
	return products

#user input
def user_input(products):
	while True:
		name = input('please put in product name:')
		if name =='q':
			break
		price = input('please input product price:')
		price = int(price)
		products.append([name,price])
	print(products)
	return products

#print all the product record
def print_products(products):
	for p in products:
		print(p[0], 'price is :', p[1])

#write in file:
def write_in(filename, products):
	with open(filename,'w',encoding = 'utf-8')as f:
		f.write('product,price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')


#main function
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):#check if it's there
		print('find it')
		products = read_file(filename)
	else:
		print('cant find file')
	products = user_input(products)
	print_products(products)
	write_in(filename, products)

main()
