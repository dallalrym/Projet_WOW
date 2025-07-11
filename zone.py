class Zone:
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Zone, cls).__new__(cls)
            # Initialisation de l'instance
            cls._instance.grille = [[None for _ in range(10)] for _ in range(10)]
        return cls._instance
    
    def placer_personnage(self, personnage):
        # Nettoyer toute ancienne position du personnage
        for x in range(10):
            for y in range(10):
                if self.grille[x][y] == personnage:
                    self.grille[x][y] = None

        if self.grille[personnage.x][personnage.y] is None:
            self.grille[personnage.x][personnage.y] = personnage
            return True
        return False



    def deplacer_personnage(self, personnage, nouvelle_x, nouvelle_y):
        if 0 <= nouvelle_x < 10 and 0 <= nouvelle_y < 10 and self.grille[nouvelle_x][nouvelle_y] is None:
            self.grille[personnage.x][personnage.y] = None
            personnage.x = nouvelle_x
            personnage.y = nouvelle_y
            self.grille[nouvelle_x][nouvelle_y] = personnage
            return True
        return False

    def afficher_zone(self):
        for y in range(9, -1, -1):
            ligne = ""
            for x in range(10):
                if self.grille[x][y] is None:
                    ligne += "[ ] "
                else:
                    ligne += f"[{self.grille[x][y].nom[0]}] "
            print(ligne)
        print("\n")

    # Supprime le personnage de la grille 
    def retirer_personnage(self, personnage):
        if 0 <= personnage.x < 10 and 0 <= personnage.y < 10:
            if self.grille[personnage.x][personnage.y] == personnage:
                self.grille[personnage.x][personnage.y] = None
