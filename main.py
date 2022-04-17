from pygame import *
from time import time as timer
import random

window = display.set_mode((700,500))
display.set_caption("Platformer")
backgr = transform.scale(image.load('background.jpg'), (700,500))
window.blit(backgr,(0,0))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.turn = 'right'
        self.speedY = 0

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def gravity(self):
        if self.rect.y <= 360:
            self.speedY -= 0.2
        else:
            self.speedY = 0

    def update(self):
        self.rect.y -= self.speedY
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
            if self.turn == 'left':
                self.image = transform.scale(image.load('right_side.png'), (70,80)) 
                self.turn = 'right'
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
            if self.turn == 'right':
                self.image = transform.scale(image.load('left_side.png'), (70,80)) 
                self.turn = 'left'
        if keys_pressed[K_SPACE] and self.rect.y > 0 and self.speedY == 0:
            self.speedY = 8
            self.rect.y -= self.speedY


spr1 = Player('right_side.png', 0, 100, 3, 70, 80)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(backgr,(0,0))
        spr1.reset()
        spr1.update()
        spr1.gravity()
        
    display.update()