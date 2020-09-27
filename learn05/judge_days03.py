"""
    作者：徐飞
    日期：2019
    版本：01
    功能：判断天数
"""
from datetime import datetime


def is_leap_year(year):
    is_leap = False
    if (year % 100 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap


def main():
    """
        主函数
    """
    input_day_str = int(input("请输入日期(yyyy-mm-dd):"))
    now = datetime.now(input_day_str)
    input_day = datetime.strftime(now, '%j')
    print(input_day)
    # year = input_day.year
    # month = input_day.month
    # day = input_day.day
    # month_day_30 = {4, 6, 9, 11}
    # month_day_31 = {1, 3, 5, 7, 8, 10, 12}
    # # month_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # days = 0
    # days += day
    # for i in range(1, month):
    #     if i in month_day_30:
    #         days += 30
    #     elif i in month_day_31:
    #         days += 31
    #     else:
    #         days += 28
    # if is_leap_year(year):
    #     days += 1
    #
    # print('这是{}的第{}天。'.format(year, days))


if __name__ == '__main__':
    main()
