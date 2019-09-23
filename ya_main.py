import sys
from plane_sprites import *


# pygame.init()
# coord_x = 210
# coord_y = 500
# coordTow_y = 700
# pygame.display.set_caption("飞机大战")
# mode = pygame.display.set_mode((480, 700))
# bg = pygame.image.load("./images/background.png")
# yingxiong = pygame.image.load("./images/life.png")
# enemy = GameSprite("./images/enemy1.png")
# enemy_group = pygame.sprite.Group(enemy)
# clock = pygame.time.Clock()
# while True:
#     clock.tick(60)
#     # mode.blit(enemy.image, enemy.rect.x, enemy.rect.y)
#
#     for eve_list in pygame.event.get():
#         if eve_list.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     mode.blit(bg, (0, 0))
#     enemy_group.update()
#     enemy_group.draw(mode)
#     if coord_y > -57:
#         mode.blit(yingxiong, (coord_x, coord_y))
#         coord_y -= 1
#     if -65 < coord_y < 0:
#         mode.blit(yingxiong, (coord_x, coordTow_y))
#         coordTow_y -= 1
#         if coordTow_y == 625:
#             coord_y = 625
#             coordTow_y = 700
#     pygame.display.update()
# pygame.quit()
class PlanGame:
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化...")
        # 创建主屏幕对象
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建时钟对象 设置帧率
        self.clock = pygame.time.Clock()
        # 运行精灵及精灵组的创建
        self.__create_sprites()

    def start_game(self):
        print("游戏开始...")

        while True:
            # 设置刷新帧率
            self.clock.tick(60)
            #  事件监听
            self.__event_handler()
            #  碰撞检测
            self.__check_collide()
            #  更新绘制精灵组
            self.__update_sprites()
            #   更新显示
            pygame.display.update()

    def __create_sprites(self):
        # 创建背景精灵 和精灵组
        # bg1 = Background("./images/background.png")
        bg1 = Background()
        # bg2 = Background("./images/background.png")
        bg2 = Background(True)
        # bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlanGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    PlanGame = PlanGame()
    PlanGame.start_game()
