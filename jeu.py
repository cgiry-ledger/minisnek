"""
Interface graphique du jeu Snake
"""
from tkinter import Tk, Canvas, Button
from tkinter import LEFT, RIGHT, TOP, BOTH

from config import TAILLE_PLATEAU, TAILLE_CASE, BOUTON_DROITE, BOUTON_HAUT, BOUTON_BAS, BOUTON_GAUCHE, TEMPS_ENTRE_TOUR
from code import Plateau, Coordonees


class Jeu:
    """
    Contient la fenêtre de l'interface graphique, le canvas pour dessiner le jeu et le plateau de jeu
    """
    fenetre: Tk
    canvas: Canvas
    plateau: Plateau

    def __init__(self):
        """
        Initialise une nouvelle fenêtre de jeu
        """
        self.plateau = None

        self.fenetre = Tk()
        taille_plateau = TAILLE_PLATEAU * TAILLE_CASE

        # Initialize canvas
        self.canvas = Canvas(
            self.fenetre,
            width=taille_plateau + TAILLE_CASE,
            height=taille_plateau + TAILLE_CASE,
            bg='black'
        )

        # Initialize Buttons
        start_button = Button(self.fenetre, text='Lancer', command=self.nouveau_jeu)
        quit_button = Button(self.fenetre, text='Quitter', command=self.fenetre.quit)

        # Pack GUI parts
        self.canvas.pack(side=TOP)
        start_button.pack(side=LEFT, fill=BOTH, expand=True)
        quit_button.pack(side=RIGHT, fill=BOTH, expand=True)

        # Set up buttons
        self.fenetre.bind(f'<{BOUTON_GAUCHE}>', self.mouvement_gauche)
        self.fenetre.bind(f'<{BOUTON_BAS}>', self.mouvement_bas)
        self.fenetre.bind(f'<{BOUTON_DROITE}>', self.mouvement_droite)
        self.fenetre.bind(f'<{BOUTON_HAUT}>', self.mouvement_haut)

        self.fenetre.mainloop()

    def nouveau_jeu(self):
        """
        Lance une nouvelle partie
        """
        if self.plateau is None or self.plateau.game_over:
            print('Nouvelle partie!')
            self.plateau = Plateau()
            self.fenetre.after(TEMPS_ENTRE_TOUR, self.boucle_jeu)
        else:
            print('Partie en cours')

    def boucle_jeu(self):
        """
        Dessine le jeu, fait progresser d'un tour et programme le prochain tour
        après TEMPS_ENTRE_TOUR
        :return:
        """
        self.plateau.tour()
        self.dessin_jeu()
        if not self.plateau.game_over:
            self.fenetre.after(TEMPS_ENTRE_TOUR, self.boucle_jeu)

    def dessin_jeu(self):
        """
        Dessine le plateau de jeu
        :return:
        """
        self.canvas.delete('all')

        # Dessine la pomme
        self.dessin_coordonnees(self.plateau.pomme, 'red')

        # Dessine le corps du Snake (sans la tête)
        for part in self.plateau.snake.corps[1:]:
            self.dessin_coordonnees(part, 'gray')

        # Dessine la tête du Snake
        self.dessin_coordonnees(self.plateau.snake.tete, 'white')

    def dessin_coordonnees(self, coordonnees: Coordonees, color: str):
        """
        Dessine un objet Coordonnees avec la couleur donnée
        :param coordonnees: la coordonée à dessiner
        :type coordonnees: Coordonees
        :param color: La couleur de la Coordonnée à dessiner
        :type color: str
        """
        x = coordonnees.x * TAILLE_CASE
        y = coordonnees.y * TAILLE_CASE
        self.canvas.create_rectangle(
            x, y,
            x + TAILLE_CASE, y + TAILLE_CASE,
            fill=color
        )

    def mouvement_haut(self, callback=None):
        """
        Change la direction du prochain tour du Snake vers le haut
        """
        if self.plateau.snake.direction != 'bas':
            self.plateau.prochaine_direction = 'haut'

    def mouvement_gauche(self, callback=None):
        """
        Change la direction du prochain tour du Snake vers la gauche
        """
        if self.plateau.snake.direction != 'droite':
            self.plateau.prochaine_direction = 'gauche'

    def mouvement_bas(self, callback=None):
        """
        Change la direction du prochain tour du Snake vers le bas
        """
        if self.plateau.snake.direction != 'haut':
            self.plateau.prochaine_direction = 'bas'

    def mouvement_droite(self, callback=None):
        """
        Change la direction du prochain tour du Snake vers la droite
        """
        if self.plateau.snake.direction != 'gauche':
            self.plateau.prochaine_direction = 'droite'


if __name__ == '__main__':
    Jeu()
