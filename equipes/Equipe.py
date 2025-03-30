class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.membres = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def est_vaincue(self):
        return all(membre.points_de_vie <= 0 for membre in self.membres)

    def afficher_membres(self):
        for membre in self.membres:
            print(f" Membres équipe {self.nom} :")
            print(f" - {membre.nom}")

    def retirer_mort(self, cimetiere):
        for p in self.membres:
            if p.est_mort():
                cimetiere.ajouter_mort(p)
                self.membres.remove(p)