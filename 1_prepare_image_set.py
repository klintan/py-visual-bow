"""
===========================================
1. Prepare image set
===========================================
Make sure all image are same width and height (keep aspect ratio)

"""
import numpy as np
import sys
from PIL import Image
import sys
sys.path.append('utils')
import imtools
import os



class prepareImages:
    def __init__(self, path, size=[200,200]):
        self.path = sys.argv[1]
        self.im_list = imtools.get_imlist(path)
        self.size = size#200,200

def imagePrep(self):
    for idx, im_name in enumerate(self.im_list):
        im = Image.open(im_name)
        im.thumbnail(self.size, Image.ANTIALIAS)
        im_name_nospaces = im_name.replace(" ","")
        im.save(self.path+'_new/'+os.path.basename(im_name_nospaces))
        print im_name
        print idx

if __name__ == '__main__':
    prepIm = prepareImages(sys_argv[1])
    prepIm.imagePrep()