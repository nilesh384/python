class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw") 


p1 = Point()
p1.draw()
p1.move()

p1.x = 10
p1.y = 20

print(p1.x) 
print(p1.y)

p2 = Point()
p2.x = 11

print(p2.x)