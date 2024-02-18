import pygame
from settings import *
from pygame.locals import *
from board import boards
from maze import Maze


class Game():
    def __init__(self):
        pygame.init()
        self.small_screen = pygame.display.set_mode((width, height), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.screen = self.small_screen.copy()
        self.timer = pygame.time.Clock()

    def restart_game(self):
        # Reset all necessary variables to their initial values
        # level = boards.copy()
        color = "blue"
        counter = 0
        turns_allowed = [False, False, False, False]
        direction_command = 0
        score = 0
        power = False
        power_counter = 0
        eaten_ghosts = [False, False, False, False]
        moving = False
        startup_counter = 0

        # Recreate the maze object
        maze = Maze("blue", width, height, self.screen)

        return color, counter, turns_allowed, direction_command, score, power, power_counter, eaten_ghosts, moving, startup_counter, maze

    def run(self):
        (color,
         counter,
         turns_allowed,
         direction_command,
         score,
         power,
         power_counter,
         eaten_ghosts,
         moving,
         startup_counter,
         maze) = self.restart_game()

        run = True

        maze = Maze("blue", width, height, self.screen)

        while run:
            self.timer.tick(fps)

            if counter < 19:
                counter += 1
                if counter > 3:
                    maze.flicker = False
            else:
                counter = 0
                maze.flicker = True
            if power and power_counter < 600:
                power_counter += 1
            elif power and power_counter >= 600:
                power_counter = 0
                power = False
                eaten_ghosts = [False, False, False, False]
            if startup_counter < 180:
                moving = False
                startup_counter += 1
            else:
                moving = True
            # # Перевірка колізій між гравцем та привидами
            # if pygame.sprite.spritecollide(maze.player, maze.ghosts, False):
            #     player.hit()

            for ghost in maze.ghosts:
                if maze.player.hitbox.colliderect(ghost.hitbox):
                    maze.player.hit()
                    break

            self.screen.fill("black")
            maze.draw_board()
            maze.draw_ghosts()
            maze.draw_player(counter)
            maze.draw_misc(score, power=power)
            self.small_screen.blit(pygame.transform.scale(self.screen, self.small_screen.get_rect().size), (0, 0))

            player_x = maze.player.x
            player_y = maze.player.y
            center_x = player_x + 23
            center_y = player_y + 24
            turns_allowed = maze.check_position(center_x, center_y)
            if moving:
                player_x, player_y = maze.move_player(turns_allowed)
            score, power, power_counter, eaten_ghosts = maze.check_collisions(score, center_x=center_x,
                                                                              center_y=center_y, power=power,
                                                                              power_count=power_counter,
                                                                              eaten_ghosts=eaten_ghosts)

            if maze.player.lives_count < 1:

                screen = pygame.display.get_surface()
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

                color, counter, turns_allowed, direction_command, score, power, power_counter, eaten_ghosts, moving, startup_counter, maze = self.restart_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == VIDEORESIZE:
                    old_width, old_height = self.screen.get_size()
                    new_width, new_height = event.size
                    ratio = old_width / old_height
                    if new_width > new_height:
                        new_width = int(new_height * ratio)
                    else:
                        new_height = int(new_width / ratio)
                    small_screen = pygame.display.set_mode((new_width, new_height), HWSURFACE | DOUBLEBUF | RESIZABLE)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        direction_command = 0
                    if event.key == pygame.K_LEFT:
                        direction_command = 1
                    if event.key == pygame.K_UP:
                        direction_command = 2
                    if event.key == pygame.K_DOWN:
                        direction_command = 3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT and direction_command == 0:
                        direction_command = maze.player.direction
                    if event.key == pygame.K_LEFT and direction_command == 1:
                        direction_command = maze.player.direction
                    if event.key == pygame.K_UP and direction_command == 2:
                        direction_command = maze.player.direction
                    if event.key == pygame.K_DOWN and direction_command == 3:
                        direction_command = maze.player.direction

            for i in range(4):
                if direction_command == i and turns_allowed[i]:
                    maze.player.direction = i

            if maze.player.x > 900:
                maze.player.x = -47
            elif maze.player.x < -50:
                maze.player.x = 897

            if maze.player.direction == 0 and turns_allowed[0]:
                maze.player.direction = 0
            if maze.player.direction == 1 and turns_allowed[1]:
                maze.player.direction = 1
            if maze.player.direction == 2 and turns_allowed[2]:
                maze.player.direction = 2
            if maze.player.direction == 3 and turns_allowed[3]:
                maze.player.direction = 3

            pygame.display.flip()

        pygame.quit()
