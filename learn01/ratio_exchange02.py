"""
    作者：徐飞
    时间：2019
    版本：02
    功能：汇率转换
"""

money = input("请输入带单位的货币金额：")
money_unite = money[-3:]
money_value = eval(money[:-3])
ratio = eval(input("请输入汇率："))
if money_unite == 'CNY':
    usd = money_value / ratio
    print("所得美元金额：", usd)
elif money_unite == 'USD':
    rmb = money_value * ratio
    print("所得人民币金额：", rmb)
else:
    print('暂不支持该种货币！')