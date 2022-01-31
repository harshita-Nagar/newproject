# super()

class Vehicle:
    def __init__(self,engine):
        print("Inside Vehicle constructor")
        self.engine=engine


class Car(Vehicle):
    def __init__(self,engine,max_speed):
        super().__init__(engine)
        print("Inside Car constructor")
        self.max_speed=max_speed


class ElectricCar:
    def __init__(self,engine,max_speed,km_range):
        super().__init__(engine,max_speed)
        print("Inside ElectricCar constructor")
        self.km_range=km_range


ev=ElectricCar("1500 cc",90,200)
print(f"engine:", ev.engine, "max_speed:", ev.max_speed, "km_range:", ev.km_range)


# A child class constructor can also invoke the parent class constructor using the super() method.





