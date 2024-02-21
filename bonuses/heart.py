import pygame



class Heart():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 50
        self.image = pygame.image.load('images/bonuses/heart.png')
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        pass
