class Car:
    def __init__(self,w,d):
        self.value=w
        self.unit=d
    def __str__(self):
      if self.unit=="kmh":
        return str("my speed is "+str(self.value)+" "+str(self.unit))
      else:
        return str("my speed is "+str(self.value)+" "+str(self.unit))
class Boat:
    def __init__(self,b):
      self.value=b
    def __str__(self):
      return str("my speed is "+str(self.value)+" knots")

ob=Car(21,'kph')
print (ob)
ob=Car(25,'mph')
print(ob)
ob=Boat(288)
print(ob)
