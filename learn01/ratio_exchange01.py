"""
    作者：徐飞
    时间：2019
    版本：01
    功能：汇率转换
"""

RMB = eval(input("请输入人民币金额："))
ratio = eval(input("请输入汇率："))
usd = RMB / ratio
print("所得美元金额：", usd)
