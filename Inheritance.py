class BMW:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print("starting the car")
    def stop(self):
        print("stoppimg the car")


class ThreeSeries(BMW):
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    def start(self):
        super().start()
        print("Inside ThreeSeries started")

"""in line 16 we are over riding the functiondefined inside the parent class, and again in line 17 we are calling the 
function from parent by using the super keywords.   
overriding is runtime polymorphism      
BMW.__init__(self,make,model,year)
Instead of giving the name of the parent class.init we can directly give super.init withot passing in the self varibale"""



class FourSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


threeSeries = ThreeSeries(True, "BMW", "328i", 2018)
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
fourSeries=FourSeries(True,"BMW","428i",2019)
print(fourSeries.parkingAssistEnabled)
print(fourSeries.make)
print(fourSeries.model)
print(fourSeries.year)
fourSeries.start()
fourSeries.stop()
