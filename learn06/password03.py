"""
    作者：徐飞
    日期：2019
    版本：03
    功能：设置密码
"""


def is_number(password_str):
    """
        判断包含数字的函数
    """
    is_num = False
    for n in password_str:
        if n.isnumeric():
            is_num = True
            break
    return is_num


def is_alpha(password_str):
    """
        判断包含字母的函数
    """
    is_alf = False
    for n in password_str:
        if n.isalpha():
            is_alf = True
            break
    return is_alf


def main():
    """
        主函数
    """
    try_times = 5
    while try_times > 0:
        try_times -= 1
        password = input('请输入密码：')
        strength_level = 0
        # 判断密码长度
        if len(password) >= 8:
            strength_level += 1
        else:
            print('密码长度要求大于等于8！')
        # 判断是否包含数字
        if is_number(password):
            strength_level += 1
        else:
            print('密码要求包含数字！')
        # 判断是否包含字母
        if is_alpha(password):
            strength_level += 1
        else:
            print('密码要求包含字母！')
        f = open('password.txt', 'a')
        f.write('密码：{}，强度：{}\n'.format(password, strength_level))
        f.close()
        # 判断密码强度
        if strength_level == 3:
            print('恭喜！密码强度符合要求！')
            break
        else:
            print('密码不符合，请重新输入！')
        if try_times <= 0:
            break
    print('设置次数过多，无法再次设置！')


if __name__ == '__main__':
    main()
