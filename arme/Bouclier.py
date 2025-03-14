class Bouclier:
    def __init__(self, nom, encaissemennt_degats, poids):
        self.nom = nom
        self.encaissemennt_degats = encaissemennt_degats
        self.poids = poids

    def __str__(self):
        return f"Bouclier({self.nom}, dégats encaissés: {self.encaissemennt_degats}, Poids: {self.poids}g)"