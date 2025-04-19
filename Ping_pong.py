from pygame import *
mixer.init()
from random import *
font.init()
from time import time as timer

window = display.set_mode((500, 500))
display.set_caption("Ping_Pong")
is_playing = True
now_turn = 1



class GameSprite(sprite.Sprite):
    def __init__(self, x, y, image_name, speed, weidth, height):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (weidth, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def show_sprite(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.x += self.speed
        self.show_sprite()

class Ball(GameSprite):
    def update(self, player):
        self.speed_x, self.speed_y = self.speed
        self.rect.x -= self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.y <= 0:
            self.speed_y -= 20
        elif self.rect.y >= 490:
            self.speed_y += 20
        if self.rect.colliderect(player):
            if self.rect.x < 250:
                self.speed_x -= 20
            else:
                self.speed_x += 20
        self.show_sprite()


player_1 = Player(25, 225, 'rocket.png', 20, 10, 50)
player_2 = Player(475, 225, 'rocket.png', 20, 10, 50)
ball = Ball(245, 245, 'ball.png', (10, 10), 10, 10)
FPS = 60


while is_playing:
    for e in event.get():
        if e.type == QUIT:
            is_playing = False
    if now_turn == 1:
        player_1.update()
        ball.update(player_1)
    elif now_turn == 2:
        player_2.update()
        ball.update(player_2)
    
    time.delay(50)
    display.update()