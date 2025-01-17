from random import randrange

def doanso():
    x = randrange(1, 101)
    i=0
    while i<7:
        n = int(input('Vui lòng đoán 1 số trong khoảng từ 1 đến 100: '))
        if n!=x:
            if n>x:
                print(f'{n} lớn hơn số của máy')
                i+=1
                print(f'Bạn còn {7-i} lần đoán!')
            else:
                print(f'{n} nhỏ hơn số của máy')
                i+=1
                print(f'Bạn còn {7-i} lần đoán!')
        else:
            return f'Xin chúc mừng! Bạn đã đoán đúng! {n} là số mà máy chọn!'
    else:
        return f'GAME OVER! Bạn đã hết lượt đoán! Số mà máy chọn là {x}'

def main():
    print(doanso())
    flag = True
    while flag:
        q = input('Bạn có muốn tiếp tục chơi không? Y/N: ')
        if q.lower() == 'y':
            print(doanso())
        elif q.lower() == 'n':
            return 'Xin cảm ơn! Hẹn gặp lại bạn vào lần sau!'
        else:
            print('Xin vui lòng chọn Y hoặc N!')
main()




