import pygame
from ghosts.Ghost import Ghost


class Clyde(Ghost):
    def __init__(self, player):
        image = pygame.transform.scale(pygame.image.load('images/ghosts/clyde.png'),
                                       (40, 40))
        super().__init__(440, 338, 2, image, player)
        # super().__init__(170, 200, 2, image, player)

    def hit(self):
        self.x = 440
        self.y = 338

    def move(self):
        if self.direction == 0:
            if self.player.x > self.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                if self.player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif self.player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                elif self.player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
            elif self.turns[0]:
                if self.player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                if self.player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                else:
                    self.x += self.speed
        elif self.direction == 1:
            if self.player.y > self.y and self.turns[3]:
                self.direction = 3
            elif self.player.x < self.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                if self.player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif self.player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                elif self.player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
            elif self.turns[1]:
                if self.player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                if self.player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                else:
                    self.x -= self.speed
        elif self.direction == 2:
            if self.player.x < self.x and self.turns[1]:
                self.direction = 1
                self.x -= self.speed
            elif self.player.y < self.y and self.turns[2]:
                self.direction = 2
                self.y -= self.speed
            elif not self.turns[2]:
                if self.player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif self.player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                elif self.player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                elif self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
            elif self.turns[2]:
                if self.player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif self.player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                else:
                    self.y -= self.speed
        elif self.direction == 3:
            if self.player.y > self.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                if self.player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif self.player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                elif self.player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                elif self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
            elif self.turns[3]:
                if self.player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif self.player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                else:
                    self.y += self.speed
        if self.x < -30:
            self.x = 900
        elif self.x > 900:
            self.x = 30
