"""这是游戏主程序用到的函数"""
import sys
import pygame
from bullets import Bullet
from aliens import Alien
from time import sleep


def fire_in_the_hole(ai_settings, screen, ship, bullets):
    # 调用时开枪, 即实例化一发子弹
    if len(bullets) <= 4:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)


def remove_out_bullet(bullets):
    # 调用时把屏幕边缘的子弹移除, 注意for循环对列表进行删除操作的方式
    for bullet in bullets.copy():
        if bullet.out_range:
            bullets.remove(bullet)


def update_bullets(aliens, bullets, ai_settings, ship, screen, stats, sb):
    # 主程序函数, 用于集合/调用子弹相关操作
    bullets.update()
    remove_out_bullet(bullets)
    # 检查子弹和飞碟碰撞
    check_bullet_alien_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb)


def check_bullet_alien_collisions(bullets, aliens, ai_settings, screen, ship, stats, sb):
    # 这里赋值了, 我想后面设置分数要用这个字典的len(dict.keys()).  --想屁吃呢? 赋值是为了判断以更新分数.  --光速打脸!
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # True表示要干死一个.

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()  # 更新分数信息, 这就是把它单独写一个函数的原因.
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, aliens, screen, ship)
        ai_settings.alien_speed_y += 0.08
        ai_settings.alien_points += 25
        stats.level += 1
        sb.prep_level()


def key_up(event, ship):     
    """与key_down()同理"""
    if event.key == pygame.K_RIGHT:
        # 停止向右移动
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # 停止向左移动
        ship.moving_left = False


def key_down(event, ship, bullets, ai_settings, screen, stats, aliens, sb):
    """下面的check_events函数在发现Key_down时触发本函数, 用以定义各种按键发生时程序的动作"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        if not stats.game_active:
            reset_all(stats, aliens, bullets, ai_settings, screen, ship, sb)
        else:
            fire_in_the_hole(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def reset_all(stats, aliens, bullets, ai_settings, screen, ship, sb):
    stats.reset_stats()
    stats.game_active = True

    pygame.mouse.set_visible(False)

    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings, aliens, screen, ship)
    ship.center_ship()

    # 重置一下记分牌..."的图像参数", 以免在下次触发写入参数之前一动不动的像王八.
    sb.prep_score()
    sb.prep_level()
    sb.prep_ships()


def check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens, sb):
    """响应鼠标键盘事件, 并让飞船做出反应"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key_down(event, ship, bullets, ai_settings, screen, stats, aliens, sb)
        elif event.type == pygame.KEYUP:
            key_up(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_buttons(play_button, stats, mouse_x, mouse_y, aliens, bullets,
                               ai_settings, screen, ship, sb)


def check_play_buttons(play_button, stats, mouse_x, mouse_y, aliens, bullets, ai_settings,
                       screen, ship, sb):
    if play_button.rect.collidepoint(mouse_x, mouse_y)\
            and not stats.game_active:
        reset_all(stats, aliens, bullets, ai_settings, screen, ship, sb)


def update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button, sb):
    """重新绘制屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # ship的函数, 功能是往screen上画ship, 它将跟随整个函数被调往主模块中运行, blit本意为位块传送
    # aliens.draw(screen)
    for alien in aliens.sprites():
        alien.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if not stats.game_active:
        play_button.draw_button()

    sb.show_score()
    # 让最近的绘制变得可见, "翻面", 这是本项目范围内让surfaces显示到屏幕上的最终一行代码.
    pygame.display.flip()


def get_number_aliens_x(ai_settings, screen):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_aliens_row(ai_settings, alien_height, ship):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship.rect.height
    number_aliens_row = int(available_space_y / (4 * alien_height))
    return number_aliens_row


def create_alien(ai_settings, screen, aliens, i, j):
    """创建一个外星人并加入舰队"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = ai_settings.first_ship_position_x + 2 * alien_width * i
    alien.rect.x = alien.x
    alien.y = ai_settings.first_ship_position_y +\
              2 * alien.rect.height * j  # 这一步及其关键!!! 真是隐蔽啊...编程这东西, 太危险了.
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, aliens, screen, ship):
    """创建舰队"""
    alien = Alien(ai_settings, screen)  # 实例仅仅是为了向rows()函数传参alien.rect.height. 其实可以不这么写,参考行函数.
    number_aliens_x = get_number_aliens_x(ai_settings, screen)
    number_aliens_rows = get_number_aliens_row(ai_settings, alien.rect.height, ship)
    for i in range(number_aliens_x):
        for j in range(number_aliens_rows):
            create_alien(ai_settings, screen, aliens, i, j)


def update_aliens(aliens, ship, stats, ai_settings, screen, bullets, sb):
    aliens.update()  # 这里和教材不一样, 教材是整体撞墙反弹, 我是单个外星人撞墙反弹, 所以检测撞墙代码放在外星人类内部.

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(aliens, ship, stats, ai_settings, screen, bullets, sb)

    check_alien_bottom(aliens, ship, stats, ai_settings, screen, bullets, sb)


def check_alien_bottom(aliens, ship, stats, ai_settings, screen, bullets, sb):
    for alien in aliens.sprites():
        if alien.rect.bottom >= ai_settings.screen_height:
            ship_hit(aliens, ship, stats, ai_settings, screen, bullets, sb)
            break


def ship_hit(aliens, ship, stats, ai_settings, screen, bullets, sb):
    """飞船和飞碟相撞"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()

        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()
        ai_settings.alien_speed_y = 0.05
        ai_settings.alien_points = 50

        # 创建新的一群外星人, 并将飞船放置到中间.
        create_fleet(ai_settings, aliens, screen, ship)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        # stats.high_score = stats.score


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


'''
- 我的生成飞碟队列写法, 亲测有效, 不过这里还是遵循教材的写法, 以免后面思维混乱.
    # 实例化一次,以获得参数
    # number_alien_x = (ai_settings.screen_width - (2 * alien.rect.width)) // (2 * alien.rect.width)
    # number_alien_y = (ai_settings.screen_height - (2 * alien.rect.height)) // (2 * alien.rect.height)
    # for i in range(int(number_alien_x+1)):
    #     x = alien.rect.width
    #     x += float(alien.rect.width) * 2*i  # 这个+=是对x的初始值进行的
    #     for j in range(int(number_alien_y/2)):
    #         alien = Alien(ai_settings, screen)
    #         alien.rect.x = x
    #         alien.y += float(alien.rect.height) * 2*j  # 这个+=是对alien.y的初始值(构造函数得出)进行的.
    #         alien.rect.y = alien.y
    #         aliens.add(alien)
'''
