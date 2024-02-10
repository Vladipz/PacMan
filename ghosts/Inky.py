import pygame
from ghosts.Ghost import Ghost


class Inky(Ghost):
    def __init__(self, player):
        image = pygame.transform.scale(pygame.image.load('images/ghosts/inky.png'),
                                       (40, 40))
        super().__init__(320, 300, 2, image, player)

    def move(self):
        player_x = self.player.x
        player_y = self.player.y

        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed

        if self.y < player_y:
            self.y += self.speed
        elif self.y > player_y:
            self.y -= self.speed
