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
    input_day_str = input("请输入日期(yyyy-mm-dd):")
    input_day = datetime.strptime(input_day_str, '%Y-%m-%d')
    year = input_day.year
    month = input_day.month
    day = input_day.day
    month_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        month_days_list[1] = 29
    days = sum(month_days_list[:month - 1]) + day
    print('这是{}的第{}天。'.format(year, days))


if __name__ == '__main__':
    main()
