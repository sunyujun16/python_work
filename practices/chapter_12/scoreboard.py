import pygame
from ship import Ship
from pygame.sprite import Group


class ScoreBoard(object):
    """记分牌"""
    def __init__(self, screen, ai_settings, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (100, 70, 30)
        self.font = pygame.sysfont.SysFont('Ubuntu Mono', 30)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """从统计信息获取当前得分, 并将得分转换为渲染的图像"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)  # 这个就死记硬背得了,数字转字符串在千位加逗号分割.

        self.score_image = self.font.render(score_str, False, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def show_score(self):
        """画在屏幕上"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高分渲染为图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, False, self.text_color,
                                                 self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.top = 10
        self.high_score_rect.centerx = self.screen_rect.centerx

    def prep_level(self):
        level = self.stats.level
        level_str = str(level)
        self.level_image = self.font.render(level_str, False, self.text_color,
                                           self.ai_settings.bg_color)
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for i in range(self.stats.ships_left):
            ship = Ship(self.screen, self.ai_settings)  # 这里就比较活用了, 要留下印象.
            ship.rect.x = 10 + i * (ship.rect.width+10)
            ship.rect.top = 10
            self.ships.add(ship)

            pass


