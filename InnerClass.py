class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, number):
            self.number = number

        def start(self):
            print("Engine started", self.number)

        def __del__(self):
            print("inside the destructor")


c = Car("BMW", 2017)
e = c.Engine(29888)
e.start()
