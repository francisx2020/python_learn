"""
    作者：徐飞
    日期：2019
    版本：02
    功能：画图
"""
import turtle


def draw_angle(size):
    number = 1
    while number <= 5:
        turtle.forward(size)
        turtle.right(144)
        number += 1


def main():
    turtle.speed(0)
    turtle.pensize(1.5)
    turtle.pencolor('red')
    size = 100
    while size < 200:
        draw_angle(size)
        size += 20
    turtle.exitonclick()


if __name__ == '__main__':
    main()
