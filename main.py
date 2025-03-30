import random

from equipes.EquipeHeros import EquipeHeros
from equipes.EquipeMonstres import EquipeMonstres
from personnages.PersonnageFactory import PersonnageFactory
from cimetiere.Cimetiere import Cimetiere


def main():
    # Creation de la factory
    factory = PersonnageFactory()

    # Création du cimetière
    cimetiere = Cimetiere()

    # Creation des equipes
    equipe_heros = EquipeHeros("Heros")
    equipe_monstres = EquipeMonstres("Monstres")

    # Création armes et nourriture
    epee1 = factory.creer_arme("Excalibur", 15, 100, 2000, "Epee")
    gourdin1 = factory.creer_arme("L'abattoir", 20, 80, 3000, "Gourdin")
    nourriture1 = factory.creer_nourriture("pomme", 10, 5)
    bouclier1 = factory.creer_bouclier("Durnvall", 5, 5)

    # Creation des personnages
    heros1 = factory.creer_personnage("Heros", "Arthur", 100,  420, [epee1, gourdin1, nourriture1], arme_equipee=epee1)
    monstre1 = factory.creer_personnage("Monstre", "Grum", 120,  300, [epee1, gourdin1, nourriture1], arme_equipee=gourdin1, bouclier_equipe=bouclier1)

    # Ajout des perso aux equipes
    equipe_heros.ajouter_membre(heros1)
    equipe_monstres.ajouter_membre(monstre1)


    # Deroulement du jeu
    while not equipe_heros.est_vaincue() and not equipe_monstres.est_vaincue():
        # Choix aléatoire de celui qui fait la première action
        premier = random.choice(equipe_heros.membres + equipe_monstres.membres)

        # Choix aléatoire parmis les 2 équipes
        deuxieme = random.choice(equipe_heros.membres + equipe_monstres.membres)

        # Vérifie si l'adversaire n'est pas le même perso que l'attaquant
        while premier == deuxieme:
            deuxieme = random.choice(equipe_heros.membres + equipe_monstres.membres)


        # Choix aléatoire de l'action de J1
        actionJ1 = random.choice(["attaquer", "manger"])

        # Si J1 attaque J2, J2 peut défendre ou manger
        if actionJ1 == "attaquer":
            premier.attaquer(deuxieme)
            actionJ2 = random.choice(["manger", "defendre"])
            if actionJ2 == "defendre":
                deuxieme.defendre(premier.arme_equipee.degats)
            else:
                deuxieme.manger()

        # Si J1 mange, J2 peut attaquer J1 ou bien manger
        else:
            premier.manger()
            actionJ2 = random.choice(["manger", "attaquer"])
            if actionJ2 == "attaquer":
                deuxieme.attaquer(premier)
            else:
                deuxieme.manger()

        # Ajout des personnages morts dans le cimetière en les retirant de leur équipe
        equipe_heros.retirer_mort(cimetiere)
        equipe_monstres.retirer_mort(cimetiere)

    # Determination du vainqueur
    if equipe_heros.est_vaincue():
        print("L'equipe des monstres a gagne!")
        cimetiere.afficher_morts()
        equipe_heros.afficher_membres()
        equipe_monstres.afficher_membres()
    else:
        print("L'equipe des heros a gagne!")
        cimetiere.afficher_morts()
        equipe_monstres.afficher_membres()
        equipe_heros.afficher_membres()

if __name__ == "__main__":
    main()