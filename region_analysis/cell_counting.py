import cv2
import numpy as np
import sys
from skimage import color as sk
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""
        regions = dict()
        Input = image
        [m, n] = Input.shape
        # print(n)
        R = np.zeros((m, n), np.uint8)
        total = 1
        for i in range(m - 1):
            for j in range(n - 1):
                if Input[i, j] == 255 and Input[i, j - 1] == 0 and Input[i - 1, j - 1] == 0 and Input[i - 1, j] == 0 and Input[
                            i - 1, j + 1] == 0:
                    R[i, j] = total
                    total = total + 1
                if Input[i, j] == 255 and Input[i, j - 1] == 0 and Input[i - 1, j - 1] == 0 and Input[i - 1, j] == 0 and Input[
                            i - 1, j + 1] == 255:
                    R[i, j] = R[i - 1, j + 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 0 and Input[i - 1, j - 1] == 0 and Input[i - 1, j] == 255 and Input[
                            i - 1, j + 1] == 0:
                    R[i, j] = R[i - 1, j]
                if Input[i, j] == 255 and Input[i, j - 1] == 0 and Input[i - 1, j - 1] == 255 and Input[i - 1, j] == 0 and Input[
                            i - 1, j + 1] == 0:
                    R[i, j] = R[i - 1, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 255 and Input[i - 1, j - 1] == 0 and Input[i - 1, j] == 0 and Input[
                            i - 1, j + 1] == 0:
                    R[i, j] = R[i, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 255 and Input[i - 1, j - 1] == 255 and Input[i - 1, j] == 0 and Input[
                            i - 1, j + 1] == 0:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j - 1]:
                        R[i, j] = R[i - 1, j - 1]
                    else:
                        R[i, j - 1] = R[i - 1, j - 1]
                        R[i, j] = R[i, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 255 and Input[i - 1, j - 1] == 0 and Input[i - 1, j] == 255 and Input[
                            i - 1, j + 1] == 0:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i, j - 1] = R[i - 1, j]
                        R[i, j] = R[i, j - 1]

                if Input[i, j] == 255 and Input[i, j - 1] == 255 and Input[i - 1, j - 1] == 0 and Input[i - 1, j] == 0 and Input[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j + 1]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i, j - 1] = R[i - 1, j + 1]
                        R[i, j] = R[i, j - 1]

                if Input[i, j] == 255 and Input[i, j - 1] == 0 and Input[i - 1, j - 1] == 255 and Input[i - 1, j] == 255 and Input[
                            i - 1, j + 1] == 0:
                    if R[i, j] == R[i - 1, j - 1] == R[i - 1, j]:
                        R[i, j] = R[i - 1, j]
                    else:
                        R[i - 1, j - 1] = R[i - 1, j]
                        R[i, j] = R[i - 1, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 0 and Input[i - 1, j - 1] == 255 and Input[i - 1, j] == 0 and Input[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i - 1, j - 1] == R[i - 1, j + 1]:
                        R[i, j] = R[i - 1, j - 1]
                    else:
                        R[i - 1, j - 1] = R[i - 1, j + 1]
                        R[i, j] = R[i - 1, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 0 and Input[i - 1, j - 1] == 0 and Input[i - 1, j] == 255 and Input[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i - 1, j] == R[i - 1, j + 1]:
                        R[i, j] = R[i - 1, j]
                    else:
                        R[i - 1, j] = R[i - 1, j + 1]
                        R[i, j] = R[i - 1, j]
                if Input[i, j] == 255 and Input[i, j - 1] == 0 and Input[i - 1, j - 1] == 255 and Input[i - 1, j] == 255 and Input[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i - 1, j] == R[i - 1, j + 1] == R[i - 1, j - 1]:
                        R[i, j] = R[i - 1, j]
                    else:
                        R[i - 1, j] = R[i - 1, j + 1]
                        R[i - 1, j - 1] = R[i - 1, j]
                        R[i, j] = R[i - 1, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 255 and Input[i - 1, j - 1] == 0 and Input[i - 1, j] == 255 and Input[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i - 1, j] == R[i - 1, j + 1] == R[i, j - 1]:
                        R[i, j] = R[i - 1, j]
                    else:
                        R[i - 1, j] = R[i - 1, j + 1]
                        R[i, j - 1] = R[i - 1, j]
                        R[i, j] = R[i, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 255 and Input[i - 1, j - 1] == 255 and Input[i - 1, j] == 0 and Input[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j + 1] == R[i - 1, j - 1]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i - 1, j - 1] = R[i - 1, j + 1]
                        R[i, j - 1] = R[i - 1, j - 1]
                        R[i, j] = R[i, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 255 and Input[i - 1, j - 1] == 255 and Input[i - 1, j] == 255 and Input[
                            i - 1, j + 1] == 0:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j] == R[i - 1, j - 1]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i - 1, j - 1] = R[i - 1, j]
                        R[i, j - 1] = R[i - 1, j - 1]
                        R[i, j] = R[i, j - 1]
                if Input[i, j] == 255 and Input[i, j - 1] == 255 and Input[i - 1, j - 1] == 255 and Input[i - 1, j] == 255 and Input[
                            i - 1, j + 1] == 255:
                    if R[i, j] == R[i, j - 1] == R[i - 1, j] == R[i - 1, j - 1]:
                        R[i, j] = R[i, j - 1]
                    else:
                        R[i - 1, j] = R[i - 1, j + 1]
                        R[i - 1, j - 1] = R[i - 1, j]
                        R[i, j - 1] = R[i - 1, j - 1]
                        R[i, j] = R[i, j - 1]

        v = (R.argmax(0))
        # print(v)
        v1 = (v.max())
        # print("max no of objects")
        #  print(v1)
        print(total)
        for k in range(1, total):
            regions[k] = []
            for i in range(m):
                for j in range(n):
                    if R[i, j] == k:
                        regions[k].append([i, j])

        print("number of regions",regions)

        return regions



    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        finalreg = dict()
        count = 1
        for i in range(1, len(region) + 1):
            if (len(region[i]) > 15):
                dim1 = 0
                dim2 = 0
                for j in range(len(region[i])):
                    dim1 += (region[i][j][0] / len(region[i]))
                    dim2 += (region[i][j][1] / len(region[i]))

                finalreg[count] = [[int(dim1), int(dim2)], len(region[i])]
                count += 1

        print(len(finalreg))
        print(finalreg)
        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)


        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return finalreg

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        for i in range(1, len(stats) + 1):
            dim1 = stats[i][0][0]
            dim2 = stats[i][0][1]
            cv2.putText(image, "*", (dim1, dim2), cv2.FONT_HERSHEY_DUPLEX, 0.4, (126, 0, 0))

        return image

