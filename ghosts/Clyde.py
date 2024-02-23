import pygame
from Player import Player
from ghosts.Ghost import Ghost


class Clyde(Ghost):
    def __init__(self, player):
        super().__init__(440, 338, 2, 'images/ghosts/clyde.png', player, Player(800, -50, 0, 0, 0, None))
        # super().__init__(170, 200, 2, image, player)

    def hit(self):
        super().hit()
        self.x = 440
        self.y = 338

    def move(self):
        player = self.choose_target()
        if self.direction == 0:
            if player.x > self.x and self.turns[0]:
                self.x += self.speed
            elif not self.turns[0]:
                if player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                elif player.x < self.x and self.turns[1]:
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
                if player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                if player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                else:
                    self.x += self.speed
        elif self.direction == 1:
            if player.y > self.y and self.turns[3]:
                self.direction = 3
            elif player.x < self.x and self.turns[1]:
                self.x -= self.speed
            elif not self.turns[1]:
                if player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                elif player.x > self.x and self.turns[0]:
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
                if player.y > self.y and self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                if player.y < self.y and self.turns[2]:
                    self.direction = 2
                    self.y -= self.speed
                else:
                    self.x -= self.speed
        elif self.direction == 2:
            if player.x < self.x and self.turns[1]:
                self.direction = 1
                self.x -= self.speed
            elif player.y < self.y and self.turns[2]:
                self.direction = 2
                self.y -= self.speed
            elif not self.turns[2]:
                if player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                elif player.y > self.y and self.turns[3]:
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
                if player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                else:
                    self.y -= self.speed
        elif self.direction == 3:
            if player.y > self.y and self.turns[3]:
                self.y += self.speed
            elif not self.turns[3]:
                if player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                elif player.y < self.y and self.turns[2]:
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
                if player.x > self.x and self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif player.x < self.x and self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
                else:
                    self.y += self.speed
        if self.x < -30:
            self.x = 900
        elif self.x > 900:
            self.x = 30
