import pygame.transform
import pygame


# from main import width, height

class Player(object):
    def __init__(self, x, y, lives_count, direction, player_speed, maze):
        self.x = x
        self.y = y
        self.lives_count = lives_count
        self.direction = direction
        self.player_speed = player_speed
        self.player_images = []
        self.hitbox = pygame.Rect(self.x, self.y, 45, 45)
        self.maze = maze
        for i in range(1, 5):
            self.player_images.append(pygame.transform.scale(pygame.image.load(f'images/player/{i}.png'), (45, 45)))

    def hit(self, screen: pygame.Surface):
        '''
        This function is called when the player is hit by the ghost
        :return:
        '''

        self.x = 450
        self.y = 663
        for i in range(len(self.maze.ghosts)):
            self.maze.ghosts[i].hit()
        self.lives_count -= 1
        if self.lives_count < 1:
            # game ends
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render('Game Over', 1, (255, 0, 0))
            text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_width() / 2))
            screen.blit(text, text_rect)
            pygame.display.flip()

            i = 0
            while i < 300:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()

            # TODO потім поміняти на початок нової гри
            self.lives_count = 3

        else:
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()

    def check_position(self, center_x, center_y):
        turns = [False, False, False, False]
        num1 = (self.maze.height - 50) // 32
        num2 = (self.maze.width // 30)
        num3 = 15
        # check collisions based on center x and center y of player +/- fudge number
        if center_x // 30 < 29:
            if self.direction == 0:
                if self.maze.level[center_y // num1][(center_x - num3) // num2] < 3:
                    turns[1] = True
            if self.direction == 1:
                if self.maze.level[center_y // num1][(center_x + num3) // num2] < 3:
                    turns[0] = True
            if self.direction == 2:
                if self.maze.level[(center_y + num3) // num1][center_x // num2] < 3:
                    turns[3] = True
            if self.direction == 3:
                if self.maze.level[(center_y - num3) // num1][center_x // num2] < 3:
                    turns[2] = True

            if self.direction == 2 or self.direction == 3:
                if 12 <= center_x % num2 <= 18:
                    if self.maze.level[(center_y + num3) // num1][center_x // num2] < 3:
                        turns[3] = True
                    if self.maze.level[(center_y - num3) // num1][center_x // num2] < 3:
                        turns[2] = True
                if 12 <= center_y % num1 <= 18:
                    if self.maze.level[center_y // num1][(center_x - num2) // num2] < 3:
                        turns[1] = True
                    if self.maze.level[center_y // num1][(center_x + num2) // num2] < 3:
                        turns[0] = True
            if self.direction == 0 or self.direction == 1:
                if 12 <= center_x % num2 <= 18:
                    if self.maze.level[(center_y + num1) // num1][center_x // num2] < 3:
                        turns[3] = True
                    if self.maze.level[(center_y - num1) // num1][center_x // num2] < 3:
                        turns[2] = True
                if 12 <= center_y % num1 <= 18:
                    if self.maze.level[center_y // num1][(center_x - num3) // num2] < 3:
                        turns[1] = True
                    if self.maze.level[center_y // num1][(center_x + num3) // num2] < 3:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns

    def move_player(self, turns_allowed):
        player_speed = self.player_speed
        direction = self.direction

        if direction == 0 and turns_allowed[0]:
            self.x += player_speed
        elif direction == 1 and turns_allowed[1]:
            self.x -= player_speed
        if direction == 2 and turns_allowed[2]:
            self.y -= player_speed
        elif direction == 3 and turns_allowed[3]:
            self.y += player_speed
        self.hitbox = pygame.Rect(self.x, self.y, 45, 45)
        return self.x, self.y

    def check_collisions(self, score, center_x, center_y, power,power_count, eaten_ghosts):
        num1 = (self.maze.height - 50) // 32
        num2 = self.maze.width // 30
        if 0 < self.x < 870:
            if self.maze.level[center_y // num1][center_x // num2] == 1:
                self.maze.level[center_y // num1][center_x // num2] = 0
                score += 10
            if self.maze.level[center_y // num1][center_x // num2] == 2:
                self.maze.level[center_y // num1][center_x // num2] = 0
                score += 50
                power = True
                power_count = 0
                eaten_ghosts = [False, False, False, False]
        return score, power, power_count, eaten_ghosts
