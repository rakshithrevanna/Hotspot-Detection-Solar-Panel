"""
Threshold value increased from 139 to 156.88
Technique used to achieve is thresholding the image and find the corners of image by summation of all values of each row
Then finding the difference between each element and plotting the graph with the same values.
We get Corners which is used to crop the image
Author: Rakshith R
"""
from PIL import Image
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from numpy import asarray

# In the future, it will be redundant since block of code used to convert gray image to B/W image based and threshold
image = io.imread('C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Main\\mi2.jpg')

rows, cols = np.shape(image)
bwImage = [[1 for x in range(cols)] for y in range(rows)]
bwImage = asarray(bwImage)
refImg = asarray(image)

for y in range(rows):
    for x in range(cols):
        if refImg[y, x] >= 139:
            bwImage[y, x] = 1
        else:
            bwImage[y, x] = 0

sumRow = []
sumCol = []
"""
tempRow = image[0]
tempCol = image[:, 0]
"""
# Finding sum of each row of B/W image
for i in range(rows):
    tempRow = image[i]
    sumRow.append(sum(tempRow))

for j in range(cols):
    tempCol = image[:, j]
    sumCol.append(sum(tempCol))

# Finding the difference between corresponding elements
diffRow = np.diff(sumRow) / 1000
diffCol = np.diff(sumCol) / 1000

fig, axs = plt.subplots(nrows=2, ncols=2)

# Plotting the graph for observation
axs[0][0].plot(diffRow)
axs[0][1].plot(diffCol)
axs[1][0].imshow(bwImage)
axs[1][1].imshow(bwImage, cmap='binary')
plt.show()
plt.close()

# Convertion of array to list
dRow = []
dCol = []
for i in diffRow:
    dRow.append(i)
for j in diffCol:
    dCol.append(j)

# Fining the Max and Min coordinates
rowMax1 = dRow.index(max(dRow))
rowMax2 = dRow.index(min(dRow))

colMax1 = dCol.index(max(dCol))
colMax2 = dCol.index(min(dCol))
#         X  ,    X   ,    Y   ,   y
print(rowMax1, rowMax2, colMax1, colMax2)

#  Cropping the Image with bellow mentionined corners
box = (colMax1, rowMax1, colMax2, rowMax2)
img = Image.open(r"C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Main\\DJI.jpg")
croppedImage = img.crop(box)
croppedImage.save('C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Main\\cropped.jpg')
croppedImage.show()


#  Code Blocl used to mask Original image with the B/W Image
"""
image = np.random.randint(1, 11, (5, 5))
mask = np.zeros((5, 5))
mask[1:, 2:4] = 10
newImage = image * (mask != 0)
print(image, mask, newImage, sep='\n')
"""
