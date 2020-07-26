import sys

import pygame

def check_events(ship):
    """相应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像并切换到新屏幕"""
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)#上颜色
    ship.blitme()#画飞船
    #擦去旧屏幕，让最近绘制的屏幕可见
    pygame.display.flip()