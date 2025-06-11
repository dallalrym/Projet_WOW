from arme.Bouclier import Bouclier
from arme.Epee import Epee
from arme.Gourdin import Gourdin
from item.Nourriture import Nourriture
from personnages.Heros import Heros
from personnages.Monstre import Monstre


class PersonnageFactory:
    @staticmethod
    def creer_personnage(type_personnage, nom, points_de_vie, endu, force, sacoche, arme_equipee=None, bouclier_equipe=None):
        if type_personnage == "Heros":
            return Heros(nom, points_de_vie, endu, force, sacoche, arme_equipee, bouclier_equipe)
        elif type_personnage == "Monstre":
            return Monstre(nom, points_de_vie, endu, force, sacoche, arme_equipee, bouclier_equipe)
        else:
            raise ValueError("Type de personnage inconnu")

    @staticmethod
    def creer_arme(nom, degats, longueur, poids, type_arme):
        if type_arme == "Epee":
            epee = Epee(nom, degats, longueur, poids, type_arme)
            print(epee)
            return epee
        elif type_arme == "Gourdin":
            gourdin = Gourdin(nom, degats, longueur, poids, type_arme)
            print(gourdin)
            return gourdin
        else:
            raise ValueError("Type d'arme inconnue")

    @staticmethod
    def creer_bouclier(nom, encaissement_degats, poids):
        bouclier = Bouclier(nom, encaissement_degats, poids)
        print(bouclier)
        return bouclier

    @staticmethod
    def creer_nourriture(nom, recup, poids):
        nourriture = Nourriture(nom, recup, poids)
        print(nourriture)
        return nourriture









