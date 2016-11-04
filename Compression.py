from __future__ import generators
import Points
import math

#given a point, the left-most point, the bottom-most point, and epsilon given a point back corresponding to grid slot
#e.g. given (3, 5) would mean grid[3][5]
def find_bucket(point, left, bottom, epsilon):
    return [math.floor(point[0] - (left[0] - 4 * epsilon)), math.floor(point[1] - (bottom[1] - 4 * epsilon))]

def extend_left(point1, point2, epsilon, points, grid):
    x_difference = point2[0] - point1[0]
    if x_difference == 0:
        x_difference = 1
    slope = float((point2[1] - point1[1]) / x_difference)
    point3 = [point2[0] - math.fabs(x_difference), slope * x_difference + point2[1]]
    bucket = find_bucket(point3, Points.get_left_point(points), Points.get_bottom_point(points), epsilon)
    points_found = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            try:
                slot = grid[bucket[0] + x][bucket[1] + y]
                for point in slot:
                    if math.sqrt((point[1] - point3[1]) ** 2 + (point[0] - point3[0]) ** 2) <= 8 * epsilon:
                        points_found.append(point3)
            except IndexError:
                continue
    return points_found

def extend_right(point1, point2, epsilon, points, grid):
    x_difference = point2[0] - point1[0]
    if x_difference == 0:
        x_difference = 1
    slope = float((point2[1] - point1[1]) / x_difference)
    point3 = [point2[0] + math.fabs(x_difference), slope * x_difference + point2[1]]
    bucket = find_bucket(point3, Points.get_left_point(points), Points.get_bottom_point(points), epsilon)
    points_found = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            try:
                slot = grid[bucket[0] + x][bucket[1] + y]
                for point in slot:
                    if math.sqrt((point[1] - point3[1]) ** 2 + (point[0] - point3[0]) ** 2) <= 8 * epsilon:
                        points_found.append(point3)
            except IndexError:
                continue
    return points_found

def check_distance(points, epsilon):
    for point1 in points:
        for point2 in points:
            if point1 == point2:
                continue
            if distance(point1, point2) <= 8 * epsilon:
                return True
    return False

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

epsilon = float(1/8)
points = Points.generatePoints(50, 0, 30, 0, 30)
while(check_distance(points, epsilon)):
    points = Points.generatePoints(50, -30, 30, -30, 30)
#points = [[4,2], [2,2], [0,2], [4, 4], [2, 4], [0, 4]]
grid = []

#calculate how many grid blocks there are in each dimension
width = (Points.get_right_point(points)[0] - (Points.get_left_point(points)[0] - 4 * epsilon)) / (8 * epsilon)
height = (Points.get_top_point(points)[1] - (Points.get_bottom_point(points)[1] - 4 * epsilon)) / (8 * epsilon)

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
    grid[first][second].append(point)

#extension process
sequences = []
for first in points:
    for second in points:
        if first[0] < second[0] or first == second:
            continue
        subsequence_left = [first, second]
        left = extend_left(subsequence_left[len(subsequence_left) - 2], subsequence_left[len(subsequence_left) - 1], epsilon, points, grid)
        while len(left) != 0:
            if len(left) > 1:
                print("EXTEND LEFT FOUND MORE THAN 1")
            subsequence_left.append(left[0])
            left = extend_left(subsequence_left[len(subsequence_left) - 2], subsequence_left[len(subsequence_left) - 1], epsilon, points, grid)

        subsequence_right = [second, first]
        right = extend_right(subsequence_right[len(subsequence_right) - 2], subsequence_right[len(subsequence_right) - 1], epsilon, points, grid)
        while len(right) != 0:
            if len(right) > 1:
                print("EXTEND RIGHT FOUND MORE THAN 1")
            subsequence_right.append(right[0])
            right = extend_right(subsequence_right[len(subsequence_right) - 2], subsequence_right[len(subsequence_right) - 1], epsilon, points, grid)
        subsequence = []
        for l in subsequence_left:
            if l not in subsequence:
                subsequence.append(l)
        for r in subsequence_right:
            if r not in subsequence:
                subsequence.append(r)
        subsequence.sort(key= lambda point: point[0])
        if len(subsequence) > 2 and subsequence not in sequences:
            sequences.append(subsequence)
print(sequences)