"""
    作者：徐飞
    时间：2019
    版本：03
    功能：汇率转换
"""
start = input("是否运行程序(不运行输入:否，运行输入:是)：")
i = 0
while start == "是":
    i += 1
    print('循环次数：', i)
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
    start = input("是否运行程序(不运行输入Q)：")

print("程序已退出！")
