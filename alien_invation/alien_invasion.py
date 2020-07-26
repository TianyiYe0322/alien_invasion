#import sys

import pygame
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()#创建实例时原类对象一定要带括号
    #创造一定尺寸的屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创造一艘飞船（外形、位置）
    ship = Ship(ai_settings,screen)
    #开始生成游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)




run_game()

