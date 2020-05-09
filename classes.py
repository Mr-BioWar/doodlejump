import pygame, constant


class GG(object):
    def __init__(self, skin_number):
        self.x, self.y = 960, 850
        self.height, self.width = 125, 46
        self.image = pygame.image.load('images\Body_GG{0}_right.png'.format(skin_number))
        self.image_r = pygame.image.load('images\Body_GG{0}_right.png'.format(skin_number))
        self.image_l = pygame.image.load('images\Body_GG{0}_left.png'.format(skin_number))
        self.skin_number = skin_number
        self.speed_x, self.speed_y = 0, 0
        self.g = -9
        self.add_x, self.add_y = 55, -95
        self.death = False


    def draw(self, background):
        background.blit(self.image, (self.x - self.width, self.y - self.height))

    def jump_y(self, mult=1):
        self.speed_y = mult * self.add_y

    def jump_x(self, direction):
        self.speed_x = direction * self.add_x
        self.image = self.image_r if direction > 0 else self.image_l

    def move(self, w, h):
        self.y += self.speed_y
        self.x += self.speed_x
        self.speed_y -= self.g

        if self.x > w + self.width:
            self.x = -self.width
        if self.x < -self.width:
            self.x = w + self.width

        if self.y > h + self.height:
            self.death = True

    def camera(self, y):
        self.y += y


class Platform(object):
    def __init__(self, x, y):
        self.width = 450
        self.image = constant.image_platform
        self.x, self.y = x, y

    def camera(self, y):
        self.y += y

    def draw(self, background):
        background.blit(self.image, (self.x, self.y))

    def touch(self, hero):
        if hero.y <= self.y < hero.y + hero.speed_y and (
                hero.x + hero.width >= self.x and hero.x - hero.width <= (self.x + self.width)):
            hero.y = self.y
            hero.jump_y()
            pygame.mixer.Sound.play(constant.sound_jump)


class PlatformFirst(Platform):
    def __init__(self, x, y):
        self.width = 500
        self.image = constant.image_platform_first
        self.x, self.y = x, y


class PlatformCrash(Platform):
    def __init__(self, x, y):
        self.width = 450
        self.x, self.y = x, y
        self.image = constant.image_platform_crash
        self.untouched = True

    def draw(self, background):
        background.blit(self.image, (self.x, self.y - 37))


    def touch(self, hero):
        if hero.y <= self.y < hero.y + hero.speed_y and (
                hero.x + hero.width >= self.x and hero.x - hero.width <= (self.x + self.width)) and self.untouched:
            hero.jump_y()
            hero.y = self.y
            self.untouched = False
            self.image = constant.image_platform_crash_off
            pygame.mixer.Sound.play(constant.sound_ljump)


class PlatformHard(Platform):
    def __init__(self, x, y):
        self.width = 450
        self.x, self.y = x, y
        self.image = constant.image_platform_hard

    def touch(self, hero):
        if hero.y <= self.y < hero.y + hero.speed_y and (
                hero.x + hero.width >= self.x and hero.x - hero.width <= (self.x + self.width)):
            hero.y = self.y
            hero.jump_y()
            pygame.mixer.Sound.play(constant.sound_jump)
        
        if hero.y - hero.height >= self.y + 100 > hero.y - hero.height + hero.speed_y and (
                hero.x + hero.width >= self.x and hero.x - hero.width <= (self.x + self.width)):
            hero.y = self.y + 100 + hero.height
            hero.speed_y = 0


class PlatformJump(Platform):
    def __init__(self, x, y):
        self.width = 450
        self.x, self.y = x, y
        self.image = constant.image_platform_jump


    def draw(self, background):
        background.blit(self.image, (self.x, self.y - 152))


    def touch(self, hero):
        if self.y >= hero.y and self.y < hero.y + hero.speed_y and (
                hero.x + hero.width >= self.x and hero.x - hero.width <= (self.x + self.width)):
            hero.y = self.y
            hero.jump_y(mult=2)
            pygame.mixer.Sound.play(constant.sound_hjump)


class Boss(GG):
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.height, self.width = 10, 5
        self.image = None
        self.speed_x = 0
        self.add_x = 4
        self.death = False

    def target(self, hero):
        if hero.x > self.x:
            self.jump_x(direction=1)
        if hero.x < self.x:
            self.jump_x(direction=-1)


class Dialog(object):
    def __init__(self, head_1, head_2):
        self.background_image = None
        self.head_1_image = None
        self.head_2_image = None
        self.text = ''
        self.num_head = -1
        self.shawn = True

    def draw(self):
        if self.shawn:
            pass

    def disappear(self):
        self.shawn = False

    def next_phrase(self, text):
        self.num_head *= -1
        self.text = text