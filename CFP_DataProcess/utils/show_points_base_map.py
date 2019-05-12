# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

def read_long_lati(file_path):
    longitude = []
    latitude = []
    fp = open(file_path)
    files_list = fp.readlines()
    for file_str in files_list:
        file_str = file_str.strip("\n")
        file_str = file_str[2:-3]
        file_str = file_str.replace("'",'')
        file_list = file_str.split(",")
        latitude.append(float(file_list[0]))
        longitude.append(float(file_list[1]))
    #print(longitude,latitude)
    return longitude,latitude

pattern = ""
parent_dir = "/home/linc/Documents/sort_by_time_1211018404"

(long,lati)=read_long_lati(parent_dir)

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution=None,
width=8E6, height=8E6,
lat_0=45, lon_0=-100,)
m.etopo(scale=0.5, alpha=0.5)

# 将经纬度映射为 (x, y) 坐标，用于绘制图像
x, y = m(-122.3, 47.6)
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Seattle', fontsize=12);

