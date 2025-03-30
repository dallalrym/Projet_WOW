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
        self.heros = []
        self.monstres = []

    def preparation(self):
        # Creation des equipes
        equipe_heros = EquipeHeros("Heros")
        equipe_monstres = EquipeMonstres("Monstres")

        # Création armes et nourriture
        epee1 = PersonnageFactory.creer_arme("Excalibur", 15, 100, 2000, "Epee")
        gourdin1 = PersonnageFactory.creer_arme("L'abattoir", 20, 80, 3000, "Gourdin")
        nourriture1 = PersonnageFactory.creer_nourriture("pomme", 10, 5)
        bouclier1 = PersonnageFactory.creer_bouclier("Durnvall", 5, 5)

        # Creation des personnages
        heros1 = PersonnageFactory.creer_personnage("Heros", "Arthur", 100, 100, 5, [epee1, gourdin1, nourriture1], arme_equipee=epee1)
        monstre1 = PersonnageFactory.creer_personnage("Monstre", "Grum", 120,42, 10, [epee1, gourdin1, nourriture1], arme_equipee=gourdin1, bouclier_equipe=bouclier1)

        # Ajout des perso aux equipes
        equipe_heros.ajouter_membre(heros1)
        equipe_monstres.ajouter_membre(monstre1)

        # Ajouter les équipes au jeu
        self.heros = equipe_heros.membres
        self.monstres = equipe_monstres.membres

        # Affiche stats perso
        monstre1.afficher_stats()
        heros1.afficher_stats()

    def placer_personnages(self):
        personnages = self.heros + self.monstres
        random.shuffle(personnages)  # Mélanger pour éviter les biais de placement

        for personnage in personnages:
            while not self.zone.placer_personnage(personnage):
            # Si la position est déjà occupée, trouver une nouvelle position aléatoire
                personnage.x = random.randint(0, 9)
                personnage.y = random.randint(0, 9)

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

    def tour_de_jeu(self):
        # Mélanger les personnages pour varier l'ordre des actions
        personnages = self.heros + self.monstres
        random.shuffle(personnages)

        for personnage in personnages:
            if personnage.points_de_vie <= 0:
                continue  # Passe au personnage suivant si celui-ci est mort

            # Choisir une action aléatoire
            action = random.choice(["se_deplacer", "dormir", "attaquer", "fuir"])

            if action == "se_deplacer":
                direction = random.choice(["Nord", "Sud", "Est", "Ouest"])
                personnage.deplacement(direction)

            elif action == "dormir":
                personnage.dormir()

            elif action == "attaquer":
                cible = self.trouver_cible(personnage)
                if cible:
                    personnage.attaquer(cible)

            elif action == "fuir":
                personnage.fuir()

        # Ajout des personnages morts dans le cimetière en les retirant de leur équipe
        """EquipeHeros.retirer_mort(Cimetiere)
        EquipeMonstres.retirer_mort(Cimetiere)
        """

        # Afficher la zone après chaque tour
        """
        Zone.afficher_zone(Zone)
        """

    def demarrer(self):
    # Préparer le jeu en créant les équipes et en plaçant les personnages
        self.preparation()

    # Boucle principale du jeu
        while self.heros and self.monstres:
            self.tour_de_jeu()

    # Déterminer le gagnant
        if not self.heros:
            print("Les monstres ont gagné !")
        else:
            print("Les héros ont gagné !")

