import array
import numpy as np


class ppmimpy:
    def __init__(self, form='P6', height=32, width=128, maxval=255):
        self.height = height
        self.width = width
        self.form = form
        self.maxval = maxval
        self.ppm_header = self.get_ppm_header(
            self.form, self.height,
            self.width, self.maxval)
        self.image = self.init_image()

    def get_ppm_header(self, form, height, width, maxval):
        return 'P6 {} {} {}\n'.format(self.width, self.height, self.maxval)

    def init_image(self, r=0, g=0, b=0):
        return array.array('B', [r, g, b]*self.width*self.height)

    def array_to_image(self, ndarray):
        if np.shape(ndarray) == (self.height, self.width):
            for x in range(self.height):
                for y in range(self.width):
                    if ndarray[x][y] == 1:
                        index = 3*(x*self.width+y)
                        self.image[index] = 255
                        self.image[index+1] = 255
                        self.image[index+2] = 255
        else:
            print('Wrong Sized Array!!!')

    def create_file(self, file_name):
        if file_name[-4:-1] != 'ppm':
            file_name = file_name+'.ppm'
        with open(file_name, 'wb') as f:
            f.write(bytearray(self.ppm_header, 'ascii'))
            self.image.tofile(f)i

    def convert_to_ppm(self, file_name):
	file_name_save = file_name
	file_name = file_name.tolower()
	if file_name.endswith(".jpeg") or file_name.endswith(".jpg"):
		return self._convert_jpg(file_name)

 
