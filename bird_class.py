import pygame
from pygame.image import load
from pygame.locals import *


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


class Bird(pygame.sprite.Sprite):

    group = pygame.sprite.Group()
    
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.elapseTime = 5 # this value is used to track how much time should pass between animations
        self.counter = 0
        for num in range(1,4):
            img = load(f"assets/bird{num}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        self.jumpDebounce = False

    def update(self):
        # Gravity
        self.vel = clamp(self.vel + 0.5, -20, 8)
        if self.rect.bottom < 768:
            self.rect.y += int(self.vel)
        
        # Jump
        keys = pygame.key.get_pressed()
        if keys[K_SPACE] == 1 and self.jumpDebounce == False:
            self.jumpDebounce = True
            self.vel = -10
        if keys[K_SPACE] == 0:
            self.jumpDebounce = False
        # handle animation
        self.counter += 1

        if self.counter > self.elapseTime:
            self.counter = 0
            self.index += 1

            if self.index >= len(self.images):
                self.index = 0


        self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)