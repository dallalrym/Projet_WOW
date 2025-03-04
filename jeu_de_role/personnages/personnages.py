from armes import armes

class Personnages:
    def __init__(self, nom, pv, arme):
        self.nom = nom
        self.pv = pv
        self.arme = arme

    """Personnage vivant ou pas"""
    def est_vivant(self):
        return self.pv > 0

    """Attaque un adversaire"""
    def attack(self, cible):
        if self.est_vivant():
            degats = self.arme.attaquer()
            print(f"{self.nom} attaque {cible.nom} avec {self.arme.nom} et inflige {degats} points de dégâts!")
            cible.subir_degats(degats)

    """Subi les dégats"""
    def subir_degats(self, degats):
        self.pv -= degats
        print(f"{self.nom} reçoit {degats} points de dégâts! (PV restants: {self.pv})")