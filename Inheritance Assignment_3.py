class Vehicle:
    def move(self):
     print("vehicle is moving")



class bike(Vehicle):
   def move(self):
      print("bike is moving") 

class car(Vehicle):
   def movie(self):
      print("car is moving")
      


a=bike()
b=car()

a.move()
b.move()