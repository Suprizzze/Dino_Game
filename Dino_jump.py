from sys import exit
import pygame
import time
import random

pygame.init()
win = pygame.display.set_mode((1600, 670))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()


class Player:

    def __init__(self, x, y, speed, width, height, jump_count):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.jump_count = jump_count
        self.is_jumpr = False
        self.is_jumpl = False
        self.left = False
        self.right = False
        self.animCount = 0
        self.fire = False
        self.ps = False
        self.bg_count = 0

    def update_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > -200:
            self.x -= self.speed
            self.left = True
            self.right = False
            self.ps = False
        elif keys[pygame.K_RIGHT] and self.x < 750:
            self.x += self.speed
            self.left = False
            self.right = True
            self.ps = False
        elif keys[pygame.K_b]:
            self.ps = True
            self.right = False
            self.left = False
        else:
            self.left = False
            self.right = True


        if not (self.is_jumpr) and not (self.is_jumpl):  # указываем если фалс из джамп
            if keys[pygame.K_m]:  # а тут если пробель и становится тру из джамп
                self.is_jumpr = True
                self.is_jumpl = False

            if keys[pygame.K_n]:
                self.is_jumpl = True
                self.is_jumpr = False
        else:
            if self.jump_count >= -10:  # тут укакзываем что если больше или равно  - 10
                if self.jump_count < 0:
                    self.y += (self.jump_count ** 2 / 2)
                else:
                    self.y -= self.jump_count ** 2 / 2
                self.jump_count -= 0.5
            else:
                self.is_jumpl = False
                self.is_jumpr = False
                self.jump_count = 10
                self.left = False
                self.right = True


player1 = Player(-200, -80, 8, 150, 150, 10)

#image_path = '/data/data/org.test.myapp/files/app/'
image_path = ""
bg_music = pygame.mixer.Sound(image_path + "Sound/bgg.mp3")
bg_mol = pygame.mixer.Sound(image_path + "Sound/mol.mp3")
bg_mol.set_volume(0.1)
bg_music.play(-1)


bg = [pygame.image.load(image_path + 'pic\\bg\\stom-land-0.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-1.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-2.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-3.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-4.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-6.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-7.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-8.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-9.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-10.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-11.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-12.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-13.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-14.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-15.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-16.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-17.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-18.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-19.png').convert()]

#stand r
sr = [pygame.image.load(image_path + "pic\\d\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\24.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\25.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\26.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\27.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\28.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\29.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\30.png").convert_alpha()]

l = [pygame.image.load(image_path + "pic\\l\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\19.png").convert_alpha(),pygame.image.load(image_path + image_path + "pic\\l\\20.png").convert_alpha()]

r = [pygame.image.load(image_path + "pic\\r\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\20.png").convert_alpha()]

jl = [pygame.image.load(image_path + "pic\\jl\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\24.png").convert_alpha()]


jr = [pygame.image.load(image_path + "pic\\jr\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\24.png").convert_alpha()]

item = [pygame.image.load(image_path + "pic\\item\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\3.png").convert_alpha(),
        pygame.image.load(image_path + "pic\\item\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\6.png").convert_alpha(),
        pygame.image.load(image_path + "pic\\item\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\9.png").convert_alpha(),
        pygame.image.load(image_path + "pic\\item\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\12.png").convert_alpha(),
        pygame.image.load(image_path + "pic\\item\\13.png").convert_alpha()]

rect1 = pygame.image.load(image_path + "pic\\rect1.png")
rect2 = pygame.image.load(image_path + "pic\\rect2.png")

start = [pygame.image.load(image_path + "pic\\start\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\24.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\25.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\26.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\27.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\28.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\29.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\30.png").convert_alpha()]

over = [pygame.image.load(image_path + "pic\\over\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\24.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\25.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\26.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\27.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\28.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\29.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\30.png").convert_alpha()]


bg_x = 0

item_list = []

rand1 = [10,20,30]
rand2 = [25,30,35,40]
rand3 = [40,45,50,55]

item_timer = pygame.USEREVENT + 1
pygame.time.set_timer(item_timer, 4000)

score = 0
label = pygame.font.SysFont("arial", 50)
lose_label = label.render("   Эх. Ты проиграл !!!", False, (193, 196, 199))
restart_label = label.render("Попробуй еще Брат!!!! Нажми на меня", False, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(400, 350))
by_label = label.render("By Petrosyan Gegham", False, (193, 196, 199))

upr_label = label.render("Управление - ← →", False, (193, 196, 199))
jump_label = label.render("Прыжок - N,M", False, (193, 196, 199))
pause_label = label.render("Пауза - B", False, (193, 196, 199))

start_label = label.render("Начать игру", False, (139, 0, 0))
start_label_rect = start_label.get_rect(topleft=(650, 370))



def draw_window():
    if player1.bg_count + 1 >= 320:
        player1.bg_count = 0
    if player1.bg_count + 1 == 35:
        bg_mol.play(fade_ms=1)
    win.blit(bg[player1.bg_count // 20], (bg_x, 0))
    win.blit(bg[player1.bg_count // 20], (bg_x + 1600, 0))
    score_label = label.render(f"Score {score}", False, (0, 255, 0))
    win.blit(score_label, (1350, 50))
    if player1.animCount + 1 >= 60:
        player1.animCount = 0
    if player1.left and not player1.is_jumpr and not player1.is_jumpl:
        win.blit(l[player1.animCount // 3], (player1.x, player1.y))
        player1.animCount += 1
    elif player1.right and not player1.is_jumpr and not player1.is_jumpl and not player1.ps:
        win.blit(r[player1.animCount // 3], (player1.x, player1.y))
        player1.animCount += 1
    if player1.ps:
        win.blit(sr[player1.animCount // 4], (player1.x, player1.y))
        player1.animCount += 1
    if player1.is_jumpr:
        win.blit(jr[player1.animCount // 3], (player1.x, player1.y))
        player1.animCount += 1
    if player1.is_jumpl:
        win.blit(jl[player1.animCount // 3], (player1.x, player1.y))
        player1.animCount += 1
        if player1.animCount + 1 >= 200:
            player1.animCount = 0

startplay = True
gameplay = False

while True:

    clock.tick(50)
    if startplay:
        player1.bg_count += 1
        win.fill((139, 0, 0))
        win.blit(start[player1.bg_count // 4],(-670, -870))
        if player1.bg_count + 1 >= 60:
            player1.bg_count = 0
        win.blit(start_label, start_label_rect)
        win.blit(upr_label, (1100, 50))
        win.blit(jump_label, (1100, 100))
        win.blit(pause_label, (1100, 150))
        mouse = pygame.mouse.get_pos()

        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            startplay = False

    elif gameplay:
        draw_window()
        if not player1.ps:
            bg_x -= 2
        elif player1.left:
            bg_x += 2
        if bg_x == -1600:
            bg_x = 0

        player1.bg_count += 1

        player_rect = rect1.get_rect(topleft=(player1.x + 200, player1.y))

        if item_list:
            for (i, j) in enumerate(item_list):
                win.blit(item[player1.bg_count // 26], j)
                if score < 200:
                    j.x -= random.choice(rand1)
                if 200 <= score < 400:
                    j.x -= random.choice(rand2)
                if 400 <= score:
                    j.x -= random.choice(rand3)
                if j.x < -25:

                    item_list.pop()
                    score += 10
                if player_rect.colliderect(j):
                    gameplay = False
                    player1.bg_count = 0
    else:
        if player1.bg_count >= 120:
            win.fill((139, 0, 0))
            win.blit(pygame.image.load("pic\\over\\30.png").convert_alpha(), (200, -80))
            win.blit(lose_label, (600, 250))
            win.blit(by_label, (1000, 0))
            win.blit(restart_label, restart_label_rect)
            label_score = label.render(f"Score = {score}", False, (0, 120, 0))
            win.blit(label_score, (200, 50))
        mouse1 = pygame.mouse.get_pos()
        if player1.bg_count < 120:
            win.fill((139, 0, 0))
            win.blit(over[player1.bg_count // 4], (200, -80))
            player1.bg_count += 1


        if restart_label_rect.collidepoint(mouse1) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player1.x = -200
            item_list.clear()
            score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == item_timer:
            if not player1.ps and not startplay:
                item_list.append(rect2.get_rect(topleft=(1600, 350)))

    pygame.display.update()
    Player.update_key(player1)




