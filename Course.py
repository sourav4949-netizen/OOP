class  Course:
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating

    def average(self):
        average=sum(self.rating)/len(self.rating)
        print("avg rating of",self.name,"is",average)

c1=Course('java',[1,2,3,4,5])
print(c1.name)
print(c1.rating)
c1.average()
c2=Course('python fundamentals',[5,5,5,5,4])
print(c2.name)
print(c2.rating)
c2.average()