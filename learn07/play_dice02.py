"""
    作者：徐飞
    日期：2019
    版本：02
    功能：掷骰子
"""
import random


def main():
    """
        主函数
    """
    times = 10000
    dice_list = [0] * 11
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, dice_list))
    for i in range(times):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        for j in range(2, 13):
            if j == (dice1+dice2):
                roll_dict[j] += 1
    for i, n in roll_dict.items():
        print('点数{}的次数：{}，频率：{}'.format(i, n, n/times))


if __name__ == '__main__':
    main()
