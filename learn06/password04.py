"""
    作者：徐飞
    日期：2019
    版本：04
    功能：设置密码
"""


class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def process_password(self):

        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码长度要求大于等于8！')
        # 判断是否包含数字
        if self.is_number():
            self.strength_level += 1
        else:
            print('密码要求包含数字！')
        # 判断是否包含字母
        if self.is_alpha():
            self.strength_level += 1
        else:
            print('密码要求包含字母！')

    def is_number(self):
        """
            判断包含数字的函数
        """
        is_num = False
        for n in self.password:
            if n.isnumeric():
                is_num = True
                break
        return is_num

    def is_alpha(self):
        """
            判断包含字母的函数
        """
        is_alf = False
        for n in self.password:
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

        password = input('请输入密码：')
        # 实例化工具类对象
        pass_tool = PasswordTool(password)
        pass_tool.process_password()
        f = open('password.txt', 'a')
        f.write('密码：{}，强度：{}\n'.format(password, pass_tool.strength_level))
        f.close()
        # 判断密码强度
        if pass_tool.strength_level == 3:
            print('恭喜！密码强度符合要求！')
            break
        else:
            print('密码不符合，请重新输入！')
            try_times -= 1
    if try_times <= 0:
        print('设置次数过多，无法再次设置！')


if __name__ == '__main__':
    main()
