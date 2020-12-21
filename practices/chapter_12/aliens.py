"""我就非要在这儿写点啥"""
import pygame
import random
from pygame.sprite import Sprite


class Alien(Sprite):
    """一个外星人的类, 注意, 凡是要编组的都是Sprite的子类"""
    def __init__(self, ai_settings, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings

        # 导入外星人飞碟图像, 获取结界
        self.image = pygame.image.load('images/a3.bmp')
        self.image.set_colorkey((230, 230, 230))  # 设置透明色
        self.rect = self.image.get_rect()
        # pygame.transform.scale(self.img, (self.rect.width // 5, self.rect.height // 2)

        # 初始化飞碟位置, at 每次实例化
        self.rect.x = ai_settings.first_ship_position_x
        self.rect.y = ai_settings.first_ship_position_y

        # 存储飞碟的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.direction = 1

    def blitme(self):
        """画飞碟, 及其单纯的功能, 就是'画飞碟'."""
        self.screen.blit(self.image, self.rect)
        pass

    def check_edge(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            self.direction *= -1
        return self.direction

    def update(self):
        """更新外星人飞碟的位置参数, 继承Sprite类就是为了这个函数能够被aliens.update()语句调用"""
        a = self.check_edge()
        '''
        小记:direction如果调用ai_settings的属性的话, 就会导致其他飞船的方向一起被更改, 而且混乱, 按说不应该呀, 啊我明白了
        ,所有飞碟实例的.ai_settings.alien_direction属性是指向同一个存储id的, 牵一发而动全身.看jupyter notebook第十三章
        的试验.那么这里就只能改为飞碟类自身的属性,这样才能让每个子类都储存不同的方向.那么之前的晃动是怎么回事呢? 唉~先pass吧.
        '''
        self.x += float(self.ai_settings.alien_speed_x * a)
        self.rect.x = self.x
        self.y += float(self.ai_settings.alien_speed_y)
        self.rect.y = self.y
        pass



