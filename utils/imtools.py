"""
===========================================
Image tools
===========================================


"""

import os
import PIL.Image
import sys
sys.modules['Image'] = PIL.Image
from numpy import *



def get_imlist(path):
    """    Returns a list of filenames for
        all jpg images in a directory. """

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg') or f.endswith('.gif')]


def compute_average(imlist):
    """    Compute the average of a list of images. """

    # open first image and make into array of type float
    averageim = array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print imname + "...skipped"
    averageim /= len(imlist)

    # return average as uint8
    return array(averageim, 'uint8')


def convert_to_grayscale(imlist):
    """    Convert a set of images to grayscale. """

    for imname in imlist:
        im = Image.open(imname).convert("L")
        im.save(imname)


def imresize(im,sz):
    """    Resize an image array using PIL. """
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))


def histeq(im,nbr_bins=256):
    """    Histogram equalization of a grayscale image. """

    # get image histogram
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize

    # use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape), cdf
