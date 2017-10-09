import cv2
import numpy as np
import sys
from random import uniform
import matplotlib.pyplot as plt
class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        [dim1,dim2] = image.shape
        hist = [0]*256
        for i in range(dim1):
            for j in range(dim2):
                hist[image[i,j]] += 1


        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""


    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        return bin_img


