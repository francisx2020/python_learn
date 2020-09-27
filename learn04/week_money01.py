"""
    作者：徐飞
    日期：2019
    版本：01
    功能：52存钱
"""


def main():
    n_week = 1
    week_per = 10
    per_week_add = 10
    saving = 0
    while n_week <= 52:
        saving += week_per
        print('第{}周存钱{}元，账户累计{}'.format(n_week, week_per, saving))
        week_per += per_week_add
        n_week += 1


if __name__ == '__main__':
    main()
