"""
===========================================
9. Compute comparisons between color histograms
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

import distance as dist


f = open(sys.argv[1]+'_color_histograms.pickle', 'r')
color_histograms = pickle.load(f)
f.close()

im_list = imtools.get_imlist(sys.argv[1])
dist_function = dist.distance('chisquared')
temp_dist = []
all_dist = []

for idx,h1 in enumerate(color_histograms):
    f1 = open(sys.argv[1]+'_color_comparison.pickle', mode='a+b')
    for h2 in color_histograms:
        vector_distance = dist_function.compute_distance(h1,h2)
        temp_dist.append(vector_distance)

    cPickle.dump(temp_dist,f1)
    temp_dist = []
    f1.close()
