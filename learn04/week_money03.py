"""
    作者：徐飞
    日期：2019
    版本：03
    功能：52存钱
"""
import math


def saving_money(n_week, week_per, per_week_add):
    money_list = []
    for i in range(n_week):
        # saving += week_per
        money_list.append(week_per)
        saving = math.fsum(money_list)
        print('第{}周存钱{}元，账户累计{}'.format(i+1, week_per, saving))
        week_per += per_week_add
    return saving
    # money_list.count()
    # money_list.index()
    # money_list.pop()
    # money_list.insert()
    # money_list.remove()
    # money_list.sort()
    # money_list.reverse()


def main():
    n_week = int(input('请输入存钱周数：'))                     # 周数
    week_per = float(input('请输入每周存钱数：'))               # 每周钱数
    per_week_add = float(input('请输入每周增加钱数：'))         # 每周增加钱数
    # saving = 0                                              # 累计金额
    saving = saving_money(n_week, week_per, per_week_add)
    print("存钱总额：", saving)


if __name__ == '__main__':
    main()
