import os
import sys
from pygame import image
from pygame.transform import scale


class ScaleZip:
    def process(self, zipprocessor):
        """Scale each image in the directory to user's size"""
        for filename in os.listdir(zipprocessor.temp_directory):
            im = image.load(zipprocessor._full_filename(filename))
            users_sizes = input(
                "Enter the size for image scaling for example - '640 400'"
                ).split()
            scaled = scale(im, (int(users_sizes[0]), int(users_sizes[1])))
            image.save(scaled, zipprocessor._full_filename(filename))
