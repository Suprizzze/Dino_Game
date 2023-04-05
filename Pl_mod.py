import pygame
import Sprit


class Player:

    def __init__(self, x, y, speed, width, height, jump_count):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.jump_count = jump_count
        self.is_jumpr = False
        self.is_jumpl = False
        self.left = False
        self.right = False
        self.animCount = 0
        self.fire = False
        self.ps = False
        self.bg_count = 0

    def update_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > -200:
            self.x -= self.speed
            self.left = True
            self.right = False
            self.ps = False
        elif keys[pygame.K_RIGHT] and self.x < 750:
            self.x += self.speed
            self.left = False
            self.right = True
            self.ps = False
        elif keys[pygame.K_b]:
            self.ps = True
            self.right = False
            self.left = False
        else:
            self.left = False
            self.right = True


        if not (self.is_jumpr) and not (self.is_jumpl):  # указываем если фалс из джамп
            if keys[pygame.K_m]:  # а тут если пробель и становится тру из джамп
                self.is_jumpr = True
                self.is_jumpl = False

            if keys[pygame.K_n]:
                self.is_jumpl = True
                self.is_jumpr = False
        else:
            if self.jump_count >= -10:  # тут укакзываем что если больше или равно  - 10
                if self.jump_count < 0:
                    self.y += (self.jump_count ** 2 / 2)
                else:
                    self.y -= self.jump_count ** 2 / 2
                self.jump_count -= 0.5
            else:
                self.is_jumpl = False
                self.is_jumpr = False
                self.jump_count = 10
                self.left = False
                self.right = True

