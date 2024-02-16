from Player import Player
from board import boards
from ghosts.Blinky import Blinky
from ghosts.Clyde import Clyde
from ghosts.Inky import Inky
from ghosts.Pinky import Pinky
import pygame
import math

PI = math.pi


class Maze(object):
    def __init__(self, color, width, height, screen):
        self.player = Player(450, 663, 3, 0, 2, self)
        self.level = boards
        self.width = width
        self.height = height
        self.screen = screen
        self.ghosts = [
            Blinky(self.player), Clyde(self.player), Inky(self.player), Pinky(self.player)
        ]
        self.flicker = bool

        self.isNormalMode = True
        self.color = color

    def draw_board(self):
        num1 = ((self.height - 50) // 32)
        num2 = (self.width // 30)
        for y in range(len(self.level)):  # висота num1
            for x in range(len(self.level[1])):  # ширина num2
                # if self.level[y][x] == 0
                if self.level[y][x] == 1:
                    pygame.draw.circle(self.screen, "white", (x * num2 + 0.5 * num2, y * num1 + 0.5 * num1), 2)
                if self.level[y][x] == 2 and not self.flicker:
                    pygame.draw.circle(self.screen, "white", (x * num2 + 0.5 * num2, y * num1 + 0.5 * num1), 6)
                if self.level[y][x] == 3:
                    pygame.draw.line(self.screen, self.color, (x * num2 + (0.5 * num2), y * num1),
                                     (x * num2 + (0.5 * num2), y * num1 + num1), 2)
                if self.level[y][x] == 4:
                    pygame.draw.line(self.screen, self.color, (x * num2, y * num1 + (0.5 * num1)),
                                     (x * num2 + num2, y * num1 + (0.5 * num1)), 2)
                if self.level[y][x] == 5:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 - (num2 * 0.5)), (y * num1 + (num1 * 0.5)), num2, num1],
                                    0, PI / 2, 2)

                if self.level[y][x] == 6:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 + (num2 * 0.5)), (y * num1 + (num1 * 0.5)), num2, num1],
                                    PI / 2, PI, 2)
                if self.level[y][x] == 7:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 + (num2 * 0.5)), (y * num1 - (num1 * 0.4)), num2, num1],
                                    PI, 3 * PI / 2, 2)
                if self.level[y][x] == 8:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 - (num2 * 0.4) - 2), (y * num1 - (num1 * 0.4)), num2, num1],
                                    3 * PI / 2, 2 * PI, 2)
                if self.level[y][x] == 9:
                    pygame.draw.line(self.screen, "white", (x * num2, y * num1 + (0.5 * num1)),
                                     (x * num2 + num2, y * num1 + (0.5 * num1)), 3)

    def draw_ghosts(self):
        for i in range(len(self.ghosts)):
            self.ghosts[i].draw(self.screen)
            self.ghosts[i].can_move(self.width, self.height)
            self.ghosts[i].move()

    def draw_player(self, counter):
        # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        direction = self.player.direction
        player_images = self.player.player_images
        player_x = self.player.x
        player_y = self.player.y

        if direction == 0:
            self.screen.blit(player_images[counter % len(player_images)], (player_x, player_y))
        elif direction == 1:
            self.screen.blit(pygame.transform.flip(player_images[counter % len(player_images)], True, False),
                             (player_x, player_y))
        elif direction == 2:
            self.screen.blit(pygame.transform.rotate(player_images[counter % len(player_images)], 90),
                             (player_x, player_y))
        elif direction == 3:
            self.screen.blit(pygame.transform.rotate(player_images[counter % len(player_images)], 270),
                             (player_x, player_y))
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox, 2)

    def draw_misc(self, score, power):
        font = pygame.font.Font(None, 36)  # створюємо об'єкт шрифту
        score_text = font.render(f'Score: {score}', True, 'white')  # створюємо зображення тексту з об'єктом шрифту
        self.screen.blit(score_text, (10, 920))  # відображаємо текст на екрані
        if power:
            pygame.draw.circle(self.screen, 'blue', (140, 930), 15)
        for i in range(self.player.lives_count):
            self.screen.blit(pygame.transform.scale(self.player.player_images[0], (30,30)), (650+i*40, 915))

