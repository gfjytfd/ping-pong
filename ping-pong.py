from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(
            player_image), (wight, height))  # разом 55,55 - параметри
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, 
                        win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

player_l = Player("racket.png", 30, 200,
                4, 50, 150)
player_r = Player("racket.png", 520, 200,
                4, 50, 150)
ball = GameSprite("tenis_ball.png", 200,
                200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose_l = font.render(
    "Player on the left lost",
    1, (180, 0, 0))
lose_r = font.render(
    "Player on the right lost",
    1, (180, 0, 0))
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)
        player_l.update_l()
        player_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if (
        sprite.collide_rect(player_l, ball)
        or sprite.collide_rect(player_r, ball)
        ):
            speed_x *= -1
            speed_y *= -1
        if (
        ball.rect.y > win_height - 50
        or ball.rect.y < 0
        ):
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_l, (100, 200))
            game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose_r, (100, 200))
            game_over = True
        player_l.reset()
        player_r.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)                                                                                                                              
                                                                                              
   