class Nourriture:
    def __init__(self, nom, recup, poids):
        self.nom = nom
        self.recup = recup
        self.poids = poids

    def __str__(self):
        return f"Nourriture({self.nom}, Récup: {self.recup}, Poids: {self.poids}g)"