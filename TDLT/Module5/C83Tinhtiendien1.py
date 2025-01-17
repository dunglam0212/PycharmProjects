def tinh_tien_dien1(k):
    if k<=50:
        return 1.549 * k
    else:
        m = 1.549 *50
        k -=50
        if k<=50:
            m+=1.6*k
            return m
        else:
            m+=1.6*50
            k-=50
            if k<=100:
                m+=1.858*k
                return m
            else:
                m += 1.858 * 100
                k-=100
                if k<=100:
                    m += 2.34 * k
                    return m
                else:
                    m += 2.34 * 100
                    k-=100
                    if k<=100:
                        m += 2.615 * k
                        return m
                    else:
                        m += 2.615 * 100
                        k-=100
                        if k>=1:
                            m += 2.701 * k
                            return m
                        else:
                            return m

print('Nhóm đối tượng khách hàng:')
print('1. Nhóm sử dụng điện cho sinh hoạt')
print('2. Nhóm sử dụng điện dùng công tơ thẻ trả trước')
flag = True
while flag:
    try:
        T = input('Bạn thuộc nhóm đối tượng nào? 1/2: ')
        if T == '1':
            K = float(input('Số Kwh bạn sử dụng trong tháng này là: '))
            print(f'Tiền điện trong tháng này của bạn là: {tinh_tien_dien1(K)}')
            flag = False
        elif T == '2':
            K = float(input('Số Kwh bạn sử dụng trong tháng này là: '))
            print(f'Tiền điện trong tháng này của bạn là: {K*2.271}')
            flag = False
        else:
            print('Vui lòng chọn 1 hoặc 2!')
    except:
        print('Giá trị bạn nhập không hợp lệ!')