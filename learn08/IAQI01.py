"""
    作者：徐飞
    日期：2019
    版本：01
    功能：计算IAQI
"""


def cal_pm_2_5(pm_2_5_val):
    """
        计算pm2.5的IAQI
    """
    pass


def cal_co(co_val):
    """
        计算co的IAQI
    """
    pass


def cal_air_quality(put_list):
    """
        计算IAQI的值
    """
    pm_2_5_val = put_list[0]
    co_val = put_list[1]

    pm_air_quality = cal_pm_2_5(pm_2_5_val)
    co_air_quality = cal_co(co_val)
    air_quality = [pm_air_quality, co_air_quality]
    air_val = max(air_quality)
    return air_val


def main():
    """
        主函数
    """
    print('请输入一下信息，以空格分隔！')
    input_str = input('1.PM2.5,2.CO:')
    input_list = input_str.split(' ')
    pm_2_5 = eval(input_list[0])
    co = eval(input_list[1])
    put_list = [pm_2_5, co]
    air_quality = cal_air_quality(put_list)



if __name__ == '__main__':
    main()
