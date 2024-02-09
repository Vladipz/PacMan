import pygame
from ghosts.Ghost import Ghost


class Inky(Ghost):
    def __init__(self, player):
        image = pygame.transform.scale(pygame.image.load('images/ghosts/inky.png'),
                                       (40, 40))
        super().__init__(400, 300, 2, image, player)
