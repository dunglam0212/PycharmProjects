class Student:
    def __init__(self, id=None, name=None, dob=None, cls=None, dqt=None, dgk=None, dck=None, dtb=None, hl=None):
        self.id=id
        self.name=name
        self.dob=dob
        self.cls=cls
        self.dqt=dqt
        self.dgk=dgk
        self.dck=dck
        self.dtb=dtb
        self.hl=hl

    def __str__(self):
        info = f'{self.id}\t{self.name}\t{self.dob}\t{self.cls}\t{self.dqt}\t{self.dgk}\t{self.dck}\t{self.dtb}\t{self.hl}'
        return info

class ListStudent():
    def __init__(self):
        self.students = []

    def add_student(self,s):
        self.students.append(s)

    def print_students(self):
        for s in self.students:
            print(s)

def tinh_dtb(qt,gk,ck):
    return qt*0.25 + gk*0.25 + ck*0.5

def xep_loai(dtb):
    if dtb < 4.0:
        return 'Kém'
    elif dtb < 5.0:
        return 'Yếu'
    elif dtb < 7.0:
        return 'Trung bình'
    elif dtb < 8.0:
        return 'Khá'
    elif dtb < 9.0:
        return 'Giỏi'
    else:
        return 'Xuất sắc'


