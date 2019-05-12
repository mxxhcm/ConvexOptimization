# -*- coding:utf-8 -*-

import os
import re


#pattern = "\'(n.*?txt)'"
def find_file_name_by_regex(pattern, parent_dir):
    # 列出所有的目录，并用str表示
    dir_list = os.listdir(parent_dir)
    dir_str = str(dir_list)

    # 利用正则表达式提取出来
    regex = re.compile(pattern)
    file_dir_list = regex.findall(dir_str)
    length = len(file_dir_list)
    return (length, file_dir_list)


def remove_file_by_regex(pattern, parent_dir):
    # 列出所有parent_dir目录下的文件，并用str来表示
    dir_list = os.listdir(parent_dir)
    dir_str = str(dir_list)

    # 利用regex 提出需要删除文件的目录
    regex = re.compile(pattern)
    file_dir_list = regex.findall(dir_str)

    for file_dir in file_dir_list:
        file_dir = parent_dir + file_dir
        os.remove(file_dir)

    length = len(file_dir_list)
    return length

def count_file_numbers_by_regex(pattern, parent_dir):
    # 列出所有parent_dir目录下的文件，并用str来表示
    dir_list = os.listdir(parent_dir)
    dir_str = str(dir_list)

    # 利用regex 提出需要查找文件的目录
    regex = re.compile(pattern)
    file_dir_list = regex.findall(dir_str)

    return (len(file_dir_list))



