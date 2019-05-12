# -*- coding:UTF-8 -*-

import h5py
import numpy as np
import time
import os

from utils.find_remove_count_files_by_regex import find_file_name_by_regex
import shutil
import seaborn as sns

class inflow_outflow():

    def __init__(self, pattern, parent_dir, m, n, begin_long, end_long, begin_lati, end_lati, time_interval):
        self.pattern = pattern
        self.parent_dir = parent_dir
        self.m = m
        self.n = n
        self.begin_long = begin_long
        self.end_long = end_long
        self.begin_lati = begin_lati
        self.end_lati = end_lati
        self.time_interval = time_interval
        (self.files_num, self.files) = find_file_name_by_regex(pattern, parent_dir)

	# self.files = ["new_eovsyt.txt"]

    # 读取某个目录下的所有原始轨迹文件，写入新的加入inflow和outflow的文件
    def create_inflow_outflow(self):     
        for file in self.files:
            # print(file)
            file_dir = self.parent_dir + file
            if os.path.isdir(file_dir):
              print(file_dir)
              continue
            trajectory = self.get_trajectory(file_dir)
            #inflow_outflow_raw_data_pathname = self.parent_dir + str(self.time_interval) + "_" + str(self.begin_long) + "_"+ str(self.end_long) + "_" + str(self.begin_lati) + "_" + str(self.end_lati) + "/inflow_outflow_raw_data_" + file
            inflow_outflow_raw_data_pathname = self.parent_dir + str(self.time_interval) + "_" + str(self.begin_long) + "_"+ str(self.end_long) + "_" + str(self.begin_lati) + "_" + str(self.end_lati) + "_" + str(self.m) + "_" + str(self.n) + "/inflow_outflow_raw_data_" + file
            trajectory = self.process_long_lati_one_trajectory_didi(trajectory, inflow_outflow_raw_data_pathname)
        
    # 将pathname中的原始数据读出来转化为list形式
    def get_trajectory(self, pathname):
        with open(pathname, "r") as f:
            trajectory = []
            for item_str in f:
                item_str = item_str.strip("\n")
                item_list = item_str.split(" ")
                trajectory.append(item_list)
            return trajectory
    
    def process_long_lati_one_trajectory(self, trajectory, inflow_outflow_raw_data_pathname):

        # 将经纬度进行分割
        long_interval = round((self.end_long - self.begin_long)/self.m, 10)
        lati_interval = round((self.end_lati - self.begin_lati)/self.n, 10)


        # 统计超范围和没有超范围的格子数
        counter_long_break = 0
        counter_lati_break = 0
        counter = 0

        f = open(inflow_outflow_raw_data_pathname, "w")
        # 上一个区域
        last_area = (-1, -1)
        last_item = []
        for k, item in enumerate(trajectory):
            # 如果超过了我们统计的经纬度范围，跳过
            # item : [longitude, latitude, is_people, timestamp]
            item[0] = float(item[0])
            item[1] = float(item[1])
            item[3] = int(item[3])
            # current_area, in_flow, is_inflow_update, out_flow, is_outflow_update
            temp = [(-1, -1), (-1, -1), 0, (-1, -1), 0]
            if item[1] < self.begin_long or item[1] > self.end_long:
                counter_long_break += 1
                area = (-1, -1)
            elif item[0] < self.begin_lati or item[0] > self.end_lati:
                counter_lati_break += 1
                area = (-1, -1)
            else:
                # 计算这个点是哪个区域的
                i = (item[1] - self.begin_long) // long_interval
                j = (item[0] - self.begin_lati) // lati_interval
                i = int(i)
                j = int(j)
                area = (i, j)    # 这次的区域
                counter += 1

            # 本次的区域
            item.append(area)

            # 0表示没有更换区域，1表示更新了区域
            # 上一次的outflow
            last_item.append(area)
            if last_area == area:
                last_item.append(0)
            else:
                last_item.append(1)
            if k != 0:
              f.write(str(last_item)+"\n")
            # 本次的inflow
            item.append(last_area)
            if area == last_area:
                item.append(0)
            else:
                item.append(1)

            # 记录一下当前item和area
            last_area = area
            last_item = item

        f.close()
        return trajectory

    def process_long_lati_one_trajectory_didi(self, trajectory, inflow_outflow_raw_data_pathname):

        # 将经纬度进行分割
        long_interval = round((self.end_long - self.begin_long)/self.m, 10)
        lati_interval = round((self.end_lati - self.begin_lati)/self.n, 10)


        # 统计超范围和没有超范围的格子数
        counter_long_break = 0
        counter_lati_break = 0
        counter = 0

        f = open(inflow_outflow_raw_data_pathname, "w")
        # 上一个区域
        last_area = (-1, -1)
        last_item = []
        for k, item in enumerate(trajectory):
            # 如果超过了我们统计的经纬度范围，跳过
            # item : [id,id, timestamp, longitude, latitude]
            item[3] = float(item[3][:-1])
            item[4] = float(item[4])
            item[2] = int(item[2][:-1])
            # current_area, in_flow, is_inflow_update, out_flow, is_outflow_update
            temp = [(-1, -1), (-1, -1), 0, (-1, -1), 0]
            if item[3] < self.begin_long or item[3] > self.end_long:
                counter_long_break += 1
                area = (-1, -1)
            elif item[4] < self.begin_lati or item[4] > self.end_lati:
                counter_lati_break += 1
                area = (-1, -1)
            else:
                # 计算这个点是哪个区域的
                i = (item[3] - self.begin_long) // long_interval
                j = (item[4] - self.begin_lati) // lati_interval
                i = int(i)
                j = int(j)
                area = (i, j)    # 这次的区域
                counter += 1

            # 本次的区域
            item.append(area)

            # 0表示没有更换区域，1表示更新了区域
            # 上一次的outflow
            last_item.append(area)
            if last_area == area:
                last_item.append(0)
            else:
                last_item.append(1)
            if k != 0:
              f.write(str(last_item)+"\n")
            # 本次的inflow
            item.append(last_area)
            if area == last_area:
                item.append(0)
            else:
                item.append(1)

            # 记录一下当前item和area
            last_area = area
            last_item = item

        f.close()
        return trajectory


class flow(object):
    def __init__(self, begin_time, end_time, time_interval, m, n, nb_flow):
        self.begin_time = begin_time
        self.end_time = end_time
        self.time_interval = time_interval
        self.time_series = self.create_time_series()
        self.nb_timeslot = self.time_series.shape[0]
        self.nb_flow = nb_flow
        self.counts = np.zeros((self.nb_timeslot, m, n, nb_flow), dtype='i')
        self.m = m
        self.n = n
        self.nb_flow = nb_flow
    
    def create_time_series(self):
        time_series = np.arange(self.begin_time, self.end_time, self.time_interval)
        for i, data in enumerate(time_series):
            time_local = time.localtime(time_series[i])
            time_series[i] = time.strftime("%Y%m%d", time_local)

        last_time = time_series[0]
        count = 1
        for i, data in enumerate(time_series):
            if time_series[i] == last_time:
                time_series[i] = str(time_series[i]) + str(count).zfill(4)

            else:
                count = 1
                last_time = time_series[i]
                time_series[i] = str(time_series[i]) + str(count).zfill(4)
            count += 1

        return time_series


    def write_to_h5file(self, file_name):
        from copy import deepcopy
        f = h5py.File(file_name, "w")
        f['data'] = self.counts
        f['date'] = self.time_series.astype('S12')
        f.close()
    
    def get_trajectory(self, pathname):
        with open(pathname, "r") as f:
            trajectory = []
            for item_str in f:
                item_str = item_str.strip("\n")
                item_str = item_str[1:-1]
                item_str = item_str.replace("\\'","")
                item_str = item_str.replace(" ","")
                item_str = item_str.replace("(","")
                item_str = item_str.replace(")","")
                item_list = item_str.split(",")
                item_list[0] = float(item_list[0])
                item_list[1] = float(item_list[1])
                item_list[3] = int(item_list[3])
                item_list[4] = (int(item_list[4]), int(item_list[5]))
                item_list[5] = (int(item_list[6]), int(item_list[7]))
                item_list[6] = int(item_list[8])
                item_list[7] = (int(item_list[9]), int(item_list[10]))
                item_list[8] = int(item_list[11])
                trajectory.append(item_list)
            return trajectory

    def get_trajectory_didi(self, pathname):
        with open(pathname, "r") as f:
            trajectory = []
            for item_str in f:
                item_str = item_str.strip("\n")
                item_str = item_str[1:-1]
                item_str = item_str.replace("\',", "")
                item_str = item_str.replace(" ", "")
                item_str = item_str.replace("(", "")
                item_str = item_str.replace(")", "")
                item_list = item_str.split(",")

                item_list[2] = int(item_list[2])
                item_list[3] = float(item_list[3])
                item_list[4] = float(item_list[4])
                item_list[5] = (int(item_list[5]), int(item_list[6]))
                item_list[6] = (int(item_list[7]), int(item_list[8]))
                item_list[7] = int(item_list[9])
                item_list[8] = (int(item_list[10]), int(item_list[11]))
                item_list[9] = int(item_list[12])
                trajectory.append(item_list)
            return trajectory


class two_flow(flow):
    def __init__(self, begin_time, end_time, time_interval, m, n, nb_flow):
        # 声明一个numpy ndarray
        super(two_flow, self).__init__(begin_time, end_time, time_interval, m, n, nb_flow)
        
    # 统计在某一个时间段内的in和out flow
    def count_in_out_flows(self,in_out_flow_raw_data):

        for i, item in enumerate(in_out_flow_raw_data):
            # longitude, latitude, is_people, timestamp, area, in_flow,in_flow_change, out_flow,out_flow_change
            # print(i, " : ", item)
            if i == len(in_out_flow_raw_data) - 1:
                continue
            timestamp = item[2]
            area = item[5]
            inflow_change = item[7]
            outflow_change = item[9]
            time_slot = (timestamp - self.begin_time)//self.time_interval
            if inflow_change == 1:
                self.counts[time_slot][area[0]][area[1]][0] += 1
            if outflow_change == 1:
                self.counts[time_slot][area[0]][area[1]][1] += 1

        # print(counts)


class sixteen_flow(flow):
    
    def __init__(self, begin_time, end_time, time_interval, m, n, nb_flow):
        # 声明一个numpy ndarray
        super(sixteen_flow, self).__init__(begin_time, end_time, time_interval, m, n, nb_flow)

    # 统计在某一个时间段内的各个方向的flow
    def count_sixteen_flow(self,in_out_flow_raw_data):

        for i, item in enumerate(in_out_flow_raw_data):
            if i == len(in_out_flow_raw_data) - 1:
                continue
            timestamp = item[3]
            area = item[4]
            inflow_area = item[5]
            outflow_area = item[7]
            inflow_change = item[6]
            outflow_chagne = item[8]
            time_slot = (timestamp - self.begin_time) // self.time_interval
            if inflow_change == 1:
                inflow_direction = (area[0] - inflow_area[0], area[1] - inflow_area[1])
                if inflow_direction[0] > 0 and inflow_direction[1] > 0:
                    self.counts[time_slot][area[0]][area[1]][0] += 1
                if inflow_direction[0] == 0 and inflow_direction[1] > 0:
                    self.counts[time_slot][area[0]][area[1]][1] += 1
                if inflow_direction[0] < 0 and (inflow_direction[1] > 0):
                    self.counts[time_slot][area[0]][area[1]][2] += 1
                if inflow_direction[0] < 0 and inflow_direction[1] == 0:
                    self.counts[time_slot][area[0]][area[1]][3] += 1
                if inflow_direction[0] < 0 and inflow_direction[1] < 0:
                    self.counts[time_slot][area[0]][area[1]][4] += 1
                if inflow_direction[0] == 0 and inflow_direction[1] < 0:
                    self.counts[time_slot][area[0]][area[1]][5] += 1
                if inflow_direction[0] > 0 and (inflow_direction[1] < 0):
                    self.counts[time_slot][area[0]][area[1]][6] += 1
                if inflow_direction[0] > 0 and inflow_direction[1] == 0:
                    self.counts[time_slot][area[0]][area[1]][7] += 1
            
            if outflow_chagne == 1:
                outflow_direction = (outflow_area[0] - area[0], outflow_area[1] - area[1])
                if outflow_direction[0] < 0 and outflow_direction[1] < 0:
                    self.counts[time_slot][area[0]][area[1]][0] += 1
                if outflow_direction[0] == 0 and outflow_direction[1] < 0:
                    self.counts[time_slot][area[0]][area[1]][1] += 1
                if outflow_direction[0] > 0 and (outflow_direction[1] < 0):
                    self.counts[time_slot][area[0]][area[1]][2] += 1
                if outflow_direction[0] > 0 and outflow_direction[1] == 0:
                    self.counts[time_slot][area[0]][area[1]][3] += 1
                if outflow_direction[0] > 0 and outflow_direction[1] > 0:
                    self.counts[time_slot][area[0]][area[1]][4] += 1
                if outflow_direction[0] == 0 and outflow_direction[1] > 0:
                    self.counts[time_slot][area[0]][area[1]][5] += 1
                if outflow_direction[0] < 0 and (outflow_direction[1] > 0):
                    self.counts[time_slot][area[0]][area[1]][6] += 1
                if outflow_direction[0] < 0 and outflow_direction[1] == 0:
                    self.counts[time_slot][area[0]][area[1]][7] += 1






# 开始时间和结束时间
# begin_time = 1211018404
# end_time = 1213089934

# 经纬度的范围
# begin_long = -122.46
# end_long = -122.40
# begin_lati = 37.75
# end_lati = 37.80

# begin_long = -122.54
# end_long = -122.36
# begin_lati = 37.70
# end_lati = 37.82

# time_interval = 1800
# nb_flows = 16
# m = 32
# n = 32


# didi@chengdu
begin_time = 1477929600
end_time = 1480521600
time_interval = 300
m = n = 32 
#begin_long = 104.05
#begin_lati = 30.66
#end_long = 104.12
#end_lati = 30.73

begin_long = 104.04
end_long = 104.13
begin_lati = 30.65
end_lati = 30.73
nb_flows = 2

h5_file_name = "./info_didi/TaxiDD_" + str(begin_long) + "_" + str(end_long) + "_" + str(begin_lati) + "_" + str(end_lati) + "_" + str(time_interval) + "_" + str(m) + "_" + str(n) + "_" + str(nb_flows) + "_count.h5"

with open(h5_file_name + "info", "w") as f:
   info = "begin_long : " + str(begin_long) + "\n"  + \
          "end_long : " + str(end_long) + "\n" + \
          "begin_lati : " + str(begin_lati) + "\n" + \
          "end_lati : " + str(end_lati) + "\n" + \
          "begin_time : " + str(begin_time) + "\n" + \
          "end_time : " + str(end_time) + "\n" + \
          "time_interval : "+ str(time_interval)+"\n" + \
          "m = n = " + str(m) + "\n"
   f.write(info)
  

# pattern = "n.*?txt"
pattern = "\'(.*?)'"
pattern_inout_flow = "\'(in.*?txt)'"

parent_dir = "/home/linc-3/one_storage/data.bak/didi_data/gps/single_driver_data/"

# in_out_raw_file path
# (count, inoutfiles) = find_file_name_by_regex(pattern_inout_flow, parent_dir)

# 创建inflow_outflow对象，用来生成原始的inflow和outflow文件
flow = inflow_outflow(pattern, parent_dir, m, n, begin_long, end_long, begin_lati, end_lati, time_interval)
#pathname = parent_dir + str(time_interval) + "_" + str(begin_long) + "_" + str(end_long) + "_" + str(begin_lati) + "_" + str(end_lati) + "/"
pathname = parent_dir + str(time_interval) + "_" + str(begin_long) + "_" + str(end_long) + "_" + str(begin_lati) + "_" + str(end_lati) + "_" + str(m) + "_" + str(n)+"/"

with open( "./info_didi/" + str(time_interval) + "_" + str(begin_long) + "_" + str(end_long) + "_" + str(begin_lati) + "_" + str(end_lati) + "_" + str(m) + "_" + str(n) + ".files","w") as f:
   f.write(str(flow.files))
#print(flow.files)
# 生成含有inflow_outflow的文件
#if os.path.exists(pathname):
#    #os.rmdir(pathname)
#   shutil.rmtree(pathname)
#os.mkdir(pathname)
print("mkdir : " + pathname)
#flow.create_inflow_outflow()

# 创建flow对象，根据inflow和outflow统计flow数量
# sixteen = sixteen_flow(begin_time, end_time, time_interval, m, n, nb_flows)
two = two_flow(begin_time, end_time, time_interval, m, n, nb_flows)

# flow.files = ["new_ubgihoot.txt"]
for f in flow.files:
    # f = "180_104.04_104.13_30.65_30.73"
    if os.path.isdir(parent_dir + f):
        print(parent_dir + f + "is not a file!!!")
        continue
    f = pathname + "inflow_outflow_raw_data_" + f
    #print(f)
    trajectory = two.get_trajectory_didi(f)
    # sixteen.count_sixteen_flow(trajectory)
    two.count_in_out_flows(trajectory)

# sixteen.write_to_h5file("./TaxiSF_16_count.h5")
# file_name = "./TaxiDD_" + str(time_interval) + "_" + str(m) + "_" + str(n) + "_" + str(nb_flows) + "_count.h5"

two.write_to_h5file(h5_file_name)

