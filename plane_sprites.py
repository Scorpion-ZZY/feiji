import random

import pygame

# 指定屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机进精灵"""

    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1, 5)
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(1, SCREEN_RECT.width-self.rect.width)


    def update(self, *args):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕.需要从精灵组删除")
