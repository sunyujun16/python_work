"""我是主程序"""

import pygame
from setttings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from buttons import Button
from scoreboard import ScoreBoard


def run_game():
    """初始化游戏并新建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("干死那帮外星人")

    # 创建飞船实例 / 子弹编组 / 飞碟编组
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()

    # 创建舰队
    gf.create_fleet(ai_settings, aliens, screen, ship)

    # 创建统计信息实例
    stats = GameStats(ai_settings)

    play_button = Button(screen, ai_settings, "Let's fuck them")

    sb = ScoreBoard(screen, ai_settings, stats)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens, bullets, ai_settings, ship, screen, stats, sb)
            gf.update_aliens(aliens, ship, stats, ai_settings, screen, bullets, sb)
        # else:
        #     pass
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb)


run_game()
