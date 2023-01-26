"""
Fichier contenant la classe Coordoneees
"""
from random import randint

from config import TAILLE_PLATEAU


class Coordonees:
    """
    Une coordonée sur le plateau de jeu
    """
    x: int
    y: int

    def __init__(self, x: int = None, y: int = None):
        """
        Crée un objet Coordonnées
        :param x: Si absent, génère une valeur aléatoire
        :param y: Si absent, génère une valeur aléatoire
        """
        if x is None:
            x = randint(0, TAILLE_PLATEAU)
        self.x = x

        if y is None:
            y = randint(0, TAILLE_PLATEAU)
        self.y = y

    def equals(self, value) -> bool:
        """
        Vérifie l'égalité entre deux coordonnées
        :param value: la coordonnée à vérifier
        :type value: Coordonees
        :return bool: le résultat de la vérification
        """
        return self.x == value.x and self.y == value.y
