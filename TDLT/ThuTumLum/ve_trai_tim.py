import turtle

import turtle
import time
import random


def draw_heart(color):
    pen = turtle.Turtle()
    pen.color(color)
    pen.begin_fill()

    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)

    pen.end_fill()
    pen.hideturtle()


def twinkling_heart():
    screen = turtle.Screen()
    screen.bgcolor("white")

    colors = ['red', 'pink', 'yellow', 'purple', 'blue']  # Các màu sắc khác nhau cho hiệu ứng lấp lánh

    while True:
        screen.clear()
        color = random.choice(colors)  # Chọn một màu ngẫu nhiên
        draw_heart(color)  # Vẽ trái tim với màu sắc ngẫu nhiên
        time.sleep(0.5)  # Dừng lại 0.5 giây trước khi thay đổi màu
        screen.update()


screen = turtle.Screen()
screen.tracer(0)  # Tắt việc cập nhật màn hình tự động
twinkling_heart()
