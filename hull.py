import matplotlib.pyplot as plt
import random
# The "2d" cross product of two vectors:
# a -> b, and a -> c.
# if the vectors are in the same line or if ac is counter-clockwise of ab, returns true.
# takes input as 3 pairs of [x, y]
# the equation Ux * Vy - Uy * Vx is from my math textbook


def is_ccw(a, b, c):
    normalized_b = (b[0] - a[0], b[1] - a[1])
    normalized_c = (c[0] - a[0], c[1] - a[1])
    return (
        normalized_b[0] * normalized_c[1] - normalized_b[1] * normalized_c[0]
    ) <= 0


def buildHalfHull(points):
    hull = []
    for point in points:
        while len(hull) >= 2 and is_ccw(hull[-2], hull[-1], point):
            hull = hull[:-1]
        hull.insert(len(hull), point)
    return hull


def convexHull(points):
    # sort the points by X, then by Y. python will automatically lexicographically sort tuples.
    points = sorted(points)

    # Andrew's monotone chain algorithm must build a lower and upper chain.
    # the lower chain starts from the left
    lower = buildHalfHull(points)
    # and the upper chain starts from the right
    upper = buildHalfHull(points[::-1])

    # we remove the last element in the lower half hull, since it's the same as the first in the other one
	# but we leave a duplicate starting and ending element.
    lower.pop()

    # add the lower to the upper (so our final hull goes clockwise)
    return [*lower, *upper]


if __name__ == "__main__":
    print("This program computes the Convex Hull of a random set of points on a 2D graph.")
    n = int(input("Please input the number of points on the board:"))
    points = [(random.randint(-100, 100), random.randint(-100, 100))
              for _ in range(n)]
    hull_points = convexHull(points)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x, y, marker='.', linestyle='None')

    # hull points
    hx = [p[0] for p in hull_points]
    hy = [p[1] for p in hull_points]
    plt.plot(hx, hy)

    plt.title('Convex Hull')
    plt.show()
