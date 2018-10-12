import array
import numpy as np

class ppmimpy:
	def __init__(self,form='P6',height=128,width=32,maxval=255):
		self.height = height
		self.width = width
		self.form = form
		self.maxval = maxval
		self.ppm_header = self.get_ppm_header(self.form,self.height,self.width,self.maxval)
		self.image = self.init_image()	

	def get_ppm_header(self,form,height,width,maxval):
		return 'P6 {} {} {}\n'.format(self.width,self.height,self.maxval)
	
	def init_image(self,r=0,g=0,b=0):
		return array.array('B',[r,g,b]*self.width*self.height)

	def array_to_image(self,ndarray):
		for x in range(self.height):
			for y in range(self.width):
				if ndarray[x][y] == 1:
					index = 3*(y*self.width+x)
					self.image[index] = 255
					self.image[index+1] = 255	 
					self.image[index+2] = 255
	def create_file(self,file_name):
		if file_name[-4:-1] != 'ppm':
			file_name = file_name+'.ppm'
		with open(file_name,'wb') as f:
			f.write(bytearray(self.ppm_header,'ascii'))
			self.image.tofile(f)
