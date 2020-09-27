"""
    作者：徐飞
    日期：2019
    版本：03
    功能：将JSON数据转化为csv
"""
import json
import csv


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
    lines = [list(city_list[0].keys())]
    # print(line)
    for city in city_list:
        lines.append(list(city.values()))
    f = open('beijing.csv', 'w', encoding='utf-8', newline='')
    write = csv.writer(f)
    for line in lines:
        write.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
