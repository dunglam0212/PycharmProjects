from DataStructure.QuanLySanPham.models.Product import Product


class ListProduct:
    def __init__(self):
        self.products = []
    def add_product(self,p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)
    def filter_products(self,min_price,max_price):
        products_filter = []
        for product in self.products:
            if product.price >= min_price and product.price <= max_price:
                products_filter.append(product)
        return products_filter
    def filter_list_product(self,min_price,max_price):
        lp = ListProduct()
        for product in self.products:
            if product.price >= min_price and product.price <= max_price:
                lp.add_product(product)
        return lp
    def find_product_by_id(self, id):
        size = len(self.products)
        i=0
        while i<size:
            p=self.products[i]
            if p.id==id:
                return p
            i+=1
        return None
    def remove_product_by_id(self, id):
        p = self.find_product_by_id(id)
        if p==None:
            return False #kh tìm thấy, xóa thất bại
        else:
            self.products.remove(p)
            return True #Tìm thấy, xóa thành công
    def sort_product_price_asc(self):
        for i in range(len(self.products)):
            for j in range(i+1,len(self.products)):
                pi = self.products[i]
                pj = self.products[j]
                if pi.price > pj.price:
                    self.products[j] = pi
                    self.products[i] = pj
    def sort_product_price_dsc(self):
        for i in range(len(self.products)):
            for j in range(i+1, len(self.products)):
                pi = self.products[i]
                pj = self.products[j]
                if pi.price < pj.price:
                    self.products[i] = pj
                    self.products[j] = pi
                elif pi.price == pj.price:
                    if pi.quantity > pj.quantity:
                        self.products[i] = pj
                        self.products[j] = pi
    def queryData(self):
        database = ListProduct()
        database.add_product(Product('P1', 'Áo ấm', 3, 150))
        database.add_product(Product('P2', 'Áo gió', 5, 200))
        database.add_product(Product('P3', 'Áo len', 10, 80))
        p = Product('P4', 'Áo 3 lỗ', 8, 10)
        database.add_product(p)
        database.add_product(Product('P5', 'Áo thun', 2, 70))
        return database
    def count(self):
        return len(self.products)
    def get_product_by_index(self, index):
        return self.products[index]



