import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QWidget, QHBoxLayout, QPushButton
from pygments.token import STANDARD_TYPES


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt QMessageBox')
        self.setGeometry(100, 100, 300, 100)

        layout = QHBoxLayout()
        self.setLayout(layout)

        btn_question = QPushButton('Question')
        btn_question.clicked.connect(self.question)

        btn_info = QPushButton('Information')
        btn_info.clicked.connect(self.info)

        btn_warning = QPushButton('Warning')
        btn_warning.clicked.connect(self.warning)

        btn_critical = QPushButton('Critical')
        btn_critical.clicked.connect(self.critical)

        layout.addWidget(btn_question)
        layout.addWidget(btn_info)
        layout.addWidget(btn_warning)
        layout.addWidget(btn_critical)

        self.show()

    def info(self):
        QMessageBox.information(self, 'Information', 'Đây là thông tin quan trọng.')

    def warning(self):
        QMessageBox.warning(self, 'Warning', 'Đây là thông báo cảnh báo.')

    def critical(self):
        QMessageBox.critical(self, 'Critical', 'Đây là thông báo nghiêm trọng.')

    def question(self):
        answer = QMessageBox.question(self, 'Xác nhận', 'Bạn có muốn thoát không?',
                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if answer == QMessageBox.StandardButton.Yes:
            QMessageBox.information(self, 'Thông tin', 'Bạn đã chọn Yes. Chương trình sẽ kết thúc.',
                                    QMessageBox.StandardButton.Ok)
            self.close()
        else:
            QMessageBox.information(self, 'Thông tin', 'Bạn đã chọn No.',
                                    QMessageBox.StandardButton.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())