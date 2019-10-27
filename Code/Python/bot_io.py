# Input and Output functions for the bot
# Will Wagner

import bot_conv as bcon
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import degrees, radians, cos, sin, asin, atan2, sqrt, pi


def create_test_lidar_data(num_rows):
    test_lidar_points = []
    angle = 0
    offset = 0
    size = 1

    fig, temp_plot = plt.subplots()

    for row in range(num_rows):
        angle += .5
        if angle > 360: 
            angle -= 360
            offset += 5
            size += 1
        distance = 5 + offset
        x,y = bcon.radial_to_cart(angle, distance)
        point = bcon.Point (x,y,0,41,-117)
        test_lidar_points.append(point)

        temp_plot.scatter(x, y, s=size, c='black', alpha=.75)

    # For a circle with origin (j, k) and radius r:
    j = 0 
    k = 0
    r = 1

    for t in range(360):
        x = r * cos(t) + j
        y = r * sin(t) + k

        temp_plot.scatter(x, y, s=1, c='green', alpha=.5)
        # plt.subplot(111, projection='polar')

    temp_plot.set_xlabel(r'Cartesian X', fontsize=15)
    temp_plot.set_ylabel(r'Cartesian Y', fontsize=15)
    temp_plot.set_title('Test Data Set - Green is a R=1 Reference Circle')

    temp_plot.grid(True)
    fig.tight_layout()
    plt.show()



def plot_points (list_of_points):

    fig, main_plot = plt.subplots()

    for point in list_of_points:
        main_plot.scatter(point.x, point.y, s=10, c='black', alpha=.75)


# create_test_lidar_data(1000)

