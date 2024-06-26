import copy
import random

from bonuses.heart import Heart
from Player import Player
from board import boards
from ghosts.Blinky import Blinky
from ghosts.Clyde import Clyde
from ghosts.Inky import Inky
from ghosts.Pinky import Pinky
import pygame
import math
from Observable import Observable

PI = math.pi


class Maze(Observable):
    def __init__(self, color, width, height, screen):
        self.player = Player(450, 663, 3, 0, 2, self)
        self.level = copy.deepcopy(boards)
        self.width = width
        self.height = height
        self.screen = screen
        self.ghosts = [
            Blinky(self.player),
            Clyde(self.player),
            Inky(self.player),
            Pinky(self.player),
        ]
        self.flicker = bool

        self.isNormalMode = True
        self.color = color
        self.count_of_points = self.check_point_on_board()
        # self.isHeartSpawned = False
        self.bonuses = []
        self.powerup_finish_event = pygame.USEREVENT + 1

    def check_win(self):
        """
        Checks if the player has won
         :return: bool
        """
        count_of_points = self.check_point_on_board()
        if count_of_points == 0:
            return True
        return False

    def check_point_on_board(self):
        """
            check number of points on the board
        :return: int
        """
        counter = 0
        for y in range(len(self.level)):
            for x in range(len(self.level[1])):
                if self.level[y][x] == 1 or self.level[y][x] == 2:
                    counter += 1
        return counter

    def find_coordinates_for_health(self):
        """
        Знаходить координати для серця
        :return: tuple
        """
        count_of_points = self.check_point_on_board()
        random_number = random.randint(1, count_of_points)
        for i in range(len(self.level)):
            for j in range(len(self.level[1])):
                if self.level[i][j] == 1 or self.level[i][j] == 2:
                    random_number -= 1
                    if random_number == 0:
                        return j, i

        return 2, 2

    def draw_heart(self):
        """
        This method draws the heart on the screen
        :return: None
        """
        for i in range(len(self.bonuses)):
            self.bonuses[i].draw(self.screen)
        # for bonus in self.bonuses:
        #     bonus.draw(self.screen)

    def check_heart_spawn(self):
        """
        Checks if hearts can be spawned
        :return: None
        """
        half = self.count_of_points // 2
        count = self.check_point_on_board()
        if count == half:
            return True
        return False

    def register_ghosts_observers(self):
        for i in range(len(self.ghosts)):
            self.register_observer(self.ghosts[i])

    def draw_board(self):
        """
        Draws the board
        :return:
        """
        num1 = (self.height - 50) // 32
        num2 = self.width // 30
        for y in range(len(self.level)):  # висота num1
            for x in range(len(self.level[1])):  # ширина num2
                # if self.level[y][x] == 0
                if self.level[y][x] == 1:
                    pygame.draw.circle(
                        self.screen,
                        "white",
                        (x * num2 + 0.5 * num2, y * num1 + 0.5 * num1),
                        2,
                    )
                if self.level[y][x] == 2 and not self.flicker:
                    pygame.draw.circle(
                        self.screen,
                        "white",
                        (x * num2 + 0.5 * num2, y * num1 + 0.5 * num1),
                        6,
                    )
                if self.level[y][x] == 3:
                    pygame.draw.line(
                        self.screen,
                        self.color,
                        (x * num2 + (0.5 * num2), y * num1),
                        (x * num2 + (0.5 * num2), y * num1 + num1),
                        2,
                    )
                if self.level[y][x] == 4:
                    pygame.draw.line(
                        self.screen,
                        self.color,
                        (x * num2, y * num1 + (0.5 * num1)),
                        (x * num2 + num2, y * num1 + (0.5 * num1)),
                        2,
                    )
                if self.level[y][x] == 5:
                    pygame.draw.arc(
                        self.screen,
                        self.color,
                        [
                            (x * num2 - (num2 * 0.5)),
                            (y * num1 + (num1 * 0.5)),
                            num2,
                            num1,
                        ],
                        0,
                        PI / 2,
                        2,
                    )

                if self.level[y][x] == 6:
                    pygame.draw.arc(
                        self.screen,
                        self.color,
                        [
                            (x * num2 + (num2 * 0.5)),
                            (y * num1 + (num1 * 0.5)),
                            num2,
                            num1,
                        ],
                        PI / 2,
                        PI,
                        2,
                    )
                if self.level[y][x] == 7:
                    pygame.draw.arc(
                        self.screen,
                        self.color,
                        [
                            (x * num2 + (num2 * 0.5)),
                            (y * num1 - (num1 * 0.4)),
                            num2,
                            num1,
                        ],
                        PI,
                        3 * PI / 2,
                        2,
                    )
                if self.level[y][x] == 8:
                    pygame.draw.arc(
                        self.screen,
                        self.color,
                        [
                            (x * num2 - (num2 * 0.4) - 2),
                            (y * num1 - (num1 * 0.4)),
                            num2,
                            num1,
                        ],
                        3 * PI / 2,
                        2 * PI,
                        2,
                    )
                if self.level[y][x] == 9:
                    pygame.draw.line(
                        self.screen,
                        "white",
                        (x * num2, y * num1 + (0.5 * num1)),
                        (x * num2 + num2, y * num1 + (0.5 * num1)),
                        3,
                    )

    def draw_ghosts(self):
        for i in range(len(self.ghosts)):
            self.ghosts[i].draw(self.screen)
            self.ghosts[i].can_move(self.width, self.height)

    def draw_player(self, counter):
        # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        direction = self.player.direction
        player_images = self.player.player_images
        player_x = self.player.x
        player_y = self.player.y

        if direction == 0:
            self.screen.blit(
                player_images[counter % len(player_images)], (player_x, player_y)
            )
        elif direction == 1:
            self.screen.blit(
                pygame.transform.flip(
                    player_images[counter % len(player_images)], True, False
                ),
                (player_x, player_y),
            )
        elif direction == 2:
            self.screen.blit(
                pygame.transform.rotate(
                    player_images[counter % len(player_images)], 90
                ),
                (player_x, player_y),
            )
        elif direction == 3:
            self.screen.blit(pygame.transform.rotate(player_images[counter % len(player_images)], 270),
                             (player_x, player_y))

            self.screen.blit(
                pygame.transform.rotate(
                    player_images[counter % len(player_images)], 270
                ),
                (player_x, player_y),
            )
        # pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox, 2)

    def check_position(self, center_x, center_y):
        turns = [False, False, False, False]
        num1 = (self.height - 50) // 32
        num2 = self.width // 30
        num3 = 15
        # check collisions based on center x and center y of player +/- fudge number
        if center_x // 30 < 29:
            if self.player.direction == 0:
                if self.level[center_y // num1][(center_x - num3) // num2] < 3:
                    turns[1] = True
            if self.player.direction == 1:
                if self.level[center_y // num1][(center_x + num3) // num2] < 3:
                    turns[0] = True
            if self.player.direction == 2:
                if self.level[(center_y + num3) // num1][center_x // num2] < 3:
                    turns[3] = True
            if self.player.direction == 3:
                if self.level[(center_y - num3) // num1][center_x // num2] < 3:
                    turns[2] = True

            if self.player.direction == 2 or self.player.direction == 3:
                if 12 <= center_x % num2 <= 18:
                    if self.level[(center_y + num3) // num1][center_x // num2] < 3:
                        turns[3] = True
                    if self.level[(center_y - num3) // num1][center_x // num2] < 3:
                        turns[2] = True
                if 12 <= center_y % num1 <= 18:
                    if self.level[center_y // num1][(center_x - num2) // num2] < 3:
                        turns[1] = True
                    if self.level[center_y // num1][(center_x + num2) // num2] < 3:
                        turns[0] = True
            if self.player.direction == 0 or self.player.direction == 1:
                if 12 <= center_x % num2 <= 18:
                    if self.level[(center_y + num1) // num1][center_x // num2] < 3:
                        turns[3] = True
                    if self.level[(center_y - num1) // num1][center_x // num2] < 3:
                        turns[2] = True
                if 12 <= center_y % num1 <= 18:
                    if self.level[center_y // num1][(center_x - num3) // num2] < 3:
                        turns[1] = True
                    if self.level[center_y // num1][(center_x + num3) // num2] < 3:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns

    def move_player(self, turns_allowed):
        player_speed = self.player.player_speed
        direction = self.player.direction

        if direction == 0 and turns_allowed[0]:
            self.player.x += player_speed
        elif direction == 1 and turns_allowed[1]:
            self.player.x -= player_speed
        if direction == 2 and turns_allowed[2]:
            self.player.y -= player_speed
        elif direction == 3 and turns_allowed[3]:
            self.player.y += player_speed

        self.player.hitbox.center = self.player.x + 23, self.player.y + 24

        return self.player.x, self.player.y

    def check_collisions(
        self, score, center_x, center_y, power, power_count, eaten_ghosts
    ):
        num1 = (self.height - 50) // 32
        num2 = self.width // 30

        if 0 < self.player.x < 870:
            if self.level[center_y // num1][center_x // num2] == 1:
                self.level[center_y // num1][center_x // num2] = 0
                score += 10

                if self.check_heart_spawn():
                    x, y = self.find_coordinates_for_health()
                    x = x * num2 + 0.5 * num2
                    y = y * num1 + 0.5 * num1
                    self.bonuses.append(Heart(x, y, self))
            if self.level[center_y // num1][center_x // num2] == 2:
                self.level[center_y // num1][center_x // num2] = 0
                score += 50
                power = True
                power_count = 0
                self.notify(power)
                eaten_ghosts = [False, False, False, False]
                pygame.time.set_timer(self.powerup_finish_event, 7000)
                if self.check_heart_spawn():
                    x, y = self.find_coordinates_for_health()
                    x = x * num2 + 0.5 * num2
                    y = y * num1 + 0.5 * num1
                    self.bonuses.append(Heart(x, y, self))

        return score, power, power_count, eaten_ghosts

    def draw_misc(
        self,
        score,
        best_score,
        power,
    ):
        font = pygame.font.Font(None, 36)  # створюємо об'єкт шрифту
        score_text = font.render(
            f"Score: {score}", True, "white"
        )  # створюємо зображення тексту з об'єктом шрифту
        self.screen.blit(score_text, (10, 920))  # відображаємо текст на екрані

        score_text = font.render(
            f"Best score: {best_score}", True, "white"
        )  # створюємо зображення тексту з об'єктом шрифту
        self.screen.blit(score_text, (200, 920))  # відображаємо текст на екрані

        if power:
            pygame.draw.circle(self.screen, "blue", (140, 930), 15)
        for i in range(self.player.lives_count):
            self.screen.blit(
                pygame.transform.scale(self.player.player_images[0], (30, 30)),
                (650 + i * 40, 915),
            )
