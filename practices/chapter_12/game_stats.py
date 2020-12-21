"""存储统计信息以供调用"""


class GameStats(object):
    """记录游戏统计信息"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()  # 为啥要费这二遍事呢, 因为我们有时候会手动调用reset ?
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏期间可能发生变化的信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.ai_settings.alien_speed_y = 0.05
        self.score = 0
        self.ai_settings.alien_points = 50
        self.level = 0
