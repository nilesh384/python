class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw") 

p1 = Point(10,20)
print(p1.x)
print(p1.y)
