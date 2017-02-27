from __future__ import generators
import Points
import math
from scipy.optimize import linprog


# Given a point, the left-most point, the bottom-most point, and epsilon given a point back corresponding to grid slot
# e.g. given (3, 5) would mean grid[3][5]
def find_bucket(point, left, bottom, epsilon):
    """Returns the array indices that a point belongs to after generating the grid

    
    Arguments:
        point {list of integers} -- the point from Points.py that you want to find the grid slot for
        left {list of integers} -- The leftmost point in the dataset, retrived from Points.get_left_point()
        bottom {list of integers} -- The bottommost point in the dataset, retrived from Points.get_bottom_point
        epsilon {float} -- Degree of error
    """
    return [int((point[0] - (left[0] - 4 * epsilon))), int((point[1] - (bottom[1] - 4 * epsilon)))]


def extend_right(point1, point2, epsilon, points, grid):
    """[summary]
    
    [description]
    
    Arguments:
        point1 {[type]} -- [description]
        point2 {[type]} -- [description]
        epsilon {[type]} -- [description]
        points {[type]} -- [description]
        grid {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    canExtend = True
    starting_points = [point1, point2]
    while(canExtend):
        ideal_point = [starting_points[-1][0] + math.fabs((starting_points[-1][0] - starting_points[-2][0])), starting_points[-1][1] + math.fabs((starting_points[-1][1] - starting_points[-2][1]))]
        bucket = find_bucket(ideal_point, Points.get_left_point(points), Points.get_bottom_point(points), epsilon)
        numPoints = len(starting_points)
        for x in range(-1, 2):
            for y in range(-1, 2):
                if numPoints < len(starting_points):
                    continue
                try:
                    slot = grid[bucket[0] + x][bucket[1] + y]
                    for point in slot:
                        if point in starting_points:
                            continue
                        if math.fabs(point[0] - ideal_point[0]) <= 4 * epsilon and math.fabs(point[1] - ideal_point[1]) <= 4 * epsilon:
                            c = [0, 0, epsilon]
                            A = []
                            b = []
                            for i in range(len(starting_points)): #two bounds for each point
                                A.append([starting_points[i][0], 1, -1])
                                b.append(starting_points[i][1])
                                A.append([-starting_points[i][0], -1, -1])
                                b.append(-starting_points[i][1])
                            A.append([point[0], 1, -1])
                            b.append(point[1])
                            A.append([-point[0], -1, -1])
                            b.append(-point[1])
                            res = linprog(c, A_ub=A, b_ub=b, options={"disp":True})
                            if res.success and float(res.x[-1]) <= epsilon:
                                    starting_points.append(point)

                except IndexError as err: #avoid out of bounds on the boundry of the grid
                    # print(str(bucket[0]))
                    # print(str(bucket[1]))
                    # print(len(grid))
                    # print(len(grid[0]))
                    # print("ERRRRR")
                    continue
        if numPoints < len(starting_points):
            canExtend = True
        else:
            canExtend = False
    return starting_points





def extend_left(point1, point2, epsilon, points, grid):
    """[summary]

    [description]

    Arguments:
        point1 {[type]} -- [description]
        point2 {[type]} -- [description]
        epsilon {[type]} -- [description]
        points {[type]} -- [description]
        grid {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    canExtend = True
    starting_points = [point1, point2]
    while(canExtend):
        ideal_point = [starting_points[-1][0] - math.fabs((starting_points[-1][0] - starting_points[-2][0])), starting_points[-1][1] - math.fabs((starting_points[-1][1] - starting_points[-2][1]))]
        bucket = find_bucket(ideal_point, Points.get_left_point(points), Points.get_bottom_point(points), epsilon)
        numPoints = len(starting_points)
        for x in range(-1, 2):
            for y in range(-1, 2):
                if numPoints < len(starting_points):
                    continue
                try:
                    slot = grid[bucket[0] + x][bucket[1] + y]
                    for point in slot:
                        if point in starting_points:
                            continue
                        if math.fabs(point[0] - ideal_point[0]) <= 4 * epsilon and math.fabs(point[1] - ideal_point[1]) <= 4 * epsilon:
                            c = [0, 0, epsilon]
                            A = []
                            b = []
                            for i in range(len(starting_points)): #two bounds for each point
                                A.append([starting_points[i][0], 1, -1])
                                b.append(starting_points[i][1])
                                A.append([-starting_points[i][0], -1, -1])
                                b.append(-starting_points[i][1])
                            A.append([point[0], 1, -1])
                            b.append(point[1])
                            A.append([-point[0], -1, -1])
                            b.append(-point[1])
                            res = linprog(c, A_ub=A, b_ub=b, options={"disp":True})
                            if res.success and float(res.x[-1]) <= epsilon:
                                    starting_points.append(point)

                except IndexError as err: #avoid out of bounds on the boundry of the grid
                    # print(str(bucket[0]))
                    # print(str(bucket[1]))
                    # print(len(grid))
                    # print(len(grid[0]))
                    # print("ERRRRR")
                    continue
        if numPoints < len(starting_points):
            canExtend = True
        else:
            canExtend = False
    return starting_points


def check_distance(points, epsilon):
    """Returns true if any two points are within 8*epsilon of each other
    
    
    Arguments:
        points {list of a list of integers} -- List of points from Points.py
        epsilon {float} -- Degree of error
    
    Returns:
        bool -- If all of the points are >= 8*epsilon apart, return false; Otherwise return true
    """
    for point1 in points:
        for point2 in points:
            if point1 == point2:
                continue
            if distance(point1, point2) < 8 * epsilon:
                return True
    return False

def distance(point1, point2):
    """Distance between two points
    
    Arguments:
        point1 {list of integers} -- 
        point2 {list of integers} -- 
    
    Returns:
        float -- distance between the two points
    """
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


epsilon = float(1/8)
points = Points.generatePoints(75, 0, 30, 0, 30)
while(check_distance(points, epsilon)):
    points = Points.generatePoints(75, 0, 30, 0, 30)
#points = [[4,2], [2,2], [0,2], [4, 4], [2, 4], [0, 4]]
grid = []

#calculate how many grid blocks there are in each dimension
width = (Points.get_right_point(points)[0] + 4 * epsilon - (Points.get_left_point(points)[0] - 4 * epsilon)) / (8 * epsilon)
height = (Points.get_top_point(points)[1] + 4 * epsilon - (Points.get_bottom_point(points)[1] - 4 * epsilon)) / (8 * epsilon)

#create the grid
for x in range(math.ceil(width)):
    grid.append([])
for slot in grid:
    for y in range(math.ceil(height)):
        slot.append([])

#place each point in its corresponding grid slot
left = Points.get_left_point(points)[0] - 4 * epsilon
bottom = Points.get_bottom_point(points)[1] - 4 * epsilon
for point in points:
    first = math.floor(point[0] - left)
    second = math.floor(point[1] - bottom)
    try:
        bucket = find_bucket(point, Points.get_left_point(points), Points.get_bottom_point(points), epsilon)
        grid[bucket[0]][bucket[1]].append(point)
    except IndexError as err:
        print(len(grid))
        print(first)
        print(len(grid[0]))
        print(second)

extend = []
for i in points:
    for j in points:
        if i is not j:
            right = extend_right(i, j, epsilon, points, grid)
            left = extend_left(i, j, epsilon, points, grid)
            combined = []
            for k in range(len(left) - 1, 1, -1):
                combined.append(left[k])
            for k in range(len(right)):
                combined.append(right[k])
            extend.append(combined)
for e in extend:
    if len(e) > 3:
        print(e)