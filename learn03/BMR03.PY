"""
    作者：徐飞
    日期：2019
    版本：03
    功能：基础代谢率
"""


def main():
    """
        主函数
    """
    start = input ('是否开始运行程序（Y/N）:')
    while start == 'N':
        print('请输入以下信息，以空格键隔开！')
        str_inf = input('性别： 体重(kg): 身高(cm): 年龄:')
        str_val = str_inf.split(' ')
        gender = str_val[0]
        weight = float(str_val[1])
        height = float(str_val[2])
        age = int(str_val[3])
        if gender == '男':
            val_bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            val_bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            val_bmr = -1
        if val_bmr != -1:
            print("此性别的BMR值：{}".format(val_bmr))
        else:
            print("暂不支持该性别！")
        start = input('是否开始运行程序（开始/Y，结束/N）:')
    print('程序已退出！')


if __name__ == '__main__':
    main()
