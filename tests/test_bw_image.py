import sys
sys.path.append("./")

import numpy as np
import  ppmimpy as ppy
test = ppy.ppmimpy()
arr = np.zeros(shape=(32,128))
arr[4:10,10:100] = 1
arr[24:30,120:300] = 1
test.array_to_image(arr)
test.create_file('temp')



