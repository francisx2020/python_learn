"""
    作者：徐飞
    日期：2019
    版本：04
    功能：52存钱
"""
import math
from datetime import datetime


def saving_money(n_week, week_per, per_week_add):
    money_list = []
    saving_list = []
    for i in range(n_week):
        # saving += week_per
        money_list.append(week_per)
        saving = math.fsum(money_list)
        saving_list.append(saving)
        # print('第{}周存钱{}元，账户累计{}'.format(i+1, week_per, saving))
        week_per += per_week_add
    return saving_list
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
    str_day_num = input('请输入要查看日期(yy/mm/dd)：')
    day_num = datetime.strptime(str_day_num, '%y/%m/%d')
    week_num = day_num.isocalendar()[1]
    saving_num = saving[week_num-1]
    print("第{}周存钱{}元。".format(week_num, saving_num))
0

if __name__ == '__main__':
    main()
