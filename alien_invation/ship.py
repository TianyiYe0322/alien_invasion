import pygame

class Ship():
    def __init__(self,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()#获取屏幕外接矩形
        #将每艘飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)#图没有位置而其外接矩形有位置，这里把图画到指定位置上，相当于通过外接矩形操作图
