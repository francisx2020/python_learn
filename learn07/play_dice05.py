"""
    作者：徐飞
    日期：2019
    版本：02
    功能：掷骰子
"""
import numpy as np
import matplotlib.pyplot as plt
# 解决中文和符号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    times = 1000
    roll1 = np.random.randint(1, 7, size=times)
    roll2 = np.random.randint(1, 7, size=times)
    roll_list = np.array(roll1 + roll2)
    hist, bins = np.histogram(roll_list, bins=range(2, 14))
    print(hist)
    print(bins)
    x_ticks = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    x_pos = np.arange(2, 13) + 0.5
    plt.hist(roll_list, bins=range(2, 14), density=1, edgecolor='k', linewidth=1, rwidth=0.8)
    plt.xticks(x_pos, x_ticks)
    plt.title('掷骰子统计图')
    plt.xlabel('点数')
    plt.ylabel('概率密度')
    plt.show()


if __name__ == '__main__':
    main()
