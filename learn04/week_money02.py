"""
    作者：徐飞
    日期：2019
    版本：02
    功能：52存钱
"""
import math


def main():
    n_week = 52  # 周数
    week_per = 10  # 每周钱数
    per_week_add = 10  # 每周增加钱数
    # saving = 0  # 累计金额
    money_list = []
    for i in range(n_week):
        # saving += week_per
        money_list.append(week_per)
        saving = math.fsum(money_list)
        print('第{}周存钱{}元，账户累计{}'.format(i+1, week_per, saving))
        week_per += per_week_add
    # money_list.count()
    # money_list.index()
    # money_list.pop()
    # money_list.insert()
    # money_list.remove()
    # money_list.sort()
    # money_list.reverse()


if __name__ == '__main__':
    main()
