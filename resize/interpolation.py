import cv2
import sys
class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here
        newIntensity = 0
        x = 0
        y = 0
        p1, int1 = pt1
        p2, int2 = pt2
        value = unknown
        Int_new = p2 - p1
        if (Int_new == 0):
            Int_new = 1

        a1 = p2 - value
        b1 = a1 / Int_new
        x = int1 * b1
        a2 = value - p1
        b2 = a2 / Int_new
        y = int2 * b2

        newIntensity = x + y
        if (newIntensity > 255):
            newIntensity = newIntensity - 255

        return newIntensity



    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task
        pointX1, pointY1, int1 = pt1
        pointX2, pointY2, int2 = pt2
        pointX3, pointY3, int3 = pt3
        pointX4, pointY4, int4 = pt4
        valueX1, valueY1 = unknown

        newInt1 = self.linear_interpolation((pointX1, int1), (pointX2, int2), valueX1)
        newInt2 = self.linear_interpolation((pointX3, int3), (pointX4, int4), valueX1)
        newpt1 = pointY1, newInt1
        newpt2 = pointY4, newInt2
        out_value = self.linear_interpolation(newpt1, newpt2, valueY1)
        return out_value


