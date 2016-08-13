"""
===========================================
Extract feature class
===========================================


"""

from skimage.feature import daisy
from skimage.feature import hog
from skimage.feature import ORB
from skimage.feature import local_binary_pattern
from skimage.color import rgb2gray

class extract_features:
   'Common base class for extracting features'
   model = 0

   def __init__(self, model):
      self.model = model

   def extractFeature(self,img):
    gray_img = rgb2gray(img)

    if  self.model == 'daisy':
        features = daisy(gray_img, step=16)
        return features

    elif  self.model== 'hog':
        features = hog(gray_img)
        return features

    elif  self.model == 'orb':
        orb = ORB(n_keypoints=100)
        orb.detect_and_extract(gray_img)
        return features

    elif  self.model == 'local_binary_pattern':
        features = local_binary_pattern(gray_img)
        return features




