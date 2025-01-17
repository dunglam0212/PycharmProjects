import array as arr
#Tạo 1 mảng arr_int để lưu các số nguyên:
arr_int = arr.array("i", [3,7,2,10,5])
#Duyệt toàn bộ danh dách
print(arr_int)
print("Xuất từng phần tử theo index: ")
for i in range(len(arr_int)):
    x=arr_int[i]
    print(x, end=" ")
print("\nXuất các giá trị có index theo cột: ")
print("INDEX\tVALUE")
for i in range(len(arr_int)):
    x=arr_int[i]
    print(f"{i}\t\t{x}")

#tính tổng mảng:
sum=0
for x in arr_int:
    sum+=x
print("Tổng mảng: ", sum)

#để thay dổi giá trị tại vị trí thứ i=3
arr_int[3] = 999
#để xoá giá trị 10 trong mảng:
#arr_int.remove(10)

#để xoá giá trị tại chỉ mục thứ 2:
arr_int.pop(2)

#xuất lại danh sách để xem:
for x in arr_int:
    print(x, end=" ")

#minh hoạ ứng dụng vòng for lồng nhau để sắp xếp mảng tăng dần:
for i in range(len(arr_int)):
    for j in range(i+1, len(arr_int)):
        if arr_int[i] > arr_int[j]:
            temp = arr_int[i]
            arr_int[i] = arr_int[j]
            arr_int[j] = temp
print("\nDanh sách sau khi sắp xếp tăng dần là: ")
for x in arr_int:
    print(x, end=" ")