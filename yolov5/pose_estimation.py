
import cv2 as cv2
import numpy as np
import math

class PoseEstimation:
    def __init__(self, width : int, height : int, center_x : int, center_y : int, img_size):
        """
        Constructor of all PoseEstimation instances

        Parameters
        ----------
            width       : int
                width of the bounding box
            height      : int
                height of the bounding box
            center_x    : int
                center's x-cordinate of the bounding box
            center_y    : int
                center's y-cordinate of the bounding box
        """
        self.width = width
        self.height = height
        self.x = center_x
        self.y = center_y
        self.img_size = img_size

    def distanceFromCam(self, known_pixel_height : float = None, known_height : float = None, known_distance : float = None) -> float:
        """
        Parameters
        Note: All parameters are optional. If not passed an approx. is done.
        ----------
            known_pixel_height  : float
                Konwn pixel height of target
            known_height        : float
                Konwn height of target
            known_distance      : float
                Distance of the target from camera
        """
        if known_pixel_height != None and known_height != None and known_distance != None:
            focal_length = float(known_pixel_height * known_distance) / known_height
            distance = float(known_height * focal_length) / self.height
            return distance
        else:
            if self.width <= self.height:
                max_image_height = int(self.img_size[0])
                return (float(max_image_height) / self.height) - 1
            else:
                max_image_width = int(self.img_size[1])
                return (float(max_image_width) / self.width) - 1

    def distanceFromCenter(self):
        return (((float(self.img_size[0])/2) - self.y)**2 + ((float(self.img_size[1])/2) - self.x)**2) ** 0.5

    def angle(self):
        if self.width == self.height:
            return 0
        elif self.width < self.height:
            return math.degrees(np.arccos(float(self.width) / self.height))
        else:
            return math.degrees(np.arccos(float(self.height) / self.width))



