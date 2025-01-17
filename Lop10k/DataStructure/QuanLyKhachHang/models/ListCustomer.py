from DataStructure.QuanLyKhachHang.models.TypePhone import TypePhone


class ListCustomer:
    def __init__(self):
        self.customers=[]
    def add_customer(self,c):
        self.customers.append(c)
    def update_customer(self, index, c):
        self.customers[index] = c
    def print_customers(self):
        for c in self.customers:
            print(c) #tự động gọi hàm __str__
    def filter_type_customers(self,tc):
        filters = []
        for c in self.customers:
            if c.tc==tc:
                filters.append(c)
        return filters #Cau truc du lieu List
    def filter_age_customers(self,min_age,max_age):
        filter = ListCustomer()
        for c in self.customers:
            if c.age >= min_age and c.age <= max_age:
                filter.add_customer(c)
        return filter #Trả về 1 đối tượng
    def filter_type_phone_customers(self,tp):
        """
        đây là hàm lọc khách hàng theo nhà mạng
        :param tp: là nhà mạng viettel, mobi, vina
        :return:
        """
        filter=ListCustomer()
        match(tp):
            case TypePhone.VIETTEL:
                filter = self.filter_viettel_customer()
                return filter
            case TypePhone.MOBI:
                filter = self.filter_mobi_customers()
                return filter
            case TypePhone.VINA:
                filter = self.filter_vina_customers()
                return filter
            case _:
                return filter

    def filter_viettel_customer(self):
        filter1 = ListCustomer()
        for c in self.customers:
            if c.phone.startswith('098') or c.phone.startswith('097'):
                filter1.add_customer(c)
        return filter1

    def filter_mobi_customers(self):
        filter1 = ListCustomer()
        for c in self.customers:
            if c.phone.startswith('090'):
                filter1.add_customer(c)
        return filter1

    def filter_vina_customers(self):
        filter1 = ListCustomer()
        for c in self.customers:
            if c.phone.startswith('093'):
                filter1.add_customer(c)
        return filter1

    def sort_customer_age_dsc(self):
        for i in range(len(self.customers)):
            for j in range(i+1, len(self.customers)):
                ci = self.customers[i]
                cj = self.customers[j]
                if ci.age < cj.age:
                    self.customers[i] = cj
                    self.customers[j] = ci

    # primitive data - kiểu dữ liệu cơ sở --> Tìm thấy: -1, Tìm không thấy thì trả về vị trí đầu tiên
    # #object data --> Tìm thấy: trả về giá trị tìm, Tìm kh thấy: None
    def find_1_id(self, id):
        for c in self.customers:
            if c.id == id:
                return c
        return None

    def remove_customer_by_index(self, index):
        if index<0 or index>= len(self.customers):
            return False
        self.customers.pop(index)

    def remove_customer_by_id(self, id):
        c_remove = self.find_1_id(id)
        if c_remove == None:
            return False
        self.customers.remove(c_remove)
        return True
