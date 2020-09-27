"""
    作者：徐飞
    日期：2019
    版本：04
    功能：画图
"""
import turtle


def draw_tree(branch):
    if branch > 5:
        # 绘制右侧树枝
        turtle.forward(branch)
        turtle.right(20)
        draw_tree(branch - 15)
        # 绘制左侧树枝
        turtle.left(40)
        draw_tree(branch - 15)
        # 返回原点
        turtle.right(20)
        turtle.backward(branch)


def main():
    """
        主函数
    """
    turtle.speed(1)
    branch = 80
    turtle.left(90)
    draw_tree(branch)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
