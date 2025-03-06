class Personnage:
    def __init__(self, nom, points_de_vie, arme):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.arme = arme

    def attaquer(self, adversaire):
        degats = self.arme.degats
        adversaire.recevoir_degats(degats)
        print(f"{self.nom} attaque {adversaire.nom} avec {self.arme.nom} et inflige {degats} degats.")

    def recevoir_degats(self, degats):
        self.points_de_vie -= degats
        if self.points_de_vie <= 0:
            print(f"{self.nom} est vaincu ! Il rejoint le cimetière !")
        else:
            print(f"{self.nom} recoit {degats} degats. Points de vie restants : {self.points_de_vie}")