from abc import ABC
from board import boards


class Movable(ABC):
    def __init__(self, x, y, in_box, dead, direction):
        self.x = x
        self.y = y
        self.turns = None
        self.center_x = x + 20
        self.center_y = y + 20
        self.in_box = in_box
        self.is_dead = dead
        self.direction = direction

    def can_move(self, width, height):
        num1 = ((height - 50) // 32)
        num2 = (width // 30)
        num3 = 1
        self.turns = [False, False, False, False]
        if 0 < self.x < width - 40 and 0 < self.y < height - 40:
            if boards[(self.y - num3) // num1][(self.x + 20) // num2] == 9:
                self.turns[2] = True
            if boards[(self.y + 20) // num1][(self.x - num3) // num2] < 3 \
                    or (boards[(self.y + 20) // num1][(self.x - num3) // num2] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[1] = True
            if boards[(self.y + 20) // num1][(self.x + num3 + 40) // num2] < 3 \
                    or (boards[(self.y + 20) // num1][(self.x + num3 + 40) // num2] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[0] = True
            if boards[(self.y + num3 + 40) // num1][(self.x + 20) // num2] < 3 \
                    or (boards[(self.y + num3 + 40) // num1][(self.x + 20) // num2] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[3] = True
            if boards[(self.y - num3) // num1][(self.x + 20) // num2] < 3 \
                    or (boards[(self.y - num3) // num1][(self.x + 20) // num2] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[2] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x < 550 and 370 < self.y < 480:
            self.in_box = True
        else:
            self.in_box = False



