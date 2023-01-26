"""
Fichier contenant la classe Plateau
"""
from code import Snake, Coordonees
from config import TAILLE_PLATEAU


class Plateau:
    """
    Plateau contenant un Snake et une pomme
    """
    snake: Snake
    prochaine_direction: str
    pomme: Coordonees
    game_over: bool

    def __init__(self):
        """
        Initialize un nouveau plateau avec un Snake et une pomme
        """
        self.snake = Snake()
        self.prochaine_direction = self.snake.direction
        self.pomme = Coordonees()
        self.game_over = False
        self.nouvelle_pomme()

    def tour(self):
        """
        Joue un tour de jeu
        Vérifie si une pomme a été mangée
        Vérifie si le Snake est entré en contact avec lui-même
        """
        self.snake.direction = self.prochaine_direction

        # Bouger le Snake
        nouvelle_position_tete = Coordonees(self.snake.tete.x, self.snake.tete.y)
        if self.snake.direction == 'haut':
            nouvelle_position_tete.y -= 1
            if nouvelle_position_tete.y < 0:
                nouvelle_position_tete.y = TAILLE_PLATEAU

        elif self.snake.direction == 'gauche':
            nouvelle_position_tete.x -= 1
            if nouvelle_position_tete.x < 0:
                nouvelle_position_tete.x = TAILLE_PLATEAU

        elif self.snake.direction == 'bas':
            nouvelle_position_tete.y += 1
            if nouvelle_position_tete.y > TAILLE_PLATEAU:
                nouvelle_position_tete.y = 0

        else:
            nouvelle_position_tete.x += 1
            if nouvelle_position_tete.x > TAILLE_PLATEAU:
                nouvelle_position_tete.x = 0

        nouveau_corps = [nouvelle_position_tete] + self.snake.corps
        self.snake.corps = nouveau_corps

        # Si la pomme a été mangée, on doit générer une nouvelle pomme
        if self.pomme_mangee():
            self.nouvelle_pomme()

        # Sinon, le corps du Snake ne grandit pas
        else:
            self.snake.corps.pop(-1)

        # On vérifie si la partie est terminée après le mouvement du Snake
        self.partie_terminee()

    def pomme_mangee(self) -> bool:
        """
        Vérifie si la pomme a été mangée
        :return bool: est-ce que la pomme a été mangée
        """
        # TODO: modifier cette fonction
        return False

    def partie_terminee(self):
        """
        Vérifie si le Snake viens d'entrer en contact avec son corps
        """
        # TODO: modifier cette fonction
        self.game_over = False

    def nouvelle_pomme(self):
        """
        On génère une nouvelle pomme sur le plateau en dehors du Snake
        Si ce n'est pas possible, c'est que le joueur a gagné
        et le snake fait la taille du plateau
        """
        # Vérifie si on peux créer une pomme
        taille_snake = len(self.snake.corps)
        taille_plateau = TAILLE_PLATEAU + 1

        if taille_snake >= (taille_plateau * taille_plateau) - 1:
            self.game_over = True
            print('Game over!')
            print('Le serpent fait la taille du plateau')
            print(f'Score: {len(self.snake.corps)} points')
        else:
            # Une pomme peux être créée, on doit donc la créer sur une case non occupée par le Snake
            position_valide = False
            while not position_valide:
                # On génère une pomme aléatoirement
                self.pomme = Coordonees()
                position_valide = True

                # On vérifie que la pomme n'est pas dans le Snake
                for partie_corps in self.snake.corps:
                    if self.pomme.equals(partie_corps):
                        position_valide = False
