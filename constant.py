import pygame


WIN_WIDTH = 1920  # Ширина создаваемого окна
WIN_HEIGHT = 1080  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#ffffff"
# кнопки меню
# кнопка игры
GAME_BUTTON_MIN_X = 675
GAME_BUTTON_MIN_Y = 208
GAME_BUTTON_MAX_X = 1175
GAME_BUTTON_MAX_Y = 408
# кнопка мкинов
SKIN_BUTTON_MIN_X = 675
SKIN_BUTTON_MIN_Y = 458
SKIN_BUTTON_MAX_X = 1175
SKIN_BUTTON_MAX_Y = 658
# кнопка звуков
MUSIC_BUTTON_MIN_X = 864
MUSIC_BUTTON_MIN_Y = 905
MUSIC_BUTTON_MAX_X = 864 + 113
MUSIC_BUTTON_MAX_Y = 905 + 113

# кнопки скинов
# кнопка скина 1
SKIN_1_BUTTON_MIN_X = 530
SKIN_1_BUTTON_MIN_Y = 308
SKIN_1_BUTTON_MAX_X = 730
SKIN_1_BUTTON_MAX_Y = 608
# кнопка скина 2
SKIN_2_BUTTON_MIN_X = 830
SKIN_2_BUTTON_MIN_Y = 308
SKIN_2_BUTTON_MAX_X = 1030
SKIN_2_BUTTON_MAX_Y = 608
# кнопка скина 3
SKIN_3_BUTTON_MIN_X = 1130
SKIN_3_BUTTON_MIN_Y = 308
SKIN_3_BUTTON_MAX_X = 1330
SKIN_3_BUTTON_MAX_Y = 608
# кнопка выхода в меню
SKIN_ESC_BUTTON_MIN_X = 675
SKIN_ESC_BUTTON_MIN_Y = 850
SKIN_ESC_BUTTON_MAX_X = 1175
SKIN_ESC_BUTTON_MAX_Y = 1050

# картинки для меню
image_menu_background = pygame.image.load('images/BG_MENU.png')

image_menu_button_game = pygame.image.load('images/GAME_BUTTON.png')
image_menu_button_skin = pygame.image.load('images/SKIN_BUTTON.png')
image_menu_button_music = pygame.image.load('images/MUSIK_ON1.png')

image_menu_down_button_game = pygame.image.load('images/GAME_BUTTON_DOWN.png')
image_menu_down_button_skin = pygame.image.load('images/SKIN_BUTTON_DOWN.png')
image_menu_down_button_music = pygame.image.load('images/MUSIK_OFF1.png')

#картинки для скинов
image_skin_background = pygame.image.load('images/BG_MENU.png')

image_skin_button_skin1 = pygame.image.load('images/SKIN1_BUTTON_OFF.png')
image_skin_button_skin2 = pygame.image.load('images/SKIN2_BUTTON_OFF.png')
image_skin_button_skin3 = pygame.image.load('images/SKIN3_BUTTON_OFF.png')
image_skin_button_esc = pygame.image.load('images/MENU_BUTTON.png')

image_skin_down_button_skin1 = pygame.image.load('images/SKIN1_BUTTON.png')
image_skin_down_button_skin2 = pygame.image.load('images/SKIN2_BUTTON.png')
image_skin_down_button_skin3 = pygame.image.load('images/SKIN3_BUTTON.png')
image_skin_down_button_esc = pygame.image.load('images/MENU_BUTTON_DOWN.png')

# выход
image_esc_background = pygame.image.load('images/ESCAPE.png')

# game background
game_background = pygame.image.load('images/GAME_BG2.png')
game_background_space = pygame.image.load('images/BG_BG.png')

image_platform_first = pygame.image.load('images/Platform_first.png')
image_platform = pygame.image.load('images/Platform.png')
image_platform_crash = pygame.image.load('images/Platform_crash.png')
image_platform_crash_off = pygame.image.load('images/Platform_crash_off.png')
image_platform_jump = pygame.image.load('images/Platform_jump.png')
image_platform_hard = pygame.image.load('images/Platform_hard.png')

image_lv_list = [pygame.image.load('images/LV_1.png'), pygame.image.load('images/LV_2.png'),
                 pygame.image.load('images/LV_3.png'), pygame.image.load('images/LV_4.png'),
                 pygame.image.load('images/LV_5.png'), pygame.image.load('images/LV_6.png'),]

#dead
image_dead = pygame.image.load('images/Dead.png')


pygame.mixer.init()
sound_button = pygame.mixer.Sound('C:\\Users\\User\\PycharmProjects\\20.04.22[doodlejump]\\music\\button.wav')
sound_jump = pygame.mixer.Sound('C:\\Users\\User\\PycharmProjects\\20.04.22[doodlejump]\\music\\jump.wav')
sound_hjump = pygame.mixer.Sound('C:\\Users\\User\\PycharmProjects\\20.04.22[doodlejump]\\music\\hjump.wav')
sound_ljump = pygame.mixer.Sound('C:\\Users\\User\\PycharmProjects\\20.04.22[doodlejump]\\music\\ljump.wav')
