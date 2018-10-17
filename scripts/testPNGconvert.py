import numpy as np
from PIL import Image


img = Image.open('tests.jpeg')
img.load()
img = img.convert("1")
img = img.resize((128,32))
data = np.asarray(img,dtype = np.int8)
print(data)
img.show()

