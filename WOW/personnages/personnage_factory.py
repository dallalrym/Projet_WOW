from personnages.heros import Heros
from personnages.monstre import Monstre
from armes.epee import Epee
from armes.gourdin import Gourdin

class PersonnageFactory:
    def creer_personnage(self, type_personnage, nom, points_de_vie, type_arme):
        arme = self.creer_arme(type_arme)
        if type_personnage == "Heros":
            return Heros(nom, points_de_vie, arme)
        elif type_personnage == "Monstre":
            return Monstre(nom, points_de_vie, arme)
        else:
            raise ValueError("Type de personnage inconnu")

    def creer_arme(self, type_arme):
        if type_arme == "Epee":
            return Epee("Excalibur", 15, 100, 2000)
        elif type_arme == "Gourdin":
            return Gourdin("L'abattoir", 20, 80, 3000)
        else:
            raise ValueError("Type d'arme inconnue")