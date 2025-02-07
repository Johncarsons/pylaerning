# object oriented programing
class Joker:
    def __init__(self, name , age ):
        # this is a constructor method
        # method is a function
        # it takes two parameters and initialise as attributes
        self.name = name
        self.age = age
    def funicito(self):
        print(f"Hello, my name is {self.name} and my age is {self.age}")
# create an objet=ct or an instance
meobj1 = Joker("Carson", 18)
meobj1.funicito()
meobj2 = Joker("Adorah", 17)
meobj2.funicito()
meobj3 = Joker("Kasongo", 57)
meobj3.funicito()
meobj4 = Joker("Zakayo", 57)
meobj5 = Joker("Zarubabel", 58)
meobj6 = Joker("Nomad", 60)
meobj5.funicito()
meobj6.funicito()
meobj4.funicito()
