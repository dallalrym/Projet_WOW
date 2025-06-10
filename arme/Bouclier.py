class Bouclier:
    def __init__(self, nom, encaissement_degats, poids):
        self.nom = nom
        self.encaissement_degats = encaissement_degats
        self.poids = poids

    def __str__(self):
        return f"Bouclier({self.nom}, dégats encaissés: {self.encaissement_degats}, Poids: {self.poids}g)"