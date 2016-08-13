"""
===========================================
4. Calculate TFIDF weight for image set
===========================================

"""

import numpy as np
import Image
import sys
sys.path.append('utils')
import imtools
import os
import pickle

from scipy.cluster.vq import *

f = open(sys.argv[1]+'_histograms.pickle', 'r')
histograms = pickle.load(f)
f.close()

path = sys.argv[1]

nbr_images = imtools.get_imlist(path)

#word, the index of 200 in the histogram
#im, the histogram of the specific image
#histograms, the list of histograms

#tf(word, histogram) computes "term frequency" which is the number of times a word appears in a image
def tf(word, im):
    return float(word) / sum(im)


#n_containing(word, histograms) returns the number of documents containing word.
def n_containing(wordidx, word, histograms):
    noOfContainingIms=[]
    count=0
    for idx,im in enumerate(histograms):
        if im[wordidx]>0:
            count+=1
    #word needs to be the index  in im of the word. If it is >0 it contains the word.
    return count

#idf(wordidx, word, histograms) computes "inverse document frequency" which measures how common a word is among all documents in bloblist
def idf(wordidx,word, histograms):
    #print n_containing(word, histograms)
    return np.log(len(histograms) / (1 + n_containing(wordidx, word, histograms)))

#tfidf(word, im, im_list) computes the TF-IDF score.
def tfidf(wordidx,word, im, histograms):
    return tf(word, im) * idf(wordidx, word, histograms)

all_scores=[]

f1 = open(sys.argv[1]+'_tfidf.pickle','w')
for i, im in enumerate(histograms):
    scores = [tfidf(wordidx,word, im, histograms) for wordidx,word in enumerate(im)]
    all_scores.append(scores)
    pickle.dump(scores,f1)

f1.close()


