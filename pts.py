def points(x,y,h,m,l):
    x1 = x
    y1 = y - h
    x2 = x1 + l
    y2 = y1 - l*m
    x3 = x2
    y3 = y + h + l*m
    x4 = x
    y4 = y + h
    print(f"{x1},{y1} {x2},{y2} {x3},{y3} {x4},{y4}")

points(60,60, 7, .15, 38)
points(60,60, 7, .15, 45)
points(60,60, 7, .15, 35)
