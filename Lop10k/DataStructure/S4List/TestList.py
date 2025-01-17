list_int = [1,2,3]
print(list_int)

list_int_2 = [i for i in range(10)]
print(list_int_2)

list_int_3 = [3]*5
print(list_int_3)

#Truy xuất phần tử trong list, ta dùng indexer:
print(list_int_2[3])

list_int_4 = [3,5,2,0,10,8]
#Truy xuất bằng cách duyệt từng đối tượng trong list:
print('Danh sách các phần tử trong list_int_4')
for item in list_int_4:
    print(item, end=' ')

#Truy xuất = cách duyt qua index, từ index ta suy ra đc đối tượng tại index:
print('Danh sách các phần tử theo index: ')
for i in range(len(list_int_4)):
    print('index thứ ',i,'có giá trị = ',list_int_4[i])
    #list_int_4[i] item at indexer (phần tử tại index thứ i)

#đôi khi ta muốn truy xuất (filter) dữ liệu nâng cao
#thay vì chỉ index, hoặc chỉ đối tượng tại index đó
#thì có lúc ta cần truy xuất tập các dữ lệu trong danh sách:
#---> filter
#Ta muốn lấy 2 dữ liệu đầu tiên trong list_int_4
print(list_int_4[:2])
#Ta muôốn lấy 2 phần tử cuối cùng:
print(list_int_4[:-2])
#Ta muốn lấy các pần tử ở giữa danh sách:
print(list_int_4[2:4])
#Ta muốn lấy tất cả các phần tử còn lại tính từ vị trí thứ x
#vd x=3
print(list_int_4[3:])

list_double_5=[2.0,3.5,4.7,0.9,10.3,8.2]
print('Danh sách toàn bộ của list double 5: ', list_double_5)
#hãy cập nhật giá trị tại index thứ 2, thay giá trị mới =113
list_double_5[2]=113
print('Danh sách mới sau khi cập nhật: ', list_double_5)
#hãy sắp xếp list_double_5
list_double_5.sort()
print('Danh sách mới sau khi sắp xếp: ', list_double_5)
#muôốn sắp xếp giam dần?
list_double_5.sort(reverse=True)
print('Danh sách mới sau khi sắp xếp giảm dần: ', list_double_5)

list_string_1=['Obama', 'Putin', 'Kim Jong Un']
print(f'Danh sách trong list 1: {list_string_1}')
# để thêm mói phần tử vào cuối danh sách:
list_string_1.append('Hồ Cẩm Đào')
print('Danh sách trong list sau khi thêm: ',list_string_1)
# để chèn một phần tử vào vị trí bất kỳ
list_string_1.insert(0,'Kim Dung')
print('Danh sách sau khi chèn: ',list_string_1)
#ta có thể chèn 1 nùi đối tượng vào danh sách gốc:
list_string_1.append(['Tây Độc', 'Đông Tà'])
print('Danh sách sau khi chèn 1 nùi: ', list_string_1)
#nếu mốn chèn nhiều phần tử nhưng là các phần tử rời rạc:
list_string_1.extend(['Trung Thần Thông', 'Nam Đế'])
print('Danh sách sau khi chèn 1 nùi: ', list_string_1)

#Dùng lệnh remove để xóa các phần tử khỏi danh sách:
list_string_1.remove('Hồ Cẩm Đào')
print('Danh sách sau khi xóa: ', list_string_1)
list_string_1.pop() # giống trong cơ chế stack gọi lệnh pop --> xóa theo stack
print('Danh sách sau khi gọi lệnh pop()', list_string_1)
list_string_1.pop(1) #Xóa phần tử theo index
print('Danh sách sau khi gọi lệnh pop(1)', list_string_1)
