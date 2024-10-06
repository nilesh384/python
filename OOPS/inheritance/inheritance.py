class Mammal:
    def walk(self):
        print("all walk")


class dog(Mammal):
    def bark(self):
        print("dog bark")


class cat(Mammal):
    pass
    
d1 = dog()
d1.walk()
d1.bark()

c1 = cat()
c1.walk()