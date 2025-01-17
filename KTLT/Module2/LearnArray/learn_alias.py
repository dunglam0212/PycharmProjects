list1 = [1,2,3]
list2 = [4,5,6]

print("list[1] = ", list1[1])
#lệnh dưới đây gây ra 2 tình huống:
#alias + garbage collection
list1=list2
#đổi giá trị của list2 --> làm list1 bị đổi
#vì list1 và list2 là alias đang cùng quản lý 1 o nhớ
list2[1] = 113
#do đó list1[1] sẽ bị đổi theo list2[1]
print("list1[1] = ", list1[1])

#Làm bài 36,37