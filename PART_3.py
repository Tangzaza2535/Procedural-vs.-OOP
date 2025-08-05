product_list = []

def add_product(product_list):
    name = input("Enter Product Name: ")
    units = int(input("Enter Product units: "))
    product_list.append([name,units])

def show_product(product_list):
    print('Product List:')
    for index,item in enumerate(product_list):
        print(f'{index+1}. Product {item[0]} - {item[1]} units')

add_product(product_list)
add_product(product_list)
add_product(product_list)
show_product(product_list)
