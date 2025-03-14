from arme.Arme import Arme


class Epee(Arme):
    def __init__(self, nom, degats, longueur, poids, type_arme):
        super().__init__(nom, degats, longueur, poids, type_arme)