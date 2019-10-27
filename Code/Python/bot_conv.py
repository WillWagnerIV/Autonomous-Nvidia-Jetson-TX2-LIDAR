# The conversion methods for our GIS Bot
# Will Wagner

import time
from math import degrees, radians, cos, sin, asin, atan2, sqrt, pi

R = 6371007.1810 # Radius of the earth in Meters per IUGG Spheroid - not WGS84 Ellipsoid


class Point:
    total_points = 0
    def __init__(self, x, y, z, lat, lon):
        self.x, self.y, self.z, self.lat, self.lon = x, y, z, lat, lon

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.x, self.y, self.z, self.lat, self.lon)

    def __neg__(self):
        return Point(-self.x, -self.y, self.z, self.lat, self.lon)

    def __add__(self, point):
        return Point(self.x+point.x, self.y+point.y, self.z, self.lat, self.lon)

    def __sub__(self, point):
        return self + -point


def latlong_to_cart (lat, lon):

    # Radians = Degrees * Pi/180
    # lat = lat * (pi / 180)
    # lon = lon * (pi / 180)
    lat = radians(lat)
    lon = radians(lon)
    
    x = R * cos(lat) * cos(lon)
    y = R * cos(lat) * sin(lon)
    z = R * sin(lat)
    timestamp = time.time()
    # print (x,y,z,timestamp)
    
    return x,y,z,timestamp


def cart_to_latlong (x,y,z):

    lat = asin(z/R)
    lon = atan2(y, x)
    timestamp = time.time()
    # print (lat,lon,timestamp)

    # Degrees = 180/Pi * Radians
    lat = (180/pi) * lat
    lon = (180/pi) * lon

    return lat,lon,timestamp


def radial_to_cart (angle, dist):

    angle = radians(angle)
    
    x = dist * cos(angle)
    y = dist * sin(angle)

    print (x, y)
    return x,y


def cart_to_radial(x,y):
    dist = sqrt(x^2 + y^2)
    angle = atan2 (y,x)
    angle = degrees(angle)

    print (angle, dist)


def point_to_point_latlon(point1, point2):
    #Read the input from user
    # print("Enter the latitude and longitude of two points on the Earth in degrees:")
    # lat1 = float(input(" Latitude 1: "))
    # lat2 = float(input(" Latitude 2: "))
    # lon1 = float(input(" Longitude 1: "))
    # lon2 = float(input(" Longitude 2: "))
    
    # The math module contains a function named radians which converts from degrees to radians.
    lat1 = radians(point1.lat)
    lon1 = radians(point1.lon)
    lat2 = radians(point2.lat)
    lon2 = radians(point2.lon)
    
    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    
    # Display the result
    print("Distance is: ",c*R,"Meters")


def point_to_point_xy(point1,point2):
    print (point1 + point2)



# print ("\n\n\n")
# x,y,z,timestamp = latlong_to_cart (34.0966667, -117.7188889)
# print (x,y,z,timestamp)

# lat,lon,timestamp = cart_to_latlong(x,y,z)
# print (lat,lon,timestamp)


# radial_to_cart(235,20.05)
# cart_to_radial(10,7)


# testpoint1 = Point(10,10,10,41,-117)
# testpoint2 = Point(25,30,10,41.05,-117.05)
# point_to_point_latlon(testpoint1,testpoint2)
# point_to_point_xy(testpoint1,testpoint2)