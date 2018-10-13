import array

# PPM header
width = 256
height = 128
maxval = 255
ppm_header = 'P6 {} {} {}\n'.format(width, height, maxval)

# PPM image data (filled with blue)
image = array.array('B', [0, 0, 0] * width * height)

# Create a red rectangle with origin at (10, 10)
# The width x height = 50 x 80 pixels
for y in range(10, 90):
    for x in range(10, 60):
        index = 3 * (y * width + x)
        image[index] = 255           # red channel
        image[index + 1] = 255       # green channel
        image[index + 2] = 255       # blue channel

# Save the PPM image as a binary file
with open('blue_red_example.ppm', 'wb') as f:
    f.write(bytearray(ppm_header, 'ascii'))
    image.tofile(f)
