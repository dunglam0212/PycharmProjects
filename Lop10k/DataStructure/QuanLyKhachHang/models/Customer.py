class Customer:
    def __init__(self,id=None, name=None, email=None,phone=None,age=None,tc=None):
        #Trong ngoặc () ở trên là những tham số hình thức
        #Do đó để dùng lại thì ta mới khai báo ở dưới
        self.id=id
        self.name=name
        self.email=email
        self.phone=phone
        self.age=age
        self.tc=tc

    def __str__(self):
        #Khi xuất ra thì trả về chuõi
        msg=f'{self.id}\t{self.name}\t{self.email}\t{self.phone}\t{self.age}\t{self.tc.value}'
        return msg

    def get_details(self):
        msg = (f'Id = {self.id}\n'
               f'Name = {self.name}\n'
               f'Email = {self.email}\n'
               f'Phone = {self.phone}\n'
               f'Age = {self.age}\n'
               f'Type Customer = {self.tc.value}')
        return msg