import cv2
import sys
import numpy as np
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here


        s = image.shape
        #print(s)
        #print(image)
        x = int(float(fx) * s[0])
        y = int(float(fy) * s[1])
        #print(xnew,ynew)
        I1 = np.zeros((x, y), np.uint8)
        shape = I1.shape
        for i in range(x-1):
            for j in range(y-1):
                nx = round(i / float(fx))
                ny = round(j / float(fy))
                # print(GI[i,j])
                I1[i, j] = image[nx, ny]
        # changed = cv2.imread(I1)
        # output = cv2.cvtColor(I1, cv2.COLOR_GRAY2BGR)
        # cv2.namedWindow("changed", cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("changed", output)
        # cv2.waitKey(10000)
        return I1

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here


        return image

