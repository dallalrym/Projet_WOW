from personnages.personnage import Personnage

class Monstre(Personnage):
    def __init__(self, nom, points_de_vie, arme):
        super().__init__(nom, points_de_vie, arme)