class Product:
    def __init__(self, id=None, name=None, quantity=None, price=None):
        #Nên =None vì khi kh cung cấp thtin thì mặc định là None (vì kh phải lúc nào cũng có thể cung cấp đầy đủ thtin cho đối tượng)
        #Constructor: 1 hàm đặc biệt tự động khởi tạo đối tượng khi đối tượng đc tạo ra trong bộ nhớ
        #self.: thuộc tính, còn trong init thì chỉ là tham số hình thức thôi
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
    def __str__(self): #Trả về 1 giá trị chuỗi mà mình mong muốn, chứ nó kh xuất ra màn hình
        info=f'{self.id}\t{self.name}\t{self.quantity}\t{self.price}'
        return info