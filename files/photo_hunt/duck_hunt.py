import pygame
import random
import os

pygame.init()

screen_width = 1920
screen_height = 1080

file_dir = os.path.dirname(__file__)
pygame.mixer.music.load(f'{file_dir}/background_music.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

birds_sound = pygame.mixer.Sound(f'{file_dir}/birds_sound.mp3')
leaves_sound = pygame.mixer.Sound(f'{file_dir}/shelest_listvy.mp3')
camera_sound = pygame.mixer.Sound(f'{file_dir}/camera_sound.wav')

background_music_channel = pygame.mixer.Channel(0)
birds_sound_channel = pygame.mixer.Channel(1)

background_music_channel.play(pygame.mixer.Sound(f'{file_dir}/birds_sound.mp3'), loops=-1)
background_music_channel.set_volume(0.2)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Фотоохота")

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (234, 255, 0)

score = 0


class Duck:
    def __init__(self):
        self.name = 'Утка'

        self.duck_rect = pygame.Rect(0, 0, 0, 0)

        self.duck_image_1, self.duck_image_2, self.duck_image_3, self.duck_image_4 = (pygame.image.load(f'{file_dir}/duck1.png'),
                                                                                      pygame.image.load(f'{file_dir}/duck2.png'),
                                                                                      pygame.image.load(f'{file_dir}/duck3.png'),
                                                                                      pygame.image.load(f'{file_dir}/duck4.png'))
        self.duck_images = [self.duck_image_1, self.duck_image_2, self.duck_image_3, self.duck_image_4]

        self.current_duck_index = 0

        self.duck_rect = self.duck_images[self.current_duck_index].get_rect()

        self.duck_rect.y = random.randint(100, screen_height - 350)

        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.duck_rect.x = -100
        else:
            self.duck_rect.x = screen_width - 150

        self.clock = pygame.time.Clock()
        self.duck_animation_timer = pygame.time.get_ticks()
        self.bush_animation_timer = pygame.time.get_ticks()

        if self.direction == 1:
            self.duck_images = [pygame.transform.flip(self.duck_image_1, True, False),
                                pygame.transform.flip(self.duck_image_2, True, False),
                                pygame.transform.flip(self.duck_image_3, True, False),
                                pygame.transform.flip(self.duck_image_4, True, False),
                                pygame.transform.flip(self.duck_image_3, True, False),
                                pygame.transform.flip(self.duck_image_2, True, False),
                                pygame.transform.flip(self.duck_image_1, True, False)]
        else:
            self.duck_images = [self.duck_image_1, self.duck_image_2, self.duck_image_3, self.duck_image_4,
                                self.duck_image_3, self.duck_image_2, self.duck_image_1]

    def update(self, current_time):
        self.duck_animation_timer = current_time
        self.current_duck_index += 1
        if self.current_duck_index > len(self.duck_images) - 1:
            self.current_duck_index = 0

        if self.duck_rect.left > screen_width or self.duck_rect.right < 0:
            place()

    def images(self):
        duck_images = self.duck_images
        duck_rect = self.duck_rect
        return duck_images, duck_rect


class Vorobey:
    def __init__(self):
        self.name = 'Воробей'

        self.duck_rect = pygame.Rect(0, 0, 0, 0)

        self.duck_image_1, self.duck_image_2, self.duck_image_3, self.duck_image_4 = (pygame.image.load(f'{file_dir}/vorobey1.png'),
                                                                                      pygame.image.load(f'{file_dir}/vorobey2.png'),
                                                                                      pygame.image.load(f'{file_dir}/vorobey3.png'),
                                                                                      pygame.image.load(f'{file_dir}/vorobey4.png'))
        self.duck_images = [self.duck_image_1, self.duck_image_2, self.duck_image_3, self.duck_image_4]

        self.current_duck_index = 0

        self.duck_rect = self.duck_images[self.current_duck_index].get_rect()

        self.duck_rect.y = random.randint(100, screen_height - 350)

        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.duck_rect.x = -100
        else:
            self.duck_rect.x = screen_width - 150

        self.clock = pygame.time.Clock()
        self.duck_animation_timer = pygame.time.get_ticks()
        self.bush_animation_timer = pygame.time.get_ticks()

        if self.direction == 1:
            self.duck_images = [pygame.transform.flip(self.duck_image_1, True, False),
                                pygame.transform.flip(self.duck_image_2, True, False),
                                pygame.transform.flip(self.duck_image_3, True, False),
                                pygame.transform.flip(self.duck_image_4, True, False),
                                pygame.transform.flip(self.duck_image_3, True, False),
                                pygame.transform.flip(self.duck_image_2, True, False),
                                pygame.transform.flip(self.duck_image_1, True, False)]
        else:
            self.duck_images = [self.duck_image_1, self.duck_image_2, self.duck_image_3, self.duck_image_4,
                                self.duck_image_3, self.duck_image_2, self.duck_image_1]

    def update(self, current_time):
        self.duck_animation_timer = current_time
        self.current_duck_index += 1
        if self.current_duck_index > len(self.duck_images) - 1:
            self.current_duck_index = 0

        if self.duck_rect.left > screen_width or self.duck_rect.right < 0:
            place()

    def images(self):
        duck_images = self.duck_images
        duck_rect = self.duck_rect
        return duck_images, duck_rect


class Bunny:
    def __init__(self):
        self.name = 'Заяц'

        self.duck_rect = pygame.Rect(0, 0, 0, 0)

        (self.duck_image_1, self.duck_image_2, self.duck_image_3,
         self.duck_image_4, self.duck_image_5, self.duck_image_6,
         self.duck_image_7, self.duck_image_8) = (pygame.image.load(f'{file_dir}/bunny1.png'),
                                                                                      pygame.image.load(f'{file_dir}/bunny2.png'),
                                                                                      pygame.image.load(f'{file_dir}/bunny3.png'),
                                                                                      pygame.image.load(f'{file_dir}/bunny4.png'),
                                                                                      pygame.image.load(f'{file_dir}/bunny5.png'),
                                                                                      pygame.image.load(f'{file_dir}/bunny6.png'),
                                                                                      pygame.image.load(f'{file_dir}/bunny7.png'),
                                                                                      pygame.image.load(f'{file_dir}/bunny8.png'))

        self.duck_images = [self.duck_image_1, self.duck_image_2, self.duck_image_3, self.duck_image_4]

        self.current_duck_index = 0

        self.duck_rect = self.duck_images[self.current_duck_index].get_rect()

        self.duck_rect.y = random.randint(900, screen_height- 100)

        self.direction = random.choice([-1, 1])
        self.spawn_behind = random.randint(0, 1)
        if self.direction == 1 and self.spawn_behind == 0:
            self.duck_rect.x = -100
        elif self.direction == -1 and self.spawn_behind == 0:
            self.duck_rect.x = screen_width - 150
        elif self.spawn_behind == 1:
            self.duck_rect.x = 635
            leaves_sound.play()

        self.clock = pygame.time.Clock()
        self.duck_animation_timer = pygame.time.get_ticks()
        self.bush_animation_timer = pygame.time.get_ticks()

        if self.direction == -1:
            self.duck_images = [pygame.transform.flip(self.duck_image_1, True, False),
                                pygame.transform.flip(self.duck_image_2, True, False),
                                pygame.transform.flip(self.duck_image_3, True, False),
                                pygame.transform.flip(self.duck_image_4, True, False),
                                pygame.transform.flip(self.duck_image_5, True, False),
                                pygame.transform.flip(self.duck_image_6, True, False),
                                pygame.transform.flip(self.duck_image_7, True, False),
                                pygame.transform.flip(self.duck_image_8, True, False)]
        else:
            self.duck_images = [self.duck_image_1, self.duck_image_2, self.duck_image_3, self.duck_image_4,
                                self.duck_image_5, self.duck_image_6, self.duck_image_7, self.duck_image_8]

    def update(self, current_time):
        self.duck_animation_timer = current_time
        self.current_duck_index += 1
        if self.current_duck_index > len(self.duck_images) - 1:
            self.current_duck_index = 0

        if self.duck_rect.left > screen_width or self.duck_rect.right < 0:
            place()

    def images(self):
        duck_images = self.duck_images
        duck_rect = self.duck_rect
        return duck_images, duck_rect


class Cloud:
    def __init__(self):
        self.cloud_image = pygame.image.load(f'{file_dir}/cloud.png')
        self.cloud_rect = self.cloud_image.get_rect()
        self.direction = random.choice([-1, 1])

    def place(self):
        self.cloud_rect.y = random.randint(20, 300)
        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.cloud_rect.x = -100
        else:
            self.cloud_rect.x = screen_width - 150


class Photo:
    def __init__(self):
        self.background = pygame.image.load(f'{file_dir}/background_for_photo.png')

    def run(self):
        screen.blit(self.background, (0, 0))

        font_name = pygame.font.Font(None, 150)
        name = font.render(animal.name, True, black)
        screen.blit(name, (825, 649))


def place():
    global animal

    r = random.randint(1, 3)
    if r == 1:
        animal = Duck()
    elif r == 2:
        animal = Vorobey()
    elif r == 3:
        animal = Bunny()
    animal.images()

    if r == 1 or r == 2:
        animal.duck_rect.y = random.randint(100, screen_height - 350)
    elif r == 3:
        if animal.spawn_behind == 1:
            animal.duck_rect.y = 630
        else:
            animal.duck_rect.y = random.randint(700, screen_height - 200)


def shot(score):
    camera_sound.play()

    fill()
    if ((animal.duck_rect.collidepoint(event.pos)
            and (670 < animal.duck_rect.y < 900 or (not (670 < animal.duck_rect.y < 900) and
                                                    not (480 < animal.duck_rect.x < 880)))) and
            (not (cloud.cloud_rect.x - 40 < animal.duck_rect.x < cloud.cloud_rect.x + 285) or
            (not (cloud.cloud_rect.y - 100 < animal.duck_rect.y < cloud.cloud_rect.y + 280))) and
            (not (630 < animal.duck_rect.y < 764) or not (1141 < animal.duck_rect.x < 1569))):
        photo = Photo()
        photo.run() 
        place()
        score += 1
    return animal.duck_rect.x, score


def fill():
    global white, black

    screen.fill(white)

    duck_rect_copy = animal.duck_rect.copy()

    if (670 < animal.duck_rect.y < 900 or (not (670 < animal.duck_rect.y < 900) and not (480 < animal.duck_rect.x < 880))) and \
            (not (cloud.cloud_rect.x - 40 < animal.duck_rect.x < cloud.cloud_rect.x + 285) or
            (not (cloud.cloud_rect.y - 100 < animal.duck_rect.y < cloud.cloud_rect.y + 280))) and \
            (not (630 < animal.duck_rect.y < 764) or not (1141 < animal.duck_rect.x < 1569)):
        pygame.draw.rect(screen, black, duck_rect_copy)

    pygame.display.flip()

    pygame.time.delay(30)


def shaking():
    coords = (random.randint(497, 500), random.randint(497, 500))
    return coords


running = True
clock = pygame.time.Clock()
duck_animation_timer = pygame.time.get_ticks()
bush_animation_timer = pygame.time.get_ticks()
birds_sound_timer = pygame.time.get_ticks()
start = True

while running:
    if start:
        place()

        birds_sound.play().set_volume(0.4)

        cloud = Cloud()
        cloud.place()

        start = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            animal.duck_rect.x, score = shot(score)

    if animal.duck_rect.left > screen_width or animal.duck_rect.right < 0:
        place()

    current_time = pygame.time.get_ticks()
    if current_time - animal.duck_animation_timer >= 200:
        animal.update(current_time)

    animal.duck_rect.move_ip(4 * animal.direction, 0)

    background = pygame.image.load(f"{file_dir}/background_for_project.png")
    screen.blit(background, (0, 0))

    current_duck_image = animal.duck_images[animal.current_duck_index]
    screen.blit(current_duck_image, animal.duck_rect)

    if cloud.cloud_rect.left > screen_width or cloud.cloud_rect.right < 0:
        cloud.place()

    cloud.cloud_rect.move_ip(1 * cloud.direction, 0)

    screen.blit(cloud.cloud_image, cloud.cloud_rect)

    bush_image = pygame.image.load(f'{file_dir}/bush.png')
    coords = (500, 500)
    if current_time - bush_animation_timer >= 400:
        bush_animation_timer = current_time
        coords = shaking()
        screen.blit(bush_image, coords)
    else:
        screen.blit(bush_image, coords)

    wood_image = pygame.image.load(f'{file_dir}/wood.png')
    wood_coords = (1167, 813)
    screen.blit(wood_image, wood_coords)

    if ((670 < animal.duck_rect.y < 900 and (385 < animal.duck_rect.x < 880)) or
            (animal.duck_rect.y > 773 and (1130 < animal.duck_rect.x < 1835))):
        screen.blit(current_duck_image, animal.duck_rect)

    font = pygame.font.Font(f'{file_dir}/UpheavalPro.ttf', 98)
    score_text = font.render("Score: " + str(score), True, yellow)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()