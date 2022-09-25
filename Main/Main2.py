from PIL import Image
from skimage import io
import matplotlib.pyplot as plt
from numpy import asarray, cumsum

# Reading the image and splitting the color channels and saving the split image -> Package used PIL
im = Image.open(r"C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Main\\DJI.jpg")
im1 = Image.Image.split(im)
# im1[0].show()
imf = im1[0]  # im1[0] = Red channel, Similarly im1[1] = Green and im1[2] = Blue
imf.save("C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Main\\2D_DJI.jpg")

# Reading the image and for Histogram -> Package used skimage
image = io.imread('C:\\Users\\Rakshith R\\Documents\\PycharmProjects\\Hotspot-Detection-Solar-Panel\\Main\\2D_DJI.jpg')

# Plotting the Histogram -> Package used matplotlib
count, bins, patches = plt.hist(image.ravel(), bins=256)  # Saving the return of plt.hist

ran = len(count)
freq = []
N = 0

for i in range(ran):
    freq.append(float(count[i]))
    N += count[i]  # Total data points, Summation of frequency

# plt.show()  # Plot the Histogram
plt.close()

# Calculating Probability
prob = []
maxProb = 0
minProb = 0
posMaxProb = 0
probChecker = 0  # Should raise to 1 or very near to one, i.e. total probability
for j in range(ran):
    prob.append(freq[j] / N)
    probChecker += prob[j]

maxProb = max(freq)
minProb = min(freq)
posMaxProb = freq.index(maxProb) - 1  # -1 because index starts from 0

# Dividing pixels based on threshold
# c0 corresponds to pixel less than threshold(k)
# c1 corresponds to pixel more than threshold(k)
w0 = []  # Potential of class c0
w1 = []  # Potential of class c1
for a in range(ran):
    temp = 0
    for m in range(a):  # Iterates from 'm' to 'a-1'
        temp += prob[m]
    w0.append(temp)
    temp = 0
    for n in range(a, ran):  # Iterates from 'a' to 'n-1', so it is 'a+1' to '255'
        temp += prob[n]
    w1.append(temp)

# Class mean levels
m0 = []
m1 = []

for b in range(ran):
    temp = 0
    for o in range(b):
        temp += o * (prob[o] / w0[b])
    m0.append(temp)
    temp = 0
    for p in range(b, ran):
        temp += p * (prob[p] / w1[b])
    m1.append(temp)

# Between class variance
bcv = []
for c in range(ran):
    bcv.append(w0[c] * w1[c] * (pow((m1[c] - m0[c]), 2)))

maxBcv = bcv.index(max(bcv))

"""
plt.plot(bcv)
plt.twinx()
plt.plot(w0)
plt.twinx()
plt.plot(w1)
plt.twinx()
plt.plot(m0)
plt.twinx()
plt.plot(m1)
plt.show()
plt.close()
"""

# th = k * t  # This is the optimal threshold value. Here 'k' is threshold

# Generating a Black and White Image
cols, rows = imf.size  # Y,X   or   W,H   or   B,L
bwImage = [[1 for x in range(cols)] for y in range(rows)]
bwImage = asarray(bwImage)
refImg = asarray(image)

for y in range(rows):
    for x in range(cols):
        if refImg[y, x] >= maxBcv:
            bwImage[y, x] = 1
        else:
            bwImage[y, x] = 0

fig, axs = plt.subplots(nrows=2, ncols=2)

axs[0][0].imshow(image)
axs[0][1].imshow(refImg, cmap='Greys')
axs[1][0].imshow(refImg, cmap='inferno')
axs[1][1].imshow(bwImage, cmap='binary')
plt.show()
plt.close()
"""
plt.subplot(121)
plt.imshow(refImg)
plt.subplot(122)
plt.imshow(bwImage)
plt.show()
"""

"""
print(w0)
print(w1)
print(m0)
print(m1)
print(bcv)
print(maxBcv)
print(maxProb)
print(minProb)
print(posMaxProb)
print(freq)
print(N)
print(prob)
print(probChecker)
print(prob)
"""