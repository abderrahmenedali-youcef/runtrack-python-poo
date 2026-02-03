class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    def vieillir(self):
        self.age += 1
    def nommer(self, nom):
        self.prenom = nom
mon_animal = Animal()
print("Âge initial :", mon_animal.age)
mon_animal.vieillir()
print("Âge après avoir vieilli :", mon_animal.age)
mon_animal.nommer("Rex")
print("Nom de l'animal :", mon_animal.prenom)
