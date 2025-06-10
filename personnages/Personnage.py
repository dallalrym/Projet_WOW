import random
from item.Nourriture import Nourriture

class Personnage:
    def __init__(self, nom, points_de_vie, endu, force, sacoche, arme_equipee=None, bouclier_equipe=None):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.pvmax = points_de_vie
        self.endu = endu
        self.endumax = endu
        self.force = force
        self.sacoche = sacoche
        self.arme_equipee = arme_equipee
        self.bouclier_equipe = bouclier_equipe
        self.x = random.randint(0, 9)
        self.y = random.randint(0, 9)

    # Méthode attaque
    def attaquer(self, adversaire):
        # Si perso n'a plus d'endurance il ne peut pas attaquer ni se défendre
        if self.endu <= 0:
            print(f"{self.nom} n'a plus d'endurance. Il ne peut plus attaquer !")
            return

        degats = self.arme_equipee.degats
        adversaire.recevoir_degats(degats)
        print(f"{self.nom} attaque {adversaire.nom} avec {self.arme_equipee.nom} et inflige {degats} degats.")

        # Calcul de l'endurance consommée pour attaquer
        perte_endurance = (self.arme_equipee.longueur * self.arme_equipee.poids) / ( 1000 * self.force)
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
        # Si perso n'a plus d'endurance il ne peut pas attaquer ni se défendre
        if self.endu <= 0 or self.points_de_vie <= 0:
            print(f"{self.nom} n'a plus d'endurance. Il ne peut plus défendre !")
            return

        if not self.bouclier_equipe:
            print(f"{self.nom} n'a pas de bouclier. Il subit {degats_recus} dégats !")
            return

        # Calcul de la réduction des dégâts avec bouclier
        reduction = self.bouclier_equipe.encaissement_degats
        degats_final = max(0, degats_recus - reduction)

        # Application des dégâts
        self.points_de_vie += reduction
        print(f"{self.nom} utilise {self.bouclier_equipe.nom} et réduit les dégâts de {reduction}. Il subit {degats_final} dégâts.")

        # Calcul de l'endurance consommée pour se défendre
        perte_endurance = self.bouclier_equipe.poids / ( 1000 * self.force)
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
        print(f"{self.nom} mange le/la {nourriture.nom}, il récupère {nourriture.recup} d'endurance ! Endurance restante : {self.endu}")

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
        print(f"Points de vie : {self.points_de_vie}/{self.pvmax}")
        print(f"Endurance : {self.endu}/{self.endumax}")
        print(f"Arme équipée : {self.arme_equipee.nom if self.arme_equipee else 'Aucune'}")
        print(f"Bouclier équipé : {self.bouclier_equipe.nom if self.bouclier_equipe else 'Aucun'}")
        print(f"Sacoche : {[item.nom for item in self.sacoche]}")
        print(f"Position : {self.x}, {self.y}")

    # Vérifie s'il est vivant
    def est_mort(self):
        return self.points_de_vie <= 0

    # Déplacement
    def deplacement(self, direction):
        deplacements = {
            "Nord": (0, 1),
            "Sud": (0, -1),
            "Est": (1, 0),
            "Ouest": (-1, 0)
        }

        if direction not in deplacements:
            print(f"Direction invalide : {direction}")
            return None

        dx, dy = deplacements[direction]
        nouvelle_x = self.x + dx
        nouvelle_y = self.y + dy

        if not (0 <= nouvelle_x < 10 and 0 <= nouvelle_y < 10):
            print(f"{self.nom} ne peut pas se déplacer vers {direction}, limite atteinte.")
            return None

        charge = self.arme_equipee.poids if self.arme_equipee else 0
        if self.bouclier_equipe:
            charge += self.bouclier_equipe.poids

        endu_conso = charge / (self.force * 1000)

        if self.endu < endu_conso:
            print(f"{self.nom} n'a pas assez d'endurance pour se déplacer.")
            return None

        return nouvelle_x, nouvelle_y, endu_conso
    
    # Dormir
    def dormir(self):
        self.points_de_vie = min(self.points_de_vie + 1, self.pvmax)
        self.endu = min(self.endu + 2, self.endumax)
        print(f"{self.nom} décide de dormir et récupère 1 pv et 2 points d'endurance  ! Endurance : {self.endu}/{self.endumax} | Pv : {self.points_de_vie}/{self.pvmax}")

    # Fuir
    def fuir(self):
        charge = self.arme_equipee.poids if self.arme_equipee else 0
        if self.bouclier_equipe:
            charge += self.bouclier_equipe.poids

        endu_conso = charge / (self.force * 1000)

        if self.endu < endu_conso:
            print(f"{self.nom} ne peut pas fuir car il n'a pas assez d'endurance !")
            return None

        # Déterminer la direction de fuite
        if self.y == 9:
            nouvelle_x, nouvelle_y = self.x, max(0, self.y - 2)
            direction = "Sud"
        elif self.y == 0:
            nouvelle_x, nouvelle_y = self.x, min(9, self.y + 2)
            direction = "Nord"
        elif self.x == 9:
            nouvelle_x, nouvelle_y = max(0, self.x - 2), self.y
            direction = "Ouest"
        elif self.x == 0:
            nouvelle_x, nouvelle_y = min(9, self.x + 2), self.y
            direction = "Est"
        else:
            # Fuite par défaut vers le Sud si possible
            nouvelle_x, nouvelle_y = self.x, max(0, self.y - 2)
            direction = "Sud"

        return nouvelle_x, nouvelle_y, endu_conso, direction
