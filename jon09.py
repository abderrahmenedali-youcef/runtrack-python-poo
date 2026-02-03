class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)
    def afficher(self):
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}, Prix TTC: {self.CalculerPrixTTC()}"
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom
    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix
    def getNom(self):
        return self.nom
    def getPrixHT(self):
        return self.prixHT
    def getTVA(self):
        return self.TVA
produit1 = Produit("Ordinateur", 1000, 0.20)
produit2 = Produit("Téléphone", 500, 0.20)
produit3 = Produit("Livre", 30, 0.05)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

print("\nCalcul des prix TTC :")
print(produit1.getNom(), "->", produit1.CalculerPrixTTC())
print(produit2.getNom(), "->", produit2.CalculerPrixTTC())
print(produit3.getNom(), "->", produit3.CalculerPrixTTC())

produit1.modifierNom("PC Portable")
produit1.modifierPrix(1200)

produit2.modifierNom("Smartphone")
produit2.modifierPrix(650)

produit3.modifierNom("Roman")
produit3.modifierPrix(35)
print("\nAprès modification :")
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())