def BMI(h,w):
    return w / (h * h)

def BMI_phanloai(bmi):
    match bmi:
        case bmi if bmi > 40.0:
            return 'Béo phì cấp độ 3'
        case bmi if bmi > 35.5:
            return 'Béo phì cấp độ 2'
        case bmi if bmi > 30.0:
            return 'Béo phì cấp độ 1'
        case bmi if bmi > 25.0:
            return 'Hơi béo'
        case bmi if bmi > 18.5:
            return 'Bình thường'
        case bmi if bmi > 0:
            return 'Gầy'
        case _:
            return 'Giá trị bạn nhập không hợp lệ'

def BMI_canhbao(bmi):
    match bmi:
        case bmi if bmi > 40.0:
            return 'Nguy hiểm'
        case bmi if bmi > 35.5:
            return 'Rất cao'
        case bmi if bmi > 30.0:
            return 'Cao'
        case bmi if bmi > 25.0:
            return 'Cao'
        case bmi if bmi > 18.5:
            return 'Trung bình'
        case bmi if bmi > 0:
            return 'Thấp'
        case _:
            return 'Giá trị bạn nhập không hợp lệ'

flag = True
while flag:
    try:
        h = float(input('Nhập chiều cao: '))
        if h>0:
            w = float(input('Nhập cân nặng: '))
            if w>0:
                BMI = BMI(h,w)
                print(f'BMI của bạn là {BMI}')
                print(f'Phân loại bạn là {BMI_phanloai(BMI)}')
                print(f'Nguy cơ bệnh của bạn là {BMI_canhbao(BMI)}')
                flag = False
            else:
                print('Vui lòng nhập cân nặng là một giá trị dương hợp lệ!')
        else:
            print('Vui lòng nhập chiều cao là một giá trị dương hợp lệ!')
    except:
        print('Giá trị bạn nhập không hợp lệ!')