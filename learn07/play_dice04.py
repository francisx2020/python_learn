"""
    作者：徐飞
    日期：2019
    版本：02
    功能：掷骰子
"""
import random
import matplotlib.pyplot as plt
# 解决中文和符号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    times = 1000
    roll_list = []
    for i in range(times):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_list.append(roll1 + roll2)
    plt.hist(roll_list, bins=range(2, 14), density=1, edgecolor='k', linewidth=1)
    plt.title('掷骰子统计图')
    plt.xlabel('点数')
    plt.ylabel('概率密度')
    plt.show()


if __name__ == '__main__':
    main()
