class Product:
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity


class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        product = Product(name, quantity)
        self.__products.append(product)

    def show_product(self):
        print('Product List:')
        for index, product in enumerate(self.__products):
            print(f'{index+1}. Product {product.get_name()} - {product.get_quantity()} units')


my_store = Store()
my_store.add_product("Laptop", 15)
my_store.add_product("Mouse", 50)
my_store.show_product()
