__author__ = 'Caleb'
import random

def generatePoints(num, x1, x2, y1, y2):
    """Returns a generated list of points in a given area
    
    Returns a list of <num> points randomly distributed from (x1, y1) to (but not including) (x2, y2)
    
    Arguments:
        num {int} -- Number of points to be generated
        x1 {int} -- X-coordinate of first (inclusive) corner
        x2 {int} -- X-coordinate of second (exclusive) corner
        y1 {int} -- Y-coordinate of first (inclusive) corner
        y2 {int} -- Y-coordinate of second (exclusive) corner
    """
    points = []
    while(len(points) < num):
        point = [random.randint(x1, x2), random.randint(y1, y2)]
        if point not in points:
            points.append(point)
    return points

def get_left_point(points):
    """Returns the the left-most point given a list of points.
    
    Given more than one left-most (lowest x-value) point, the point with the lowest y-value is returned.
    
    Arguments:
        points {list of points} -- The list of points to be included in the search for the left-most point.
    """
    points.sort(key=lambda point: point[0])
    left = []
    for point in points:
        if point[0] == points[0][0]:
            left.append(point)
    left.sort(key=lambda data: data[1])
    return left[0]

def get_right_point(points):
    """Returns the right-most point, given a list of points.
    
    Given more than one right-most (highest x-value) point, the point with the lowest y-value is returned.
    
    Arguments:
        points {list of points} -- The list of points to be included in the search for the left-most point.
    """
    points.sort(key=lambda point: point[0])
    bottom = []
    for point in points:
        if point[0] == points[len(points) - 1][0]:
            bottom.append(point)
    bottom.sort(key=lambda data: data[1])
    return bottom[0]

def get_bottom_point(points):
    """Returns the lowest y-value point given a list of points.
    
    Returns lowest x-value point as a secondary key if there is more than one lowest y-value point.
    
    Arguments:
        points {list of points} -- The list of points from which to choose a bottom-most point.
    """
    points.sort(key=lambda point: point[1])
    bottom = []
    for point in points:
        if point[1] == points[0][1]:
            bottom.append(point)
    bottom.sort(key=lambda data: data[0])
    return bottom[0]

def get_top_point(points):
    """Returns the highest y-value point given a list of points.
    
    Returns lowest x-value point as a secondary key if there is more than one highest y-value point.
    
    Arguments:
        points {list of points} -- The list of points from which to choose a top-most point.
    """
    points.sort(key=lambda point: point[1])
    bottom = []
    for point in points:
        if point[1] == points[len(points) - 1][1]:
            bottom.append(point)
    bottom.sort(key=lambda data: data[0])
    return bottom[0]
