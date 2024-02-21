import pygame



class Heart():
    def __init__(self, x, y, maze):
        self.x = x
        self.y = y

        self.image = pygame.transform.scale(pygame.image.load('images/bonuses/heart.png'),(40, 40))
        self.rect = self.image.get_rect()
        self.width = 40
        self.height = 40
        self.rect.center = (self.x, self.y)
        self.maze = maze

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
    def hit(self):
        self.maze.player.lives_count += 1
        pass
