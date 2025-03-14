from personnages.heros import Heros
from personnages.monstre import Monstre
from armes.epee import Epee
from armes.gourdin import Gourdin
from armes.bouclier import Bouclier
from personnages.nourriture import Nourriture

class PersonnageFactory:
    def creer_personnage(self, type_personnage, nom, points_de_vie, endurance, type_arme, type_bouclier=None, nourriture=[]):
        arme = self.creer_arme(type_arme)
        bouclier = self.creer_bouclier(type_bouclier) if type_bouclier else None
        sacoche = [self.creer_nourriture(item) for item in nourriture]

        if type_personnage == "Heros":
            return Heros(nom, points_de_vie, endurance, arme, bouclier, sacoche)
        elif type_personnage == "Monstre":
            return Monstre(nom, points_de_vie, endurance, arme, bouclier, sacoche)
        else:
            raise ValueError("Type de personnage inconnu")

    def creer_arme(self, type_arme):
        if type_arme == "Epee":
            return Epee("Excalibur", 15, 100, 2000)
        elif type_arme == "Gourdin":
            return Gourdin("L'abattoir", 20, 80, 3000)
        else:
            raise ValueError("Type d'arme inconnue")

    def creer_bouclier(self, type_bouclier):
        if type_bouclier == "Durnval":
            return Bouclier("Durnval", 10, 2500)
        return None

    def creer_nourriture(self, type_nourriture):
        if type_nourriture == "Pomme":
            return Nourriture("Pomme", 10, 200)
        elif type_nourriture == "Raisin":
            return Nourriture("Raisin", 5, 100)
        else:
            raise ValueError("Type de nourriture inconnu")
