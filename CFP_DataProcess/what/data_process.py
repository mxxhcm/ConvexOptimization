import os
import shutil
import pandas as pd
import re

class deal_didi:
  #def __init__(self):

  def deal_all_file(self, pattern, parent_dir):
    if os.path.exists(parent_dir+"single_driver_data"):
      shutil.rmtree(parent_dir+"single_driver_data")
    os.mkdir(parent_dir+"single_driver_data")
    
    files = self.find_file_path(pattern, parent_dir)
    print(files)
    for file_path in files:
      print(file_path)
      self.deal_one_file(parent_dir,file_path)

      
  def deal_one_file(self, parent_dir, file_path):    
    data = pd.read_csv(file_path, header=None, prefix='L')
    if not os.path.exists(parent_dir+"single_driver_data"):
      os.mkdir(parent_dir+"single_driver_data")
    for key, value in data.groupby('L0'):
      file_name = key
      print(file_name)
      fp = open(parent_dir + "single_driver_data/" + file_name, "a")
      value = value.values
      value_list = value.tolist()
      # write list to file
      for single_list in value_list:
         single_str = str(single_list)
         single_str = single_str[1:-1]
         fp.write(single_str+"\n")
      fp.close()


  def find_file_path(self, pattern, parent_dir):
    dir_list = os.listdir(parent_dir)
    dir_str = str(dir_list)
    # print(dir_str)
    # compile pattern
    pattern = re.compile(pattern)
    file_dir_list = pattern.findall(dir_str)
    # print(file_dir_list)
    # print(len(file_dir_list))
    return file_dir_list

if __name__ == '__main__':
  parent_dir = "/home/linc/two_storage/didi/gps/"
  pattern = "gps_201611[0-3][0-9]"
  didi = deal_didi()
  pathname = "/home/linc/two_storage/didi/gps/test"
  didi.deal_one_file(parent_dir, pathname)
  #didi.deal_all_file(pattern, parent_dir)
