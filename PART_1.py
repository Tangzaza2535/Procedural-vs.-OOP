class OnlineShop:
    def __init__(self, name, url):
        self.__name = name
        self.__url = url
        self.__products = []

    def get_products(self):
        return self.__products

    def addingItemsToCart(self, customer, product, quantity):
        customer.add_to_cart(product, quantity)

    def checkOut(self, customer):
        psum = 0
        cart = customer.get_cart()
        for product, quantity in cart:
            psum += product.get_price() * quantity
        order = {
            "order_id": len(customer.get_past_orders()),
            "sum": psum,
            "order": cart.copy()
        }
        customer.add_order(order)
        customer.clear_cart()

    def orderTracking(self, customer, order_id):
        past_orders = customer.get_past_orders()
        if order_id < 0 or order_id >= len(past_orders):
            print("ไม่พบคำสั่งซื้อ")
            return

        order = past_orders[order_id]
        print(f"คำสั่งซื้อเลขที่: {order['order_id']}")
        print("รายการสินค้า:")
        for product, quantity in order["order"]:
            print(f"- {product.get_name()} x {quantity} = {product.get_price() * quantity:.2f} บาท")
        print(f"ราคารวมทั้งหมด: {order['sum']:.2f} บาท")


class Product:
    def __init__(self, name, description, price, online_shop):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__online_shop = online_shop
        self.__online_shop.get_products().append(self)

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_price(self):
        return self.__price

    def get_online_shop(self):
        return self.__online_shop


class Customer:
    def __init__(self, name, email, address):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__cart = []
        self.__past_orders = []

    def add_to_cart(self, product, quantity):
        self.__cart.append([product, quantity])

    def get_cart(self):
        return self.__cart

    def clear_cart(self):
        self.__cart = []

    def add_order(self, order):
        self.__past_orders.append(order)

    def get_past_orders(self):
        return self.__past_orders

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

my_Customer = Customer("Q", "wachirachoomsiri@gmail.com", "Rayong")
my_OnlineShop = OnlineShop("ECS Store", "https://ee-eng.su.ac.th")

my_Product1 = Product("Wireless Mouse", "A smooth and silent wireless mouse", 790, my_OnlineShop)
my_Product2 = Product("Mechanical Keyboard", "RGB mechanical keyboard with blue switches", 1990, my_OnlineShop)
my_Product3 = Product("USB-C Hub", "7-in-1 USB-C hub for laptops", 990, my_OnlineShop)
my_Product4 = Product("Monitor", "Full HD IPS monitor with HDMI and DisplayPort", 4990, my_OnlineShop)

my_OnlineShop.addingItemsToCart(my_Customer, my_Product1, 1)
my_OnlineShop.addingItemsToCart(my_Customer, my_Product2, 1)
my_OnlineShop.checkOut(my_Customer)

my_OnlineShop.addingItemsToCart(my_Customer, my_Product3, 2)
my_OnlineShop.addingItemsToCart(my_Customer, my_Product4, 2)
my_OnlineShop.checkOut(my_Customer)

my_OnlineShop.orderTracking(my_Customer, 0)
my_OnlineShop.orderTracking(my_Customer, 1)
