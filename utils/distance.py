"""
===========================================
Histogram comparison and distance
===========================================


"""
from scipy.spatial.distance import chebyshev
from scipy.spatial.distance import hamming
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import cityblock

import numpy as np

class distance:
    'Common base class for comparing distance between histogram'
    model = 0

    def __init__(self, model):
        models = {
            "hamming": hamming,
            "chebyshev": chebyshev,
            "euclidean": euclidean,
            "manhattan": cityblock,
            "chisquared":chi2_distance}
        self.model = models[model]
        print self.model

    def compute_distance(self, h1, h2):
        distance = self.model(h1,h2)
        return distance


def chi2_distance(histA, histB, eps = 1e-10):
    # compute the chi-squared distance
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])

    # return the chi-squared distance
    return d