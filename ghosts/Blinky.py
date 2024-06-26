from ghosts.Ghost import Ghost
from Player import Player
import path


class Blinky(Ghost):
    def __init__(self, player):
        super().__init__(
            56, 58, 0, path.ghosts_image[0], player, Player(100, -50, 0, 0, 0, None)
        )

    def hit(self):
        super().hit()
        self.x = 56
        self.y = 58

    def update(self, powerup):
        super().update(powerup)

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
                self.x += self.speed
        elif self.direction == 1:
            if player.x < self.x and self.turns[1]:
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
                self.x -= self.speed
        elif self.direction == 2:
            if player.y < self.y and self.turns[2]:
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
                elif self.turns[3]:
                    self.direction = 3
                    self.y += self.speed
                elif self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
            elif self.turns[2]:
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
                elif self.turns[0]:
                    self.direction = 0
                    self.x += self.speed
                elif self.turns[1]:
                    self.direction = 1
                    self.x -= self.speed
            elif self.turns[3]:
                self.y += self.speed
        if self.x < -30:
            self.x = 900
        elif self.x > 900:
            self.x = 30
