"""
    作者：徐飞
    日期：2019
    版本：03
    功能：画图
"""
import turtle


def draw_angle(size):
    """
        递归函数
    """
    number = 1
    while number <= 5:
        turtle.forward(size)
        turtle.right(144)
        number += 1
    if size < 200:
        size += 20
        draw_angle(size)


def main():
    """
        主函数
    """
    turtle.speed(0)
    turtle.pensize(1.5)
    turtle.pencolor('red')
    size = 100
    draw_angle(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
