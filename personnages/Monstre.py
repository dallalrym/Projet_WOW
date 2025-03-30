from personnages.Personnage import Personnage

class Monstre(Personnage):
    def __init__(self, nom, points_de_vie, endu, force, sacoche, arme_equipee=None, bouclier_equipe=None):
        super().__init__(nom, points_de_vie, endu, force, sacoche, arme_equipee, bouclier_equipe)