"""
    作者：徐飞
    日期：2019
    版本：01
    功能：画图
"""
import turtle


def main():
    number = 1
    while number <= 5:
        turtle.forward(100)
        turtle.right(144)
        number += 1
    turtle.exitonclick()


if __name__ == '__main__':
    main()
