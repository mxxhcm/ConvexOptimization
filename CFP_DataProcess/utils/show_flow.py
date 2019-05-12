import matplotlib.pyplot as plt
import numpy as np
import argparse
import h5py


class show_flow:

    def show_scatter(self,x,y,picture_name):
        plt.scatter(x,y)
        plt.title(picture_name)
        plt.show()
    
    # 
    def show_img(self,img, x):
        img = img * 1.0 / x
        plt.imshow(img)
        plt.show()

    
if __name__ == '__main__':
    flow = show_flow()
    x = [1, 2, 3]
    y = [3, 4, 2]
    flow.show(x, y, "test")