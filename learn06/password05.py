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


class FileTool:
    """
        文件工具类
    """
    def __init__(self, file_path):
        self.file_path = file_path

    # 写文件
    def write_file(self, lines):
        f = open(self.file_path, 'a')
        f.write(lines)
        f.close()

    # 读文件
    def read_file(self):
        f = open(self.file_path, 'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        主函数
    """
    try_times = 5
    file_path = 'password.txt'
    # 实例化文件类对象
    file_tool = FileTool(file_path)
    while try_times > 0:

        password = input('请输入密码：')
        # 实例化工具类对象
        pass_tool = PasswordTool(password)
        pass_tool.process_password()
        # 写文件
        line = '密码：{}，强度：{}\n'.format(password, pass_tool.strength_level)
        file_tool.write_file(line)

        # 判断密码强度
        if pass_tool.strength_level == 3:
            print('恭喜！密码强度符合要求！')
            break
        else:
            print('密码不符合，请重新输入！')
            try_times -= 1
    if try_times <= 0:
        print('设置次数过多，无法再次设置！')
    # 读文件
    lines = file_tool.read_file()
    print(lines)


if __name__ == '__main__':
    main()
