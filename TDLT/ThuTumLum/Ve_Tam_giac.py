#Vẽ hình tam giác cân bằng *
def draw_isosceles_triangle(height):
    for i in range(height):
        #In khoảng trắng
        for j in range(height-i-1):
            print(' ', end='')
        #In dấu *
        for t in range(i+1):
            print('*', end=' ')
        print('')
draw_isosceles_triangle(5)

