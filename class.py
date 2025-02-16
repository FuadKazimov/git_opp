class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Məhsul: {self.name} - {self.price:.2f} AZN"


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def get_total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name} - {self.get_total_price():.2f} AZN"


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
    
    def add_item(self, product, quantity):
        self.items.append(OrderItem(product, quantity))
    
    def get_total(self):
        return sum(item.get_total_price() for item in self.items)
    
    def __str__(self):
        order_details = f"Sifariş: {self.customer_name}\n"
        order_details += "\n".join(str(item) for item in self.items)
        order_details += f"\nÜmumi: {self.get_total():.2f} AZN"
        return order_details

laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 19.99)
order = Order("John Doe")
order.add_item(laptop, 2)
order.add_item(mouse, 1)

print(order)