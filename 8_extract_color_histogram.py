"""
===========================================
8. Create color histograms for color comparison
===========================================

"""
import sys
sys.path.append('utils')
import imtools
import pickle
import cPickle
import numpy as np
from PIL import Image

from skimage.color import rgb2gray
from skimage.color import rgb2hsv

class colorhistogram:
    'Common base class for converting to different color spaces'
    model = 0

    def __init__(self, model,bin_size):
        models = {
            "hsv":  rgb2hsv}
        self.model = models[model]
        self.bin_size = bin_size

    def convert_histogram(self, img_name):
        img = (np.array(Image.open(img_name)))
        return img

    def extract_histogram(self,img):
        hist = np.histogram(img, bins=self.bin_size)
        return hist

    def extract_channel_histogram(self,img):
        all_hist = []
        for idz in range(0,3):
            ch_hist,bin_edges = np.histogram(img[idz], bins=self.bin_size)
            all_hist.append(ch_hist)

        return all_hist


if __name__ == '__main__':
    path = sys.argv[1]
    im_list = imtools.get_imlist(path)
    color_hist_list= []
    color  = colorhistogram("hsv",8)
    for idx,image_name in enumerate(im_list):
        hsv_img = color.convert_histogram(image_name)
        color_hist = color.extract_channel_histogram(hsv_img)
        color_hist = np.hstack(color_hist)
        color_hist_list.append(color_hist)


f1 = open(sys.argv[1]+'_color_histograms.pickle','w')
pickle.dump(color_hist_list,f1)
f1.close()