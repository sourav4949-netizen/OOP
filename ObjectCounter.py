"""In this program we are trying to count the number  of objects created of the given class.
we are able to do it by defining a variable callled noOfObject inside the class.
Each time a new object is created the __init__ function or constructor will increase the value of noOfObject
so we can keep a track on the number of object created """

class ObjectCounter:
    noOfObject =0

    def __init__(self):
        ObjectCounter.noOfObject+=1

    @staticmethod
    def display():
        print("No of object of the class ObjectCounter created in this program is:",ObjectCounter.noOfObject)


o1=ObjectCounter()
o2=ObjectCounter()
o3=ObjectCounter()
ObjectCounter.display()

