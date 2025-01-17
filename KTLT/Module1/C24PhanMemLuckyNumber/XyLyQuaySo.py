#from random import randrange

tien_may = 100
tien_nguoi =100
#if người dùng nhấn nút quay số thì
def xulyquayso(tien_may,tien_nguoi):
    if tien_nguoi>=30:
        tien_may+=30
        tien_nguoi-=30
        tien_thuong=0
        '''so1 = randrange(9)
        so2 = randrange(10)
        so3 = randrange(11)'''
        so1=input('so1 = ')
        so2 = input('so2=')
        so3=input('so3=')
        if so1 == '7':
            tien_thuong = 100 + 0.5*tien_may
            tien_may*=0.5
            tien_nguoi = tien_nguoi+tien_thuong
        if so2 == '7':
            tien_thuong = 30 + 0.5*tien_may
            tien_may *= 0.5
            tien_nguoi=tien_nguoi+tien_thuong
        if so3 == '7':
            tien_nguoi+=10
        print('tien may=', tien_may)
        print('tien thuong=', tien_thuong)
        print('tien nguoi=', tien_nguoi)