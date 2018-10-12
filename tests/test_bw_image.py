import numpy as np
import  ppmimpy as ppy

test = ppy.ppmimpy()
arr = np.zeros(shape=(128,32))
arr[10:100][4:10] = 1
arr[120:300][24:30] = 1
test.array_to_image(arr)
test.create_file('temp')



