import pygame
from settings import fps, width, height
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE, VIDEORESIZE
from maze import Maze
from save_load_manager import SavaLoadSystem
import sys
import path


class Game:
    def __init__(self):
        pygame.init()
        self.small_screen = pygame.display.set_mode(
            (width, height), HWSURFACE | DOUBLEBUF | RESIZABLE
        )
        self.screen = self.small_screen.copy()
        self.timer = pygame.time.Clock()
        self.save_load_system = SavaLoadSystem(".json", "save_files")
        self.score = 0
        self.best_score = 0

    def restart_game(self, score, best_score):
        # Reset all necessary variables to their initial values
        # level = boards.copy()

        color = "blue"
        if len(sys.argv) > 1:
            color = sys.argv[1]
        counter = 0
        turns_allowed = [False, False, False, False]
        direction_command = 0
        self.score = score
        self.best_score = best_score
        power = False
        power_counter = 0
        eaten_ghosts = [False, False, False, False]
        moving = False
        startup_counter = 0
        # Recreate the maze object
        maze = Maze(color, width, height, self.screen)
        maze.register_ghosts_observers()
        return (
            color,
            counter,
            turns_allowed,
            direction_command,
            score,
            power,
            power_counter,
            eaten_ghosts,
            moving,
            startup_counter,
            maze,
            best_score,
        )

    def run(self):
        """
        This function is called to run the game
        :return:
        """

        (
            color,
            counter,
            turns_allowed,
            direction_command,
            self.score,
            power,
            power_counter,
            eaten_ghosts,
            moving,
            startup_counter,
            maze,
            self.best_score,
        ) = self.restart_game(0, self.save_load_system.load("best_score", 0))

        run = True

        window_icon = pygame.image.load(path.icon_path)
        pygame.display.set_icon(window_icon)
        pygame.display.set_caption("OrangeMan")
        while run:
            self.timer.tick(fps)

            if counter < 19:
                counter += 0.3
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
                    if ghost.powerup:
                        ghost.hit()
                    else:
                        direction_command = 0
                        maze.player.hit(self.screen)
                    break

            for bonus in maze.bonuses:
                if maze.player.hitbox.colliderect(bonus.rect):
                    bonus.hit()
                    maze.bonuses.remove(bonus)
                    break

            self.screen.fill("black")
            maze.draw_board()
            if len(maze.bonuses) != 0:
                maze.draw_heart()
            maze.draw_ghosts()
            maze.draw_player(int(counter))
            maze.draw_misc(self.score, self.best_score, power)

            self.small_screen.blit(
                pygame.transform.scale(self.screen, self.small_screen.get_rect().size),
                (0, 0),
            )

            player_x = maze.player.x
            player_y = maze.player.y
            center_x = player_x + 23
            center_y = player_y + 24

            maze.player.center_x = center_x
            maze.player.center_y = center_y

            turns_allowed = maze.check_position(center_x, center_y)
            if moving:
                player_x, player_y = maze.move_player(turns_allowed)
                for i in range(len(maze.ghosts)):
                    maze.ghosts[i].move()
            self.score, power, power_counter, eaten_ghosts = maze.check_collisions(
                self.score,
                center_x=center_x,
                center_y=center_y,
                power=power,
                power_count=power_counter,
                eaten_ghosts=eaten_ghosts,
            )

            if maze.check_win():
                (
                    color,
                    counter,
                    turns_allowed,
                    direction_command,
                    score,
                    power,
                    power_counter,
                    eaten_ghosts,
                    moving,
                    startup_counter,
                    maze,
                    best_score,
                ) = self.restart_game(self.score, self.best_score)

            if maze.player.lives_count < 1:

                screen = pygame.display.get_surface()

                # game ends
                font1 = pygame.font.SysFont("comicsans", 100)
                text = font1.render("Game Over", 1, (255, 0, 0))
                text_rect = text.get_rect(
                    center=(screen.get_width() / 2, screen.get_width() / 2)
                )
                screen.blit(text, text_rect)

                if self.score > self.best_score:
                    self.best_score = self.score
                    font1 = pygame.font.SysFont("comicsans", 30)
                    text = font1.render(
                        f"New best score: {self.best_score}", 1, (255, 0, 0)
                    )
                    text_rect = text.get_rect(
                        center=(screen.get_width() / 2, screen.get_width() / 2 + 100)
                    )
                    screen.blit(text, text_rect)

                pygame.display.flip()

                self.wait_and_quit(3)

                (
                    color,
                    counter,
                    turns_allowed,
                    direction_command,
                    score,
                    power,
                    power_counter,
                    eaten_ghosts,
                    moving,
                    startup_counter,
                    maze,
                    best_score,
                ) = self.restart_game(0, self.best_score)

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
                if event.type == maze.powerup_finish_event:
                    maze.notify(False)
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
        self.save_load_system.save(self.best_score, "best_score")

        pygame.quit()

    def wait_and_quit(self, time_delay):
        """
        This function is called to wait
        :param time_delay: The duration to wait in seconds.
        :return:
        """
        helper = 100
        time_delay = time_delay * helper
        i = 0
        while i < time_delay:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
