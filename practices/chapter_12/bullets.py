"""子弹的属性模块"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):  # 编组要继承Sprite类

    def __init__(self, ai_settings, screen, ship):  # 传参和设置参数顺序没管, 出错了, 然后就懵逼了. 啊天呐!
        """初始化子弹的属性"""
        super(Bullet, self).__init__()

        # 生成子弹的矩形
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        # 定义后面函数需用到的属性
        self.speed = ai_settings.bullet_speed  # 步幅
        self.color = ai_settings.bullet_color
        self.screen = screen

        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top
        self.screen_rect = screen.get_rect()

        self.y = float(self.rect.y)
        self.bullet_fired = False
        self.out_range = False

    def draw_bullet(self):
        """画在screen上, 调用到gf模块的update_screen()函数内部, 但是不能一直射, 故应该绑定space的event."""
        pygame.draw.rect(self.screen, self.color, self.rect)  # 函数和画图片的不同

    def update(self):
        """子弹一直垂直向上移动, 不受按键控制, 只跟边缘条件有关"""
        if self.rect.top >= self.screen_rect.top:
            self.y -= self.speed  # 这里写成+=了, 注意习惯,坐标系原点在左上角.
            self.rect.y = self.y
        else:
            self.out_range = True





