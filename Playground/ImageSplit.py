# importing Image class from PIL package
from PIL import Image

# opening a multiband image (RGB specifically)
im = Image.open(r"C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Playground"
                r"\\DJI_0804.jpg")

# split() method
# this will split the image in individual bands
# and return a tuple
im1 = Image.Image.split(im)

# showing each band
im1[0].show()
im1[1].show()
im1[2].show()

imf = im1[0]
imf.save("C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Playground\\DJI.jpg")

