import random

from equipes.EquipeHeros import EquipeHeros
from equipes.EquipeMonstres import EquipeMonstres
from personnages.PersonnageFactory import PersonnageFactory
from cimetiere.Cimetiere import Cimetiere
from zone import Zone

class Jeu:
    def __init__(self):
        self.zone = Zone()
        self.factory = PersonnageFactory()
        self.cimetiere = Cimetiere() 

    def preparation(self):
        # Creation des equipes
        equipe_heros = EquipeHeros("Heros")
        equipe_monstres = EquipeMonstres("Monstres")

        # Création armes et nourriture
        epee1 = PersonnageFactory.creer_arme("Excalibur", 15, 30, 2000, "Epee")
        gourdin1 = PersonnageFactory.creer_arme("L'abattoir", 20, 50, 3000, "Gourdin")
        nourriture1 = PersonnageFactory.creer_nourriture("pomme", 10, 5)
        bouclier1 = PersonnageFactory.creer_bouclier("Durnvall", 5, 5)

        # Creation des personnages (héros)
        heros1 = PersonnageFactory.creer_personnage("Heros", "Arthur", 500, 100, 5, [epee1, gourdin1, nourriture1], arme_equipee=epee1)
        
        # Création des personnages (Monstres)
        monstre1 = PersonnageFactory.creer_personnage("Monstre", "Grum", 120, 42, 10, [epee1, gourdin1, nourriture1], arme_equipee=gourdin1, bouclier_equipe=bouclier1)

        # Ajout des perso aux equipes
        equipe_heros.ajouter_membre(heros1)
        equipe_monstres.ajouter_membre(monstre1)

        # Ajouter les équipes au jeu
        self.heros = equipe_heros.membres
        self.monstres = equipe_monstres.membres

        # Placer les personnages sur la Zone
        self.zone.placer_personnage(heros1)
        self.zone.placer_personnage(monstre1)
        

    def trouver_cible(self, attaquant):
        # Trouver une cible adjacente
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Ignorer la case actuelle de l'attaquant
                x, y = attaquant.x + dx, attaquant.y + dy
                if 0 <= x < 10 and 0 <= y < 10:
                    cible = self.zone.grille[x][y]
                    if cible and cible != attaquant:
                        return cible
        return None

    def nettoyer_equipes(self):
        # Nettoyer les héros morts
        vivants_heros = []
        for h in self.heros:
            if h.est_mort():
                self.cimetiere.ajouter_mort(h)
                self.zone.retirer_personnage(h)
            else:
                vivants_heros.append(h)
        self.heros = vivants_heros

        # Nettoyer les monstres morts
        vivants_monstres = []
        for m in self.monstres:
            if m.est_mort():
                self.cimetiere.ajouter_mort(m)
                self.zone.retirer_personnage(m)
            else:
                vivants_monstres.append(m)
        self.monstres = vivants_monstres

    def tour_de_jeu(self):
        # Mélanger les personnages pour varier l'ordre des actions
        personnages = self.heros + self.monstres
        random.shuffle(personnages)

        for personnage in personnages:
            print(f"--- {personnage.nom} commence son tour ---")
            print(f"PV : {personnage.points_de_vie}, Endurance : {personnage.endu}, Position : ({personnage.x}, {personnage.y})")
            if personnage.points_de_vie <= 0:
                continue  # Passe au personnage suivant si celui-ci est mort

            # Choisir une action aléatoire
            action = random.choice(["se_deplacer", "dormir", "attaquer", "fuir"])

            if action == "se_deplacer":
                print(f"{personnage.nom} tente de faire l'action : {action}")
                direction = random.choice(["Nord", "Sud", "Est", "Ouest"])
                result = personnage.deplacement(direction)
                if result:
                    nouvelle_x, nouvelle_y, endu_conso = result
                    if self.zone.deplacer_personnage(personnage, nouvelle_x, nouvelle_y):
                        personnage.endu -= endu_conso
                        print(f"{personnage.nom} se déplace vers {direction} et consomme {endu_conso:.4f} d'endurance. Endurance restante : {personnage.endu:.2f}")
                    else:
                        print(f"{personnage.nom} ne peut pas se déplacer vers {direction}, case occupée.")

            elif action == "dormir":
                print(f"{personnage.nom} tente de faire l'action : {action}")
                personnage.dormir()

            elif action == "attaquer":
                print(f"{personnage.nom} tente de faire l'action : {action}")
                cible = self.trouver_cible(personnage)
                if cible:
                    personnage.attaquer(cible)

            elif action == "fuir":
                print(f"{personnage.nom} tente de faire l'action : {action}")
                result = personnage.fuir()
                if result:
                    nx, ny, conso, direction = result
                    if self.zone.deplacer_personnage(personnage, nx, ny):
                        personnage.endu -= conso
                        print(f"{personnage.nom} fuit vers le {direction} et consomme {conso:.4f} d'endurance. Endurance restante : {personnage.endu:.2f}")
                    else:
                        print(f"{personnage.nom} ne peut pas fuir vers le {direction}, case occupée.")

        # Ajout des personnages morts dans le cimetière en les retirant de leur équipe et de la zone
        self.nettoyer_equipes()

        # Afficher la zone après chaque tour
        self.zone.afficher_zone()
        

    def demarrer(self):
    # Préparer le jeu en créant les équipes et en plaçant les personnages
        self.preparation()

    # Boucle principale du jeu
        while self.heros and self.monstres:
            self.tour_de_jeu()

    # Annonce le gagnant
        if not self.heros:
            print("Les monstres ont gagné !")
        else:
            print("Les héros ont gagné !")
