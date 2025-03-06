from personnages.Personnage import Personnage

class Heros(Personnage):
    def __init__(self, nom, points_de_vie, arme):
        super().__init__(nom, points_de_vie, arme)