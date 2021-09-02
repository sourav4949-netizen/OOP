"""When we define a class we can create an abstract method. An abstarct method is a method which is haveing a method
heading using @abstractmethod as a decorator. when ever a child class is defined for taht we need to define the
abstract method inside the child class otherwise the child class will also become an abstract class, and we
cannot create a object of abstract class. If atleast one method in a class is a abstract method then that class
becomes a abstract class.
In python an abstract class is called an interface
The below code is taken from inheritance. and added the concept for abstraction of drive method"""
from abc import abstractmethod, ABC



class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print("starting the car")
    def stop(self):
        print("stoppimg the car")
    @abstractmethod
    def drive(self):
        pass


class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    def start(self):
        super().start()
        print("Inside ThreeSeries started")
    def drive(self):
        print("driving Three series")

"""in line 16 we are over riding the functiondefined inside the parent class, and again in line 17 we are calling the 
function from parent by using the super keywords.   
overriding is runtime polymorphism      
BMW.__init__(self,make,model,year)
Instead of giving the name of the parent class.init we can directly give super.init withot passing in the self varibale"""



class FourSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
    def drive(self):
        print("driving five series")


threeSeries = ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.drive()
fourSeries=FourSeries(True,"BMW","428i",2019)
print(fourSeries.parkingAssistEnabled)
print(fourSeries.make)
print(fourSeries.model)
print(fourSeries.year)
fourSeries.start()
fourSeries.stop()
fourSeries.drive()
