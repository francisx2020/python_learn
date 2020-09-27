"""
    作者：徐飞
    日期：2019
    版本：01
    功能：基础代谢率
"""


def main():
    """
        主函数
    """
    start = input('是否开始运行程序（开始/Y，结束/N）:')
    while start == 'Y':
        gender = input('请输入性别：')
        weight = float(input('请输入体重（Kg）:'))
        height = float(input('请输入身高（cm）:'))
        age = int(input('请输入年龄（岁）:'))
        if gender == '男':
            val_bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            val_bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            val_bmr = -1
        if val_bmr != -1:
            print("此性别的BMR值：", val_bmr)
        else:
            print("暂不支持该性别！")
        start = input('是否开始运行程序（开始/Y，结束/N）:')
    print('程序已退出！')


if __name__ == '__main__':
    main()
