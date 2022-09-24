from skimage import io, color
import matplotlib.pyplot as plt
from PIL import Image

# Reading image and Splitting
im = Image.open(r"C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Playground"
                r"\\DJI_0804.jpg")
im1 = Image.Image.split(im)
im1[0].show()
imf = im1[0]
imf.save("C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Playground\\DJI.jpg")

# Reading image again for Histogram
image = io.imread('C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Playground\\DJI'
                  '.jpg')

# i = color.gray2rgb(image)

count, bins, temp = plt.hist(image.ravel(), bins=256)

float_number = []
for i in range(len(count)):
    float_number.append(float(count[i]))

print(float_number)

plt.show()
io.imsave('C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Playground\\DJI2.jpg',
          image)
