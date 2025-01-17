def processAdd(self):
    try:
        l = len(self.list_fraction)
        f1 = self.list_fraction[l - 2]
        f2 = self.list_fraction[l - 1]
        f = add_fractions(f1, f2)
        self.lineEditResult.setText(f"{output_fraction(f1)} + {output_fraction(f2)} = {output_fraction(f)}")
    except:
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Warning')
        msgBox.setText('Valid Error!')
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()


def processSubstract(self):
    try:
        l = len(self.list_fraction)
        f1 = self.list_fraction[l - 2]
        f2 = self.list_fraction[l - 1]
        f = subtract_fractions(f1, f2)
        self.lineEditResult.setText(f"{output_fraction(f1)} - {output_fraction(f2)} = {output_fraction(f)}")
    except:
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Warning')
        msgBox.setText('Valid Error!')
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()


def processMultiple(self):
    try:
        l = len(self.list_fraction)
        f1 = self.list_fraction[l - 2]
        f2 = self.list_fraction[l - 1]
        f = multiply_fractions(f1, f2)
        self.lineEditResult.setText(f"{output_fraction(f1)} * {output_fraction(f2)} = {output_fraction(f)}")
    except:
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Warning')
        msgBox.setText('Valid Error!')
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()


def processDivide(self):
    try:
        l = len(self.list_fraction)
        f1 = self.list_fraction[l - 2]
        f2 = self.list_fraction[l - 1]
        f = divide_fractions(f1, f2)
        self.lineEditResult.setText(f"{output_fraction(f1)} / {output_fraction(f2)} = {output_fraction(f)}")
    except:
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Warning')
        msgBox.setText('Valid Error!')
        msgBox.setIcon(QMessageBox.Icon.Warning)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()