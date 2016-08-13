"""
===========================================
3. Create Histograms and Calculate TFIDF weight for image set
===========================================


"""
import numpy as np
import sys
sys.path.append('utils')
import imtools
import os
import pickle

from skimage.feature import daisy
from skimage.color import rgb2gray
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from scipy.sparse import coo_matrix

from PIL import Image
class patternHistograms:
    def __init__(self,img_type,vocab_size=800,feature):
        self.img_type = img_type
        self.vocab_size = vocab_size
        self.feature = feature

if __name__ == '__main__':
    f = open(sys.argv[1]+'_vocab.pickle', 'r')
    km = pickle.load(f)
    path = sys.argv[1]

    im_list = imtools.get_imlist(path)

    counts=[]
    words=[]
    word_occurences=[]
    hists = []
    words_1 = []
    for idx,image_name in enumerate(im_list):
        features = daisy(rgb2gray(np.array(Image.open(image_name))), step=8)
        words = km.predict(features.reshape(-1, 200))
        hists.append(np.bincount(words,minlength = 800))
        words_1.append(words)


    #normalize the histograms
    def normalizeHIstogram(histogram):
        return [word / sum(histogram) for word in float(histogram)]

    f1 = open(sys.argv[1]+'_histograms.pickle','w')
    pickle.dump(hists,f1)
    f1.close()