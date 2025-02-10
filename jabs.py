class personel:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def didy(self):
        print(f"Me de {self.name} and me de age de  {self.age}")
mtu3 = personel("Abel", 26)
mtu2 = personel("Kamau", 29)
mtu1 = personel("Jane", 20)
mtu3.didy()
mtu2.didy()
mtu1.didy()