import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()#创建实例时原类对象一定要带括号

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创造一艘飞船
    ship = Ship(screen)
    #开始生成游戏的主循环
    while True:
        for event in pygame.event.get():#监视鼠标和键盘事件
            if event.type == pygame.QUIT:
                sys.exit()
        # 设置背景颜色
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()



run_game()

