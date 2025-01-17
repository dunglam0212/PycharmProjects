from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie
from PyQt6.QtWidgets import QLabel

label = QLabel('Hello, I am QLabel widget')
font = label.font()
font.setPointSize(30)
label.setFont(font)
label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

#Hiển thị dữ liệu hình ảnh định dạng .bmp, .jpg, .jpeg, .png, .svg cho QLabel:
label1 = QLabel()
pixmap = QPixmap('myavatar.png')
label1.setPixmap(pixmap)

#Hiển thị dữ liệu hình ảnh định dạng .gif cho QLabel
movie = QMovie('mygif.gif')
label2 = QLabel()
label2.setMovie(movie)
movie.start()
