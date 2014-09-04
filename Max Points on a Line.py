__author__ = 'samsung'
def maxPoints(points):
    n = len(points)
    if n <= 2:
        return n
    mymax = 0
    for i in xrange(n-1):
        slope = {'inf': 0}
        same = 1
        result = 0
        for j in xrange(i+1, n):
            x1 = points[i].x
            x2 = points[j].x
            y1 = points[i].y
            y2 = points[j].y
            if x1 == x2 and y1 != y2:
                k = 'inf'
                slope[k] = slope.get(k, 0) + 1
            elif x1 == x2 and y1 == y2:
                same += 1
            else:
                k = float(y2 - y1) / float(x2 - x1)
                slope[k] = slope.get(k, 0) + 1
        result = max(slope.values()) + same
        if result > mymax:
            mymax = result
    return mymax

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

points = [Point(0, 0), Point(1, 1), Point(0, 0)]
print maxPoints(points)
