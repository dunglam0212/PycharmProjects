from LearnPyQtDesign.S13LearnQPushButtonBasicWidgets.MainWindow import Ui_MainWindow

class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonCalculate.clicked.connect(self.processCalculate)
    def show(self):
        self.MainWindow.show()
    def processCalculate(self):
        w = float(self.lineEditWeight.text())
        h = float(self.lineEditHeight.text())
        h = h/100
        BMI = w/(h*h)
        BMI = round(BMI, 2)
        commemt = ''
        if BMI < 16:
            commemt = 'Severe Thinness'
            self.labelComment2.setStyleSheet('color: blue;')
        elif BMI < 17:
            comment = 'Moderate Thinness'
            self.labelComment2.setStyleSheet('color: blue;')
        elif BMI < 18.5:
            commemt = 'Mild Thinness'
            self.labelComment2.setStyleSheet('color: blue;')
        elif BMI < 25:
            comment = 'Normal'
            self.labelComment2.setStyleSheet('color: green;')
        elif BMI <30:
            comment = 'Overweight'
            self.labelComment2.setStyleSheet('color: red;')
        elif BMI < 35:
            comment = 'Obese Class I'
            self.labelComment2.setStyleSheet('color: red;')
        elif BMI < 40:
            comment = 'Obese Class II'
            self.labelComment2.setStyleSheet('color: red;')
        else:
            comment = 'Obese Class III'
            self.labelComment2.setStyleSheet('color: red;')
        self.labelBMI2.setText(str(BMI))
        self.labelBMI2.setStyleSheet("color: blue;")
        self.labelComment2.setText(comment)
