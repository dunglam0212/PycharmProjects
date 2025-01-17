print("Lâm Thùy")
print("Dung ")

#Dùng end=' ' để nối 2 dòng print lại với nhau
print("Lâm Thùy",end=' ')
print("Dung")
print("Lâm Thùy ",end='')
print("Dung")

ho = "Lâm"
tenlot = "Thùy"
ten = "Dung"
#Xuất dữ liệu theo cách thông thường:
print(ho,tenlot,ten)
#Xuất dữ liệu bằng format
print(f"{ho} {tenlot} {ten}")

s= '{0} {1} {2}'.format(ho, tenlot, ten)
#Lưu ý: khi dùng format thì số lượng biến phải đúng bằng với số lượng khởi tạo

#Căn phải
print('-'*30) #Xuất dữ liệu lắp
print('{0:>2}' '{1:>11}'.format("STT", "Giá trị"))
print('{0:>2}' '{1:>11}'.format("1", "1000"))
print('{0:>2}' '{1:>11}'.format("2", "1000000"))
print('-'*30)



