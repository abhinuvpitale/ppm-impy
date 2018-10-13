import numpy as np
from src import ppmimpy as ppy


def create_black_and_white_image():
    test = ppy.ppmimpy()
    arr = np.zeros(shape=(32, 128))
    arr[4:10, 10:100] = 1
    arr[24:30, 120:300] = 1
    test.array_to_image(arr)
    test.create_file('ppms/temp')


def test_can_create_black_and_white_image():
    create_black_and_white_image()
