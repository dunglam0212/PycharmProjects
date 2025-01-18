class ListProduct:
    def __init__(self):
        self.listproducts = []
        self.filter_price_list = []
    def add_product(self, p, target_list=None):
        if target_list is None:
            target_list = self.listproducts
        target_list.append(p)
    def print_list_products(self):
        for p in self.listproducts:
            print(p)
    def find_product_by_id(self, f_id):
        for p in self.listproducts:
            if p.pro_id == f_id:
                return p
    def find_product_by_name(self, f_name):
        for p in self.listproducts:
            if p.name == f_name:
                return p
    def remove_product_by_id(self,r_id):
        p = self.find_product_by_id(r_id)
        if p == None:
            return
        self.listproducts.remove(p)
        del p
        return True
    def remove_product_by_name(self, r_name):
        p = self.find_product_by_name(r_name)
        if p == None:
            return
        self.listproducts.remove(p)
        del p
        return True
    def order_by_price_asc(self):
        for i in range(len(self.listproducts)):
            for j in range(i+1, len(self.listproducts)):
                if self.listproducts[i].price > self.listproducts[j].price:
                    temp = self.listproducts[i]
                    self.listproducts[i] = self.listproducts[j]
                    self.listproducts[j] = temp
    def order_by_price_desc(self):
        for i in range(len(self.listproducts)):
            for j in range(i+1, len(self.listproducts)):
                if self.listproducts[i].price < self.listproducts[j].price:
                    temp = self.listproducts[i]
                    self.listproducts[i] = self.listproducts[j]
                    self.listproducts[j] = temp
    def filter_price(self, min_price, max_price):
        self.filter_price_list = []
        for p in self.listproducts:
            if p.price>=min_price and p.price<=max_price:
                self.add_product(p, self.filter_price_list)
        return self.filter_price_list