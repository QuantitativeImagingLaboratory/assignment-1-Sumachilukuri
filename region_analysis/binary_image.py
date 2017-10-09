import cv2
import numpy as np
import sys
import os
from random import uniform
import matplotlib.pyplot as plt


class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        (dim1, dim2) = image.shape
        hist = [0] * 256

        for i in range(dim1):
            for j in range(dim2):
                hist[image[i, j]] += 1

        return hist

    int1 = list(range(0, 256))
    freq = list(range(0, 256))
    k = int1[0]
    j = int1[-1]
    min_int1 = min(int1)
    max_int1 = max(int1)
    rand_val = min_int1 + (max_int1 - min_int1) * uniform(0, 1)
    # print(rand_val)

    def find_optimal_threshold(self,thresh):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""
        int1 = list(range(0, 256))
        freq = list(range(0, 256))
        k = int1[0]
        j = int1[-1]
        min_int1 = min(int1)
        max_int1 = max(int1)

        total = 0
        number = 0
        finaltotal = 0
        final_number = 0
        t = 0
        op_t = round(thresh)
        for x in range(k, op_t):
            total = total + int1[x]
            number = number + 1

        mean_thresh = total / number
        for y in range(op_t, j):
            finaltotal = finaltotal + int1[y]
            final_number = final_number + 1

        mean_end = finaltotal / final_number
        avg = round((mean_thresh + mean_end) / 2)
        while 1:
            if (abs(avg - op_t) == 0):
                op_t = avg
                t = 1
                # print(op_t)
                break
            else:
                t = 0
                c = self.find_optimal_threshold(avg)
                
                op_t = c
                break

            if t == 1:
                op_t = avg
                #print(op_t)
                break

        return op_t



    def binarize(self, image,a):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        [k, l] = image.shape
        out_img = image
        #print(image)
        for i in range(0, k):
            for j in range(0, l):
                if (image[i, j]) < a:
                    out_img[i, j] = 255
                else:
                    out_img[i, j] = 0

        out_img = image.copy()
        return out_img
        bin_img = image.copy()




