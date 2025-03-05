import random
from personnages.personnage_factory import PersonnageFactory
from equipes.equipe_heros import EquipeHeros
from equipes.equipe_monstres import EquipeMonstres
from cimetiere.cimetiere import Cimetiere

def main():
    # Creation de la factory
    factory = PersonnageFactory()

    # Creation des equipes
    equipe_heros = EquipeHeros("Heros")
    equipe_monstres = EquipeMonstres("Monstres")

    # Creation des personnages 
    heros1 = factory.creer_personnage("Heros", "Arthur", 100, "Epee")
    monstre1 = factory.creer_personnage("Monstre", "Grum", 120, "Gourdin")

    # Ajout des perso aux equipes
    equipe_heros.ajouter_membre(heros1)
    equipe_monstres.ajouter_membre(monstre1)


    # Deroulement du jeu
    while not equipe_heros.est_vaincue() and not equipe_monstres.est_vaincue():
        # Choisi un attaquant au hasard parmis les 2 équipes
        attaquant = random.choice(equipe_heros.membres + equipe_monstres.membres)
        # Choisi un adversaire au hasard parmis les 2 équipes
        adversaire = random.choice(equipe_heros.membres + equipe_monstres.membres)
        # Vérifie si l'adversaire n'est pas le même perso que l'attaquant
        while attaquant == adversaire:
            adversaire = random.choice(equipe_heros.membres + equipe_monstres.membres)

        attaquant.attaquer(adversaire)
        # Contre attaque de l'adversaire si il est toujours en vie
        if adversaire.points_de_vie > 0:
            adversaire.attaquer(attaquant)

    # Determination du vainqueur
    if equipe_heros.est_vaincue():
        print("L'equipe des monstres a gagne!")
    else:
        print("L'equipe des heros a gagne!")

if __name__ == "__main__":
    main()