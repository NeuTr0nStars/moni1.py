import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt

def geodistance(lng1, lat1, lng2, lat2):
    '公式计算两点间距离（m）'
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])  # 经纬度转换成弧度
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    distance = round(distance / 1000, 3)  # 得到单位km
    return distance

def cal_h(region_df):
    city_ind_h = {} #计算每个产业的最优的h值和距离对
    # n = region_df.shape[0]
    city_list = list(region_df['citycode'].unique())
    ind_list = list(region_df['CIC3_2002'].unique())
    city_ind_dis = []
    for city in city_list:
        for ind in ind_list:
            try:
                one_city_ind_df = region_df[(region_df['CIC3_2002'] == ind) & (region_df['citycode'] == city)]
                one_city_ind_df = one_city_ind_df.reset_index(drop=True)
                n = one_city_ind_df.shape[0]
                for i in range(len(one_city_ind_df)-1):
                    lng1 = one_city_ind_df.loc[i,'WGS_lon']
                    lat1 = one_city_ind_df.loc[i,'WGS_lat']
                    for j in range(i+1,len(one_city_ind_df)):
                        lng2 = one_city_ind_df.loc[j, 'WGS_lon']
                        lat2 = one_city_ind_df.loc[j, 'WGS_lat']
                        dis = geodistance(lng1, lat1, lng2, lat2)
                        print(dis)
                        city_ind_dis = city_ind_dis + [dis]
            except Exception as error:
                print(error)
    return city_ind_dis




if __name__ == '__main__':
    file_path = r'E:\数据\DO\DO指数测算数据集\DO少量指标\all.csv'
    df = pd.read_csv(file_path)
    d = cal_h(df)
    print(np.median(d))
    print(np.max(d))















