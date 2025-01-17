def BMI(h,w):
    BMI = w / (h * h)

def BMI_phanloai(bmi):
    if bmi > 40.0:
        return 'Béo phì cấp độ 3'
    elif bmi > 35.5:
        return 'Béo phì cấp độ 2'
    elif bmi > 30.0:
        return 'Béo phì cấp độ 1'
    elif bmi > 25.0:
        return 'Hơi béo'
    elif bmi > 18.5:
        return 'Bình thường'
    elif bmi >0:
        return 'Gầy'
    else:
        return 'Giá trị bạn nhập không hợp lệ'

def BMI_canhbao(bmi):
    if bmi > 40.0:
        return 'Nguy hiểm'
    elif bmi > 35.5:
        return 'Rất cao'
    elif bmi > 30.0:
        return 'Cao'
    elif bmi > 25.0:
        return 'Cao'
    elif bmi > 18.5:
        return 'Trung bình'
    elif bmi >0:
        return 'Thấp'
    else:
        return 'Giá trị bạn nhập không hợp lệ'

h = float(input('Nhập chiều cao: '))
w = float(input('Nhập cân nặng: '))