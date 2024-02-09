import pygame
from ghosts.Ghost import Ghost


class Clyde(Ghost):
    def __init__(self, player):
        image = pygame.transform.scale(pygame.image.load('images/ghosts/clyde.png'),
                                       (40, 40))
        super().__init__(440, 300, 2, image, player)
