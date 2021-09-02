class Programming:
    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setTechnology(self, tech):
        self.technology = tech

    def getTechnology(self):
        return self.technology

    def setSalary(self, sal):
        self.salary = sal

    def getSalary(self):
        return self.salary

p1 = Programming()
p1.setName('John')
p1.setTechnology(['java', 'python', 'hibernate', 'oracle'])
p1.setSalary(10000)
print(p1.getName())
print(p1.getSalary())
print(p1.getTechnology())
