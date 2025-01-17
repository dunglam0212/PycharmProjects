class Product:
    def __init__(self, id = None, name = None, quantity = None, price = None):
        self.id = id #id chỉ là biến local còn self.id thì là thuộc tính của đối tượng
        self.name = name
        self.quantity = quantity
        self.price = price
    def __str__(self):
        info = f"{self.id}\t{self.name}\t{self.quantity}\t{self.price}"
        return info
