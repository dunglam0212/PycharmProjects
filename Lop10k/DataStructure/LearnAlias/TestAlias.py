from DataStructure.QuanLySanPham.models.Product import Product

p1=Product('p1', 'Coca', 18,20)
p2=Product('p2', 'Pepsi', 15, 24)
#Đọc và nhìn, nghe: p1 bằng p2
#máy tính hoạt động chính xác như sau:
#Đối tượng p1 trỏ tới vùng nhớ mà đối tượng p2 đang quản lý
p1=p2
#Lúc này máy tính thực hiện 2 tình huống:
#Tình huống 1: ô nhớ b mà p2 đang quản lý bây giờ có thêm p1 quản lý --> Gọi là Alias
#tức là khi p1 đổi giá trị trên ô nhớ b thì p2 cũng tự động bị thay đổi, và ngược lại
p1.name ='Thuốc trị hôi nách'
print('Tên của p2 là:')
print(p2)

p2.name = 'Haha'
print('Tên của p1: ', p1.name)

p3=p1
p3.name = 'Thuốc trị phông bạt'
print('Tên của p1: ', p1.name)
print('Tên của p2: ', p2.name)

#Tình huống 2: Khi p1 trỏ qua ô nhớ của p2
#Tức là lúc này p1 đã bỏ mới nới cũ
#p1 không còn quản lý ô nhớ mà trước đó nó được hệ điều hành cấp phát
#lúc này máy tính sẽ: Nếu ô nhớ nào được cấp phát mà bây giờ không còn
#bất kỳ đối tượng nào tham gia quản lý --> tự động thu hồi bộ nhớ để tối ưu hệ thống
#sự thu hồi này được gọi là: gom rác tự động (garbage collection)
