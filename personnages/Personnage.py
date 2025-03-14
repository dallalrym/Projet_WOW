import random

from item.Nourriture import Nourriture

class Personnage:
    def __init__(self, nom, points_de_vie, arme, endu, sacoche, arme_equipee=None, bouclier_equipe=None):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.arme = arme
        self.endu = endu
        self.sacoche = sacoche
        self.arme_equipee = arme_equipee
        self.bouclier_equipe = bouclier_equipe

    # Méthode attaque
    def attaquer(self, adversaire):
        # Si perso n'a plus d'endurance il ne peut pas attaquer ni se défendre
        if self.endu <= 0:
            print(f"{self.nom} n'a plus d'endurance. Il ne peut plus attaquer !")
            return

        degats = self.arme.degats
        adversaire.recevoir_degats(degats)
        print(f"{self.nom} attaque {adversaire.nom} avec {self.arme.nom} et inflige {degats} degats.")

        # Calcul de l'endurance consommée pour attaquer
        perte_endurance = (self.arme_equipee.longueur * self.arme_equipee.poids) / 10000
        self.endu -= perte_endurance
        print(f"Endurance restante de {self.nom} : {self.endu}")

    # Méthode recevoir dégats
    def recevoir_degats(self, degats):
        self.points_de_vie -= degats
        if self.points_de_vie <= 0:
            print(f"{self.nom} est vaincu ! Il rejoint le cimetière !")
        else:
            print(f"{self.nom} recoit {degats} degats. Points de vie restants : {self.points_de_vie}")

    # Méthode défendre
    def defendre(self, degats_recus):
        if not self.bouclier_equipe:
            self.points_de_vie -= degats_recus
            print(f"{self.nom} n'a pas de bouclier. Il subit {degats_recus} dégats !")
            return

        # Calcul de la réduction des dégâts avec bouclier
        reduction = self.bouclier_equipe.encaissement_degats
        degats_final = max(0, degats_recus - reduction)

        # Application des dégâts
        self.points_de_vie -= degats_final
        print(f"{self.nom} utilise {self.bouclier_equipe.nom} et réduit les dégâts de {reduction}. Il subit {degats_final} dégâts.")

        # Calcul de l'endurance consommée pour se défendre
        perte_endurance = self.bouclier_equipe.poids / 1000
        self.endu -= perte_endurance
        print(f"Endurance restante de {self.nom} : {self.endu}")

    # Méthode manger
    def manger(self):
        nourriture_dispo = [item for item in self.sacoche if isinstance(item, Nourriture)]
        if not nourriture_dispo:
            print(f"{self.nom} n'a pas de nourriture dans son inventaire. Il ne récupère pas d'endurance !")
            return

        # Choisi un objet nourriture au hasard, calcul les points d'endurance à ajouter et supprime l'objet de la sacoche
        nourriture = random.choice(nourriture_dispo)
        self.endu += nourriture.recup
        self.sacoche.remove(nourriture)

    # Méthode équiper un bouclier
    def equiper_bouclier(self, nouveau_bouclier):
        if nouveau_bouclier in self.sacoche:
            self.bouclier_equipe = nouveau_bouclier
            print(f"{self.nom} est maintenant équipé du bouclier : {nouveau_bouclier.nom}.")
        else:
            print(f"{nouveau_bouclier.nom} n'est pas dans la sacoche de {self.nom}.")

    # Méthode équiper une arme
    def equiper_arme(self, nouvelle_arme):
        if nouvelle_arme in self.sacoche:
            self.arme_equipee = nouvelle_arme
            print(f"{self.nom} est maintenant équipé de l'arme : {nouvelle_arme.nom}.")
        else:
            print(f"{nouvelle_arme.nom} n'est pas dans la sacoche de {self.nom}.")

    # Getter stats du perso
    def afficher_stats(self):
        print(f"\n{self.nom} stats :")
        print(f"Points de vie : {self.points_de_vie}")
        print(f"Endurance : {self.endu}")
        print(f"Arme équipée : {self.arme_equipee.nom if self.arme_equipee else 'Aucune'}")
        print(f"Bouclier équipé : {self.bouclier_equipe.nom if self.bouclier_equipe else 'Aucun'}")
        print(f"Sacoche : {[item.nom for item in self.sacoche]}")