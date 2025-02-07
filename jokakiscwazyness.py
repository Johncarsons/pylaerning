class cars:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname, self.year)
c1 = cars("Lamborghini Aventador", 2019)
c1.display()
c2 = cars("Porshe Cayenne", 2017)
c2.display()