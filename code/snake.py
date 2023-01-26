"""
Fichier contenant la classe Snake
"""
from random import choice

from code import Coordonees


class Snake:
    """
    Le Snake
    Représenté par une liste de coordonnées dont la première est la tête du Snake
    La direction est celle vers laquelle le snake bouge
    """
    corps: list[Coordonees]
    direction: str

    def __init__(self):
        """
        Initialise un Snake
        """
        # Initialise la tête du Snake de manière aléatoire
        tete_snake = Coordonees()

        # Initialise le corps du snake
        self.corps = []
        self.corps.append(tete_snake)

        # Génère une direction initiale de manière aléatoire
        self.direction = choice(['haut', 'gauche', 'bas', 'droite'])

    @property
    def tete(self) -> Coordonees:
        """
        Retourne le premier élément du corps du Snake
        :return Coordonees: la tête du Snake
        """
        return self.corps[0]
