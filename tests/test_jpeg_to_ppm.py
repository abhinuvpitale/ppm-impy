import numpy as np
from src import ppmimpy as ppy

def create_ppm_from_jpeg():
    test = ppy.ppmimpy()
    test.convert_to_ppm("./other/test.jpeg")

def test_can_create_jpeg():
    create_ppm_from_jpeg()
