class Point:  # Here Point is a Class
    def move(self):  # Here move is a function for moving a point
        print("move")

    def draw(self):
        print("draw")


point1 = Point()  # Point() is object and we store it in Variable
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

