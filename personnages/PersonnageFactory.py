from arme.Bouclier import Bouclier
from arme.Epee import Epee
from arme.Gourdin import Gourdin
from item.Nourriture import Nourriture
from personnages.Heros import Heros
from personnages.Monstre import Monstre
from zone import Zone
from equipes.EquipeHeros import EquipeHeros
from equipes.EquipeMonstres import EquipeMonstres
from cimetiere.Cimetiere import Cimetiere


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

"""
factory = PersonnageFactory()
zone = Zone()
Cimetiere = Cimetiere()

equipe_heros = EquipeHeros("Heros")
equipe_monstres = EquipeMonstres("Monstres")
epee1 = factory.creer_arme("Excalibur", 15, 100, 2000, "Epee")
gourdin1 = factory.creer_arme("L'abattoir", 20, 80, 3000, "Gourdin")
nourriture1 = factory.creer_nourriture("pomme", 10, 5)
bouclier1 = factory.creer_bouclier("Durnvall", 5, 5)
arthur = factory.creer_personnage("Heros", "Arthur", 100, 100, 5, [epee1, gourdin1, nourriture1], arme_equipee=epee1)
grum = factory.creer_personnage("Monstre", "Grum", 120,42, 10, [epee1, gourdin1, nourriture1], arme_equipee=gourdin1, bouclier_equipe=bouclier1)

equipe_heros.ajouter_membre(arthur)
equipe_monstres.ajouter_membre(grum)

arthur.afficher_stats()
grum.afficher_stats()
Zone.placer_personnage(zone,arthur)
Zone.placer_personnage(zone,grum)
Zone.afficher_zone(zone)
EquipeHeros.retirer_mort(Cimetiere)
"""










