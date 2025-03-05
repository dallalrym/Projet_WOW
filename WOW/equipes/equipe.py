class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.membres = []

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def est_vaincue(self):
        return all(membre.points_de_vie <= 0 for membre in self.membres)