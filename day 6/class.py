class car:
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname)
        print(self.year)

c1 = car("bmw",2021)
c1.display()
