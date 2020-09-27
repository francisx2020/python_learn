"""
    作者：徐飞
    日期：2019
    版本：02
    功能：掷骰子
"""
import random
import matplotlib.pyplot as plt


def main():
    """
        主函数
    """
    times = 100
    dice_list = [0] * 11
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, dice_list))
    roll1_list = []
    roll2_list = []
    for i in range(times):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll1_list.append(dice1)
        roll2_list.append(dice2)
        for j in range(2, 13):
            if j == (dice1+dice2):
                roll_dict[j] += 1
    for i, n in roll_dict.items():
        print('点数{}的次数：{}，频率：{}'.format(i, n, n/times))
    x = range(1, times + 1)
    plt.scatter(x, roll1_list, alpha=0.5, c='g')
    plt.scatter(x, roll2_list, alpha=0.5, c='r')
    plt.show()


if __name__ == '__main__':
    main()
