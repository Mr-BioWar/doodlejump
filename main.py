# Импортируем библиотеку pygame
import pygame, classes, constant, time, random


def draw_menu(background, num_button, music_on):
    background.blit(constant.image_menu_background, (0, 0))
    if num_button == 1:
        background.blit(constant.image_menu_down_button_game, (constant.GAME_BUTTON_MIN_X, constant.GAME_BUTTON_MIN_Y))
    else:
        background.blit(constant.image_menu_button_game, (constant.GAME_BUTTON_MIN_X, constant.GAME_BUTTON_MIN_Y))
    if num_button == 2:
        background.blit(constant.image_menu_down_button_skin, (constant.SKIN_BUTTON_MIN_X, constant.SKIN_BUTTON_MIN_Y))
    else:
        background.blit(constant.image_menu_button_skin, (constant.SKIN_BUTTON_MIN_X, constant.SKIN_BUTTON_MIN_Y))
    if music_on:
        background.blit(constant.image_menu_down_button_music, (constant.MUSIC_BUTTON_MIN_X, constant.MUSIC_BUTTON_MIN_Y))
    else:
        background.blit(constant.image_menu_button_music, (constant.MUSIC_BUTTON_MIN_X, constant.MUSIC_BUTTON_MIN_Y))


def draw_skin(background, num_button):
    global skin_number
    background.blit(constant.image_skin_background, (0, 0))
    background.blit(constant.image_skin_button_skin1, (constant.SKIN_1_BUTTON_MIN_X, constant.SKIN_1_BUTTON_MIN_Y))
    background.blit(constant.image_skin_button_skin2, (constant.SKIN_2_BUTTON_MIN_X, constant.SKIN_2_BUTTON_MIN_Y))
    background.blit(constant.image_skin_button_skin3, (constant.SKIN_3_BUTTON_MIN_X, constant.SKIN_3_BUTTON_MIN_Y))

    if skin_number == 1:
        background.blit(constant.image_skin_down_button_skin1, (constant.SKIN_1_BUTTON_MIN_X, constant.SKIN_1_BUTTON_MIN_Y))
    elif skin_number == 2:
        background.blit(constant.image_skin_down_button_skin2, (constant.SKIN_2_BUTTON_MIN_X, constant.SKIN_2_BUTTON_MIN_Y))
    elif skin_number == 3:
        background.blit(constant.image_skin_down_button_skin3, (constant.SKIN_3_BUTTON_MIN_X, constant.SKIN_3_BUTTON_MIN_Y))

    if num_button == 4:
        background.blit(constant.image_skin_down_button_esc, (constant.SKIN_ESC_BUTTON_MIN_X, constant.SKIN_ESC_BUTTON_MIN_Y))
    else:
        background.blit(constant.image_skin_button_esc, (constant.SKIN_ESC_BUTTON_MIN_X, constant.SKIN_ESC_BUTTON_MIN_Y))


def draw_highscore(background, score):
    myfont = pygame.font.SysFont('ocrastd', 40)
    f = myfont.render(str(score), True, (0, 255, 255))
    if score < 100000:
        for item, elem in enumerate([5000, 10000, 30000, 50000, 100000]):
            if score < elem:
                background.blit(constant.image_lv_list[item], (1520, 0))
                break
    else:
        background.blit(constant.image_lv_list[5], (1520, 0))
    background.blit(f, (1900 - myfont.size(str(score))[0], 20))


def draw_game_over(background, highscore):
    background.blit(constant.image_dead, (0, 0))
    myfont = pygame.font.SysFont('ocrastd', 80)
    f = myfont.render(str(highscore), True, (0, 255, 255))
    background.blit(f, (960 - myfont.size(str(highscore))[0] // 2, 630))


def random_class(highscore):
    random.seed()
    number = random.randint(1, 100)

    answer = classes.PlatformHard

    lst = [[5000, [81, 96, 98]], [10000, [76, 88, 95]], [30000, [61, 71, 85]], [50000, [61, 66, 83]],
           [100000, [41, 44, 78]], [100000000, [11, 11, 46]]]
    for score, temp_lst in lst:
        if highscore < score:
            if number < temp_lst[0]:
                answer = classes.Platform
            elif number < temp_lst[1]:
                answer = classes.PlatformJump
            elif number < temp_lst[2]:
                answer = classes.PlatformCrash
            else:
                answer = classes.PlatformHard
            break

    return answer


def generate_platform(platform, score):

    x,y = platform.x, platform.y
    random.seed()

    if random.random() < 0.5:
        if y > 400:
            return [random_class(score)(random.randint(100, 1620), random.randint(-200, 0))]
        return [random_class(score)(random.randint(100, 1620), random.randint(y - 480, y - 400))]

    if y - 400 > 0:
        return [random_class(score)(random.randint(-100, 510), random.randint(-200, 0)),
                random_class(score)(random.randint(960, 1620), random.randint(-200, 0))]

    return [random_class(score)(random.randint(-100, 510), random.randint(y - 495, y - 450)),
            random_class(score)(random.randint(960, 1620), random.randint(y - 495, y - 450))]


def first_generate_platforms():
    platformss = []
    platformss.append(classes.PlatformFirst(710, 1000))
    platformss.append(classes.Platform(1210, 600))
    platformss.append(classes.Platform(210, 600))
    platformss.append(classes.Platform(710, 200))
    return platformss


def process_event(game_mode, event, background):
    global screen, music_off, highscore, gg, platforms, skin_number, game_background_y

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        if game_mode in ['menu', 'skin']:
            background.blit(constant.image_esc_background, (0, 0))
            screen.blit(background, (0, 0))
            pygame.display.update()
            time.sleep(5)
            raise (SystemExit, "QUIT")
        elif game_mode in ['game', 'game over']:
            draw_menu(background, 0, music_off)
            if not music_off:
                pygame.mixer.music.load('C:\\Users\\User\\PycharmProjects\\20.04.22[doodlejump]\\music\\Menu_theme.mp3')
                pygame.mixer.music.play(-1)
            else:
                pygame.mixer.music.stop()
            game_mode = 'menu'

    if game_mode == 'menu':
        if event.type == 5:
            x, y = pygame.mouse.get_pos()
            if constant.GAME_BUTTON_MIN_X < x < constant.GAME_BUTTON_MAX_X and\
                constant.GAME_BUTTON_MIN_Y < y < constant.GAME_BUTTON_MAX_Y:
                draw_menu(background, 1, music_off)
                pygame.mixer.Sound.play(constant.sound_button)
                return game_mode
            if constant.SKIN_BUTTON_MIN_X < x < constant.SKIN_BUTTON_MAX_X and\
                constant.SKIN_BUTTON_MIN_Y < y < constant.SKIN_BUTTON_MAX_Y:
                draw_menu(background, 2, music_off)
                pygame.mixer.Sound.play(constant.sound_button)
                return game_mode
            if constant.MUSIC_BUTTON_MIN_X < x < constant.MUSIC_BUTTON_MAX_X and\
                constant.MUSIC_BUTTON_MIN_Y < y < constant.MUSIC_BUTTON_MAX_Y:
                music_off = not music_off
                draw_menu(background, 0, music_off)
                pygame.mixer.Sound.play(constant.sound_button)
                if music_off: pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1)
                return game_mode
        elif event.type == 6:
            draw_menu(background, 0, music_off)
            x, y = pygame.mouse.get_pos()
            if constant.GAME_BUTTON_MIN_X < x < constant.GAME_BUTTON_MAX_X and\
                constant.GAME_BUTTON_MIN_Y < y < constant.GAME_BUTTON_MAX_Y:
                highscore = 0
                gg = classes.GG(skin_number)
                platforms = first_generate_platforms()
                game_background_y = -1080
                if not music_off:
                    pygame.mixer.music.load('C:\\Users\\User\\PycharmProjects\\20.04.22[doodlejump]\\music\\Game_theme.mp3')
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
                return 'game'
            if constant.SKIN_BUTTON_MIN_X < x < constant.SKIN_BUTTON_MAX_X and\
                constant.SKIN_BUTTON_MIN_Y < y < constant.SKIN_BUTTON_MAX_Y:
                draw_skin(background, 0)
                return 'skin'

    elif game_mode == 'skin':
        if event.type == 5:
            x, y = pygame.mouse.get_pos()
            if constant.SKIN_1_BUTTON_MIN_X < x < constant.SKIN_1_BUTTON_MAX_X and\
                constant.SKIN_1_BUTTON_MIN_Y < y < constant.SKIN_1_BUTTON_MAX_Y:
                skin_number = 1
                draw_skin(background, 1)
                pygame.mixer.Sound.play(constant.sound_button)
                return game_mode
            if constant.SKIN_2_BUTTON_MIN_X < x < constant.SKIN_2_BUTTON_MAX_X and\
                constant.SKIN_2_BUTTON_MIN_Y < y < constant.SKIN_2_BUTTON_MAX_Y:
                skin_number = 2
                draw_skin(background, 2)
                pygame.mixer.Sound.play(constant.sound_button)
                return game_mode
            if constant.SKIN_3_BUTTON_MIN_X < x < constant.SKIN_3_BUTTON_MAX_X and\
                constant.SKIN_3_BUTTON_MIN_Y < y < constant.SKIN_3_BUTTON_MAX_Y:
                skin_number = 3
                draw_skin(background, 3)
                pygame.mixer.Sound.play(constant.sound_button)
                return game_mode
            if constant.SKIN_ESC_BUTTON_MIN_X < x < constant.SKIN_ESC_BUTTON_MAX_X and\
                constant.SKIN_ESC_BUTTON_MIN_Y < y < constant.SKIN_ESC_BUTTON_MAX_Y:
                draw_skin(background, 4)
                pygame.mixer.Sound.play(constant.sound_button)
                return game_mode
        if event.type == 6:
            draw_skin(background, 0)
            x, y = pygame.mouse.get_pos()
            if constant.SKIN_1_BUTTON_MIN_X < x < constant.SKIN_1_BUTTON_MAX_X and\
                constant.SKIN_1_BUTTON_MIN_Y < y < constant.SKIN_1_BUTTON_MAX_Y:

                draw_skin(background, 0)
                return game_mode
            if constant.SKIN_2_BUTTON_MIN_X < x < constant.SKIN_2_BUTTON_MAX_X and\
                constant.SKIN_2_BUTTON_MIN_Y < y < constant.SKIN_2_BUTTON_MAX_Y:
                draw_skin(background, 0)

                return game_mode
            if constant.SKIN_3_BUTTON_MIN_X < x < constant.SKIN_3_BUTTON_MAX_X and\
                constant.SKIN_3_BUTTON_MIN_Y < y < constant.SKIN_3_BUTTON_MAX_Y:
                draw_skin(background, 0)

                return game_mode
            if constant.SKIN_ESC_BUTTON_MIN_X < x < constant.SKIN_ESC_BUTTON_MAX_X and\
                constant.SKIN_ESC_BUTTON_MIN_Y < y < constant.SKIN_ESC_BUTTON_MAX_Y:
                draw_menu(background, 0, music_off)
                return 'menu'
    elif game_mode == 'game':
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            gg.jump_x(-1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            gg.jump_x(1)
        elif max(pygame.key.get_pressed()) < 1:
            gg.speed_x = 0

    return game_mode


def main():
    global screen, music_off, highscore, gg, platforms, skin_number, game_background_y

    game_mode = 'menu'
    music_off = False
    highscore = 0
    skin_number = 1
    gg = classes.GG(1)
    platforms = []
    game_background_y = -1080

    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(constant.DISPLAY, flags= pygame.FULLSCREEN)
    pygame.display.set_caption("Spacejump")
    background = pygame.Surface(constant.DISPLAY)
    draw_menu(background, 0, music_off)
    pygame.mixer.music.load('C:\\Users\\User\\PycharmProjects\\20.04.22[doodlejump]\\music\\Menu_theme.mp3')
    pygame.mixer.music.play(-1)

    while True:  # Основной цикл программы

        for e in pygame.event.get():
            game_mode = process_event(game_mode, e, background)

        if game_mode == 'game':
            # hero movement
            gg.move(constant.WIN_WIDTH, constant.WIN_HEIGHT)
            # platforms crashing
            a = list(map(lambda plat: plat.touch(gg), platforms))
            # camera movement
            camera_movement = 500 - gg.y if gg.y < 500 else 0
            gg.camera(camera_movement)
            a = list(map(lambda plat: plat.camera(camera_movement), platforms))

            highscore += camera_movement
            game_background_y = (1080 + game_background_y + camera_movement // 10) % 1080 - 1080
            # draw objects
            background.blit(constant.game_background_space, (0, 0))
            background.blit(constant.game_background, (0, game_background_y))
            a = list(map(lambda plat: plat.draw(background), platforms))
            gg.draw(background)

            draw_highscore(background, highscore)


            # platform's generation
            if min(platforms, key=lambda plat: plat.y).y > 0:
                platforms.extend(generate_platform(min(platforms, key=lambda plat: plat.y), highscore))
            platforms = list(filter(lambda plat: plat.y < 1080, platforms))

            if gg.death:
                draw_game_over(background, highscore)
                game_mode = 'game over'

        screen.blit(background, (0, 0))  # Каждую итерацию необходимо всё перерисовывать
        pygame.display.update()  # обновление и вывод всех изменений на экран
        clock.tick(45)


if __name__ == "__main__":
    main()