from pygame import *
mixer.init()
from random import *
font.init()
from time import time as timer

window = display.set_mode((500, 500))
background = transform.scale(image.load('table.png'), (500, 500))
display.set_caption("Ping_Pong")
is_playing = True
now_turn = 1
win = None
now_time = timer()


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
    def update(self, num):
        keys_pressed = key.get_pressed()
        if num == 1:
            if keys_pressed[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN] and self.rect.y < 450:
                self.rect.y += self.speed
        elif num == 2:
            if keys_pressed[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if keys_pressed[K_s] and self.rect.y < 450:
                self.rect.y += self.speed
        

class Ball(GameSprite):
    def update(self, player_1, player_2):
        global now_time
        self.speed_x, self.speed_y = self.speed
        self.rect.x -= self.speed_x
        self.rect.y -= self.speed_y
        if self.rect.y <= 0 or self.rect.y >= 490:
            self.speed_y *= -1.1
        if (self.rect.colliderect(player_1) or self.rect.colliderect(player_2)) and timer() - now_time > 1:
            self.speed_x *= -1.1
            now_time = timer()
        self.speed = (self.speed_x, self.speed_y)
        self.show_sprite()


player_1 = Player(50, 225, 'rocket.png', 20, 10, 50)
player_2 = Player(450, 225, 'rocket.png', 20, 10, 50)
ball = Ball(245, 245, 'ball.png', (5, 5), 10, 10)
FPS = 60

font = font.Font(None, 50)

while is_playing:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            is_playing = False
    ball.update(player_1, player_2)
    player_1.update(1)
    player_2.update(2)
    player_1.show_sprite()
    player_2.show_sprite()
    if ball.rect.x <= 10:
        is_playing = False
        win = 'Player 2'
    elif ball.rect.x >= 490:
        is_playing = False
        win = 'Player 1'
    ball.speed = (ball.speed_x, ball.speed_y)
    time.delay(50)
    display.update()

else:
    if win:
        window.blit(background, (0, 0))
        win = font.render((win + ' won!'), True, (255, 0, 0))
        window.blit(win, (150, 225))
        display.update()
        time.delay(5000)