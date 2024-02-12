import pygame.transform
import pygame

class Player(object):
    def __init__(self, x, y, lives_count, direction):
        self.x = x
        self.y = y
        self.lives_count = lives_count
        self.direction = direction
        self.player_images = []
        for i in range(1, 5):
            self.player_images.append(pygame.transform.scale(pygame.image.load(f'images/player/{i}.png'), (45, 45)))


