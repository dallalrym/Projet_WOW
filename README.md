# 🧙‍♂️ Jeu de rôle - WOW
Ce projet est une simulation de jeu de rôles en tour par tour, inspiré de mécaniques classiques (RPG). Nous avons choisi de le développer en Python. Il met en scène 2 équipes (héros et monstres) évoluant sur une carte en 2D.

## Fonctionnalités principales

### Carte de jeu

Grille 10x10 représentant l'univers du jeu.

#### Personnages
Héros ou Monstres avec :

- Points de vie (PV) et endurance (PE) avec valeurs max et actuelles.
- Force, inventaire, armes et boucliers équipés
- Coordonnées (X, Y)

#### Actions disponibles

- Se déplacer (Nord, Sud, Est, Ouest) / Coût en endurance basé sur force/poids
- Dormir / Régénère 1 PV et 2 PE par tour
- Fuir / Déplacement d'urgence de 2 cases (si assez d'endurance)
- Attaquer / Se Défendre / Attaques dépendant de l'équipement et de la position

#### Combat

- Seul un personnage adjacent peut être attaqué
- Le défenseur réagit immédiatement à l'attaque (si possible)
- Les combats peuvent se conclure par la mort ou la fuite

#### Conditions de victoire

L'équipe perdante est celle dont tous les membres sont morts

## 🗺️ Déroulement du jeu

1) Création de 2 équipes égales : une de héros, une de monstres
2) Chaque personnage est équipé (armes, boucliers, objets) et positionné aléatoirement sur la carte (cases non partagées)
3) A chaque tour :
   - Une action est choisie aléatoirement pour chaque personnage
   - Si une attaque est possible (personnage adjacent), elle a lieu
   - Le jeu continue jusqu'à la défaite d'une équipe

## 🎮 Lancement du jeu

1) Cloner le projet et vérifier que vous vous trouvez dans la branche main en faisant git branch
   ```bash
   git clone https://github.com/dallalrym/Projet_WOW.git
   cd projet_wow
   git branch
   ```
   
2) Installer Python s'il n'est pas déjà installer :
   L'installer depuis le Microsoft Store (Prioriser cette méthode) en allant sur ce lien : https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=fr-fr&gl=FR&ocid=pdpshare

   ou bien en le téléchargent ici : https://www.python.org/downloads/

3) Ouvrez un invite de commande à la racine du projet puis tapez cette commande :
   ```bash
   python main.py
   ```
