from arme.Bouclier import Bouclier
from arme.Epee import Epee
from arme.Gourdin import Gourdin
from item.Nourriture import Nourriture
from personnages.Heros import Heros
from personnages.Monstre import Monstre




class PersonnageFactory:
    @staticmethod
    def creer_personnage(type_personnage, nom, points_de_vie, endu, sacoche, arme_equipee=None, bouclier_equipe=None):
        if type_personnage == "Heros":
            return Heros(nom, points_de_vie, endu, sacoche, arme_equipee, bouclier_equipe)
        elif type_personnage == "Monstre":
            return Monstre(nom, points_de_vie, endu, sacoche, arme_equipee, bouclier_equipe)
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

"""
factory = PersonnageFactory()

equipe_heros = EquipeHeros("Heros")
equipe_monstres = EquipeMonstres("Monstres")
epee1 = factory.creer_arme("Excalibur", 15, 100, 2000, "Epee")
gourdin1 = factory.creer_arme("L'abattoir", 20, 80, 3000, "Gourdin")
nourriture1 = factory.creer_nourriture("pomme", 10, 5)
bouclier1 = factory.creer_bouclier("Durnvall", 5, 5)
arthur = factory.creer_personnage("Heros", "Arthur", 100, 100, [epee1, gourdin1, nourriture1], arme_equipee=epee1)
grum = factory.creer_personnage("Monstre", "Grum", 120,  42, [epee1, gourdin1, nourriture1], arme_equipee=gourdin1, bouclier_equipe=bouclier1)

equipe_heros.ajouter_membre(arthur)
equipe_monstres.ajouter_membre(grum)
arthur.attaquer(grum)
print(grum.points_de_vie)
grum.defendre(arthur.arme_equipee.degats)
print(grum.points_de_vie)
grum.manger()
print(grum.endu)

cimetiere.ajouter_mort(arthur)
cimetiere.afficher_morts()
equipe_heros.afficher_membres()
equipe_monstres.afficher_membres()
"""