import pygame
from pygame import sysfont


class Button(object):
    """创建按钮"""
    def __init__(self, screen, ai_settings, msg):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 设计按钮的属性/特征
        self.width, self.height = 200, 50
        self.button_color = 200, 255, 200
        self.text_color = 100, 100, 255

        self.font = pygame.sysfont.SysFont('Ubuntu Mono', 24)

        # 创建按钮的结界, 即rect对象, 并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染成图像, 并将其在按钮上居中"""
        pass
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)





