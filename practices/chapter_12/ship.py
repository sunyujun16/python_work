"""飞船的基本行为在这里"""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        """初始化飞船,并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen  # 化妆成自有属性以便其他函数使用

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')  # 加载图像image,定义为self.image
        self.rect = self.image.get_rect()  # 获取self.image的外结界矩形,定义为self.rect
        self.screen_rect = screen.get_rect()  # 获取screen的结界,定义为self.screen_rect
        self.moving_right = False
        self.moving_left = False

        # 将每艘新船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx  # 获取screen的矩形的x值, 把它赋值给ship(self)的矩形.
        self.rect.bottom = self.screen_rect.bottom  # 获取screen_rect的x值,让self.rect与它相等.

        # 关联settings里的参数
        self.ai_settings = ai_settings

        # 自定义一个飞船的center参数, 用于以浮点数储存位置, 因为pycharm自带的centerx等不支持浮点数
        self.center = float(self.rect.centerx)

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 参考结界self.rect的值, 把ship.image画在screen上.

    def update(self):
        """检测moving_xxx的值, 从而更新ship位置. 至于moving_xxx值是啥, gf模块的check_event说了算"""
        if self.moving_right and self.rect.centerx <= self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.centerx > self.screen_rect.right:
            self.center = 0
        # 到屏幕另一端, 我自己做的改动.
        if self.moving_left and self.rect.centerx >= 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx < 0:
            self.center = self.screen_rect.right

        self.rect.centerx = self.center  # 浮点数溜达一圈到这步又被取消, 但是运行时还有效, 嘶~.

    def center_ship(self):
        self.center = self.screen_rect.centerx
        # 注意这里为什么必须写self.center, 因为它是我们在update中用来给self.rect.centerx赋值的变量. 如果不这么写,而是直接
        # 给self.rect.centerx赋值, 等到update时, 它就又被原有的self.center给赋值了, 我们赋的值屁用没有就被擦写掉了.

