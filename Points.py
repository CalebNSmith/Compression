__author__ = 'Caleb'
import random

#generates a given number of points randomly distributed from (x1, y1) to (but not including) (x2, y2)
def generatePoints(num, x1, x2, y1, y2):
    points = []
    while(len(points) < num):
        point = [random.randint(x1, x2), random.randint(y1, y2)]
        if point not in points:
            points.append(point)
    return points

#Given a list of points, returns the point with the lowest y of the points with the lowest x
def get_left_point(points):
    points.sort(key=lambda point: point[0])
    left = []
    for point in points:
        if point[0] == points[0][0]:
            left.append(point)
    left.sort(key=lambda data: data[1])
    return left[0]

#Given a list of points, returns the point with the lowest y of the points with the greatest x
def get_right_point(points):
    points.sort(key=lambda point: point[0])
    bottom = []
    for point in points:
        if point[0] == points[len(points) - 1][0]:
            bottom.append(point)
    bottom.sort(key=lambda data: data[1])
    return bottom[0]

#Given a list of points, returns the point with the lowest x of the points with the lowest y
def get_bottom_point(points):
    points.sort(key=lambda point: point[1])
    bottom = []
    for point in points:
        if point[1] == points[0][1]:
            bottom.append(point)
    bottom.sort(key=lambda data: data[0])
    return bottom[0]

#Given a list of points, returns the point with the lowest x of the points with the greatest y
def get_top_point(points):
    points.sort(key=lambda point: point[1])
    bottom = []
    for point in points:
        if point[1] == points[len(points) - 1][1]:
            bottom.append(point)
    bottom.sort(key=lambda data: data[0])
    return bottom[0]
