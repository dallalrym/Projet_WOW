from epee import Epee
from gourdin import Gourdin

class FabriqueArme:
    @staticmethod
    def creer_arme(type_arme, nom, degats, longueur, poids):
        if type_arme == "epee":
            return Epee(nom, degats, longueur, poids)
        elif type_arme == "gourdin":
            return Gourdin(nom, degats, longueur, poids)
        else:
            raise ValueError("Type d'arme inconnu")