class Student:
    def __init__(self):
        self.__name="Sourav"
        self.__id=123
    def display(self):
        print(self.__name)
        print(self.__id)

s=Student()
s.display()
print(s._Student__name)
"""name mangling--In python the private members are not completely hidden. it is stored as the format specified above 
and is termed as name mangling.Below are the dynamic variable entry into the fields"""

class Students:
    def setNames(self,names):
        self.names=names
    def getNames(self):
        return(self.names)
    def setIds(self,ids):
        self.ids=ids
    def getIds(self):
        return(self.ids)
s1=Students()
s1.setIds(1)
print(s1.getIds())
s1.setNames("Sourav")
print(s1.getNames())