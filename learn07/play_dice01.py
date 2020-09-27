"""
    作者：徐飞
    日期：2019
    版本：01
    功能：掷骰子
"""
import random


def main():
    """
        主函数
    """
    times = 100000
    dice_list = [0] * 6
    for i in range(times):
        dice = random.randint(1, 6)
        for j in range(7):
            if j == dice:
                dice_list[j-1] += 1
    for i, n in enumerate(dice_list):
        print('点数{}的次数：{}，频率：{}'.format(i+1, n, n/times))


if __name__ == '__main__':
    main()
