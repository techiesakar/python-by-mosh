class Point:  # Init method is used to initalize the Object
    def __init__(self, x, y):  # self here is the reference to the current object
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)
print(point.y)
