class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"
personne1 = Personne("john", "Doe")
personne2 = Personne("jean", "Dupind")
print(personne1.SePresenter())
print(personne2.SePresenter())