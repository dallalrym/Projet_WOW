class Arme:
    def __init__(self, nom, degats, longueur, poids, type_arme):
        self.nom = nom
        self.degats = degats
        self.longueur = longueur
        self.poids = poids
        self.type_arme = type_arme

    def __str__(self):
        return f"Arme({self.nom}, dégats: {self.degats}, longueur: {self.longueur}, poids: {self.poids}, type d'arme: {self.type_arme})"