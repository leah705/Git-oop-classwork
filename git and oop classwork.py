#A:
#1.
class Vehicles:
    pass
#2.
class Vehicle:
  color = "white"#4 add a class attribute
  def __init__(self, max_speed ,mileage,capacity):#5.
      self.max_speed = max_speed
      self.mileage = mileage
      self.capacity = capacity
  def capacity(self):
      print(f" capacity is:{self.capacity}")
  #6.
  def far(self):
      return self.capacity*100
#3.
class Bus(Vehicle):
 def __init__(self, max_speed ,mileage,seating_capacity=50):
     super().__init__(max_speed ,mileage,seating_capacity)
 def seating_capacity(self):#5.
     print(f"seating capacity is:{self.seating_capacity}")
 def far(self):
     return (self.capacity()*100) + 50
 def display_info(self):

     print(f"bus Max Speed:{self.max_speed},bus mileage:{self.mileage},bus seating capacity:{self.capacity}")
car= Vehicle(150,12000,30)
print(car.far())
my_bus=Bus(1200,150000)
print(my_bus.far())
my_bus.display_info()