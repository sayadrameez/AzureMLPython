from matplotlib import pyplot
from PIL import Image
import numpy as np
import skimage.color as sc
import requests
import io
resp = requests.get('https://github.com/sayadrameez/AI-Introduction/raw/master/files/graeme1.jpg')
imopenc1 = Image.open(io.BytesIO(resp.content))
i = np.array(imopenc1)
pyplot.imshow(i)
#pyplot.show()
print(type(i))
print(i.dtype)
print(i.shape)

im_mono = sc.rgb2gray(i)
pyplot.imshow(im_mono,cmap="gray")
#pyplot.show()
print(im_mono.shape)

def im_hist(img):
    fig = pyplot.figure(figsize=(8,6))
    fig.clf()
    ax = fig.gca()
    ax.hist(img.flatten(),bins=256)
    pyplot.show()
im_hist(im_mono)

def im_cdf(img):
    fig = pyplot.figure(figsize=(8,6))
    fig.clf()
    ax = fig.gca()
    ax.hist(img.flatten(),bins=256,cumulative = True)
    pyplot.show()
im_cdf(im_mono)

from skimage import exposure
i_eq = exposure.equalize_hist(im_mono)
pyplot.imshow(i_eq,cmap ="gray")
#pyplot.show()
im_cdf(i_eq)

import skimage
i_n = skimage.util.random_noise(i_eq)
pyplot.imshow(i_n,cmap="gray")
pyplot.show()


def gauss_filter(im , sigma=10):
    from scipy.ndimage.filters import gaussian_filter as gf
    import numpy as np
    return gf(im,sigma= sigma)
i_g = gauss_filter(i_n)
pyplot.imshow(i_g,cmap="gray")
pyplot.show()

def med_filter(im,size=10):
    from scipy.ndimage.filters import median_filter as mf
    import numpy as np
    return mf(im,size=size)
i_m = med_filter(i_n)
pyplot.imshow(i_m,cmap="gray")
pyplot.show()

def edge_sobel(im):
    from scipy import ndimage
    import skimage.color as sc
    import numpy as np
    image = sc.rgb2gray(im)
    dx = ndimage.sobel(im,1)
    dy = ndimage.sobel(im,0)
    mag = np.hypot(dx,dy)
    mag*=255.0 / np.amax(mag) # normalization
    mag = mag.astype(np.uint8)
    return mag

i_edge = edge_sobel(i_m)
pyplot.imshow(i_edge,cmap="gray")
pyplot.show()

def corner_harr(im,min_distance=5):
    from skimage.feature import corner_harris,corner_peaks
    mag = corner_harris(im)
    return corner_peaks(mag,min_distance=min_distance)
harris = corner_harr(i_eq)

def plot_harris(im,harris,markersize=10,color='red'):
    import matplotlib.pyplot as plt
    import numpy as np
    fig = plt.figure(figsize=(6,6))
    fig.clf()
    ax = fig.gca()
    ax.imshow(np.array(im).astype(float),cmap = "gray")
    ax.plot(harris[:,1],harris[:,1],'r+',color=color,markersize=markersize)
    plt.show()
    return 'Done'
    
plot_harris(i_eq,harris)