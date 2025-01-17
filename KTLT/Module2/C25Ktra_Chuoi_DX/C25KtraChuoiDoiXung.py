# Sinh viên sử dụng vòng lặp while vô tận, cho phép Nhập vào một Chuỗi
# ➔Xuất Chuỗi này có phải đối xứng hay không? Hỏi người sử dụng có tiếp tục phần mềm.
# Nếu tiếp tục thì nhập Chuỗi mới, còn không thì thoát và thông báo cảm ơn.

def kt_chuoi_dx(chuoi):
    cd = len(chuoi)
    giua = cd//2
    dem=0
    for i in range(giua):
        if chuoi[i] == chuoi[cd-1]:
            dem+=1
            cd-=1
    if dem == giua:
        return True

#Cách của Thầy - ngắn gọn:
# def CheckDoiXung(s):
#  flag=True
#  for i in range(len(s)):
#      if s[i]!=s[len(s)-i-1]:
#          flag=False
#          break
#  return flag

def question():
    flag = True
    while flag:
        q = input("Bạn có muốn tiếp tục chương trình không? Y/N: ")
        if q.lower() == "y":
            return
        elif q.lower() == "n":
            print("Cảm ơn bạn vì đã sử dụng chương trình")
            print("Hẹn gặp lại bạn vào lần sau")
            return True
        else:
            print("Xin vui lòng chọn Y hoặc N!")

def main():
    flag = True
    while flag:
        chuoi = input("Hãy nhập vào một chuỗi tuỳ ý: ")
        rs = kt_chuoi_dx(chuoi)
        if rs == True:
            print(f"'{chuoi}' là một chuỗi đối xứng!")
        else:
            print(f"'{chuoi}' không phải là một chuỗi đối xứng!")
        q = question()
        if q == True:
            flag = False



