"""配置文件,相当于之前tkinter项目的configuration"""


class Settings(object):
    """储存外星人入侵游戏所有的设置参数"""
    def __init__(self):
        """初始化游戏的设置"""
        self.screen_width = 1400
        self.screen_height = 960
        self.bg_color = (230, 230, 230)

        # 飞船速度, 即每一次移动的步幅.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的参数们
        self.bullet_speed = 1.5
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 60, 100, 40
        self.bullets_allowed = 3

        # 外星人的参数
        self.first_ship_position_x = 150
        self.first_ship_position_y = 100
        self.alien_speed_x = 0.8
        self.alien_speed_y = 0.08
        self.alien_direction = 1
        self.alien_points = 50

