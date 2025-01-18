class Product:
    def __init__(self, pro_id=None, name=None, unit_cal=None, quantity=None, price=None):
        self.pro_id = pro_id
        self.name = name
        self.unit_cal = unit_cal
        self.quanity = quantity
        self.price = price
    def __str__(self):
        return f"{self.pro_id}\t{self.name}\t{self.unit_cal}\t{self.quanity}\t{self.price}"
