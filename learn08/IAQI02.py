"""
    作者：徐飞
    日期：2019
    版本：02
    功能：处理JSON数据
"""
import json


def process_file(file_path):
    """
        读取json文件
    """
    f = open(file_path, mode='r', encoding='utf-8')
    pro_file = json.load(f)
    f.close()
    return pro_file


def main():
    """
        主函数
    """
    file_path = input("请输入文件名称：")
    city_list = process_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])
    top_5 = city_list[:5]
    f = open('top_5.json', 'w', encoding='utf-8')
    json.dump(top_5, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
