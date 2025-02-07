# impliment constructor method and a method function that prints (my fav car is ____, it is this in colour, and manufuctured in __ yrs)
class cars:
    def __init__(self,brand,model,colour, year):
        self.brand = brand
        self.model = model
        self.colour = colour
        self.year = year
    def display(self):
        print (f"My favourite car is {self.brand}, speciffically the {self.model}, it is {self.colour} in colour and was manufuctured in the year {self.year}.")
m1 = cars("Mercedes","compressor 350", "black", 2019)
m2 = cars("Mercedes","AMG", "white", 2022)
m3 = cars("Dodge","Demon-ghost", "black", 2024)
m4 = cars("Porshe","Cayenne", "brown", 2018)
m5 = cars("Toyota","Supra,mk4", "red", 2012)
m6 = cars("Bugatti","Chirron", "blue & black", 2024)
m7 = cars("Lamborghini","Aventador", "red", 2020)
m1.display()
m2.display()
m3.display()
m4.display()
m5.display()
m6.display()
m7.display()