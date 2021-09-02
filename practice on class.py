class circle():
    pi=3.14
    print("[ennter the radius as per u r need")
    radius=int(input())
    #def __init__(self,radius=int(input())):
     #   self.radius= radius
    def circuference(self):
        return 2 * circle.pi * self.radius
    def area(self):
        return circle.pi * self.radius * self.radius
#output=circle()
print(circle().circuference())
print(circle().area())