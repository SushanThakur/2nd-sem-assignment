points = [(1, 2), (2, 4), (3, 6)]
(x1, y1), (x2, y2) = points[0], points[1]
slope = (y2 - y1) / (x2 - x1)

collinear = True
for i in range(2, len(points)):
    x, y = points[i]
    if (y - y1) / (x - x1) != slope:
        collinear = False
        break

print("Points form straight line" if collinear else "Not a straight line")

