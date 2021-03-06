import pygame
import math
import random
from plot.imagens import *

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = capanga_img
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 40, 40)


        self.rect.x = 750 + random.randint(1, 250)
        self.rect.y = random.randint(1, 420)

        self.speed = 1 + random.random() * 3


    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
