class Person:

    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print(f"hi i am {self.name}")

p1 = Person("Ayush")
print(f"My name is {p1.name}")
p1.talk()