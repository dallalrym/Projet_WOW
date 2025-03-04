class Armes:
    def __init__(self, nom, longueur, poids, degats):
        self.nom = nom
        self.longueur = longueur
        self.poids = poids
        self.degats = degats

    def attaquer(self):
        return self.degats
