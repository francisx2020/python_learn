"""
    作者：徐飞
    时间：2019
    版本：04
    功能：汇率转换
"""


def main():
    """
        主函数
    """
    ratio = eval(input('请输入汇率值：'))
    money = input("请输入带单位的货币金额：")
    money_unite = money[-3:]
    money_value = eval(money[:-3])
    if money_unite == 'CNY':
        exchange_rate = 1 / ratio
    elif money_unite == 'USD':
        exchange_rate = ratio
    else:
        exchange_rate = -1

    if exchange_rate != -1:
        # 调用函数
        out_currency = lambda x, y: x * y
        out_money = out_currency(money_value, exchange_rate)
        print(out_money)
    else:
        print('暂不支持该货币！')


if __name__ == '__main__':
    main()
