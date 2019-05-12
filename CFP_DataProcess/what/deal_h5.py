import argparse

import h5py
import numpy


parser = argparse.ArgumentParser(usage="?",description="help for deal_h5")
parser.add_argument("path",help="pathname to deal")
args = parser.parse_args()

class deal_h5:
    def __init__(self,pathname):
        self.pathname = pathname

    def count_num_in_array(self, array, num):
        return numpy.sum(array == num)
    
    def deal(self):
        f = h5py.File(self.pathname)
        self.data = f['data'][:]
        self.date = f['date'][:]
        print(self.data.shape)
        self.shape = self.data.shape
        self.max = self.data.max()
        self.min = self.data.min()
        self.sum = self.data.sum()
        l = len(self.shape)
        self.size = 1
        for i in range(l):
            self.size = self.size * self.shape[i]
        self.count = numpy.zeros((int(self.max)+1), dtype='i')
        for i in range(int(self.max) + 1):
            self.count[i] = self.count_num_in_array(self.data, i)
        # print(self.count)
        f.close()

if __name__ == '__main__':
    h5 = deal_h5(args.path)
    h5.deal()
    print(h5.max)
    print(h5.min)
    print(h5.sum)
    print(h5.count_num_in_array(h5.data, 0))
    print(h5.size)
