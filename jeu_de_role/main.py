import random
from personnages.heros import Heros
from personnages.monstre import Monstre
from personnages.emonstre import Emonstre
from personnages.eheros import Eheros
from armes.epee import Epee
from armes.gourdin import Gourdin




def main():

    # Création des armes
    epee = FabriqueArme.creer_arme("epee", "Excalibur", 10, 100, 1200)
    gourdin = FabriqueArme.creer_arme("gourdin", "L'Abattoir", 8, 80, 1500)

    # Création des personnages
    heros = FabriquePersonnage.creer_personnage("heros", "Arthur", 30, epee)
    monstre = FabriquePersonnage.creer_personnage("monstre", "Grum", 25, gourdin)

    # Combat
    while heros.est_vivant() and monstre.est_vivant():
        if random.choice([True, False]):
            heros.attaquer(monstre)
            if monstre.est_vivant():
                monstre.attaquer(heros)
        else:
            monstre.attaquer(heros)
            if heros.est_vivant():
                heros.attaquer(monstre)

    # Résultat
    if heros.est_vivant():
        print(f"{heros.nom} a gagné!")
    else:
        print(f"{monstre.nom} a gagné!")

if __name__ == "__main__":
    main()

