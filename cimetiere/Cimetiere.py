class Cimetiere:
    def __init__(self):
        self.morts = []

    def ajouter_mort(self, personnage):
        self.morts.append(personnage)

    def afficher_morts(self):
        if not self.morts:
            print("Le cimetière est vide.")
        else:
            print("Personnages morts :")
            for mort in self.morts:
                print(f"- {mort.nom}")