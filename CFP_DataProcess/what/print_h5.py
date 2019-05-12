import os 
import h5py

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dir')
args = parser.parse_args()


def read(parent_dir):
  f = h5py.File(parent_dir)
  data = f['data'][:]
  date = f['date'][:]
  print(date)
  print(data.shape)


if __name__ == '__main__':
  read(args.dir)
