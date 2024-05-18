from graphics import Window, Line, Point

win = Window(800, 600)
point1 = Point(5,250)
point2 = Point(40, 430)
line1 = Line(point1, point2)
point3 = Point(580,250)
point4 = Point(450, 730)
line2 = Line(point3, point4)

win.draw_line(line1, "red")
win.draw_line(line2, "red")
win.wait_for_close()