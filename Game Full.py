import ctypes
import pygame
from Pl_mod import Player
import Sprit
import time
import random

pygame.init()


player1 = Player(-200, -80, 8, 150, 150, 10)


win = pygame.display.set_mode((1600, 670))

pygame.display.set_caption("Game")
clock = pygame.time.Clock()

bg_music = pygame.mixer.Sound(Sprit.image_path + "Sound/bgg.mp3")
bg_mol = pygame.mixer.Sound(Sprit.image_path + "Sound/mol.mp3")
bg_mol.set_volume(0.1)
bg_music.play(-1)


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
    win.blit(Sprit.bg[player1.bg_count // 20], (bg_x, 0))
    win.blit(Sprit.bg[player1.bg_count // 20], (bg_x + 1600, 0))
    score_label = label.render(f"Score {score}", False, (0, 255, 0))
    win.blit(score_label, (1350, 50))
    if player1.animCount + 1 >= 60:
        player1.animCount = 0
    if player1.left and not player1.is_jumpr and not player1.is_jumpl:
        win.blit(Sprit.l[player1.animCount // 3], (player1.x, player1.y))
        player1.animCount += 1
    elif player1.right and not player1.is_jumpr and not player1.is_jumpl and not player1.ps:
        win.blit(Sprit.r[player1.animCount // 3], (player1.x, player1.y))
        player1.animCount += 1
    if player1.ps:
        win.blit(Sprit.sr[player1.animCount // 4], (player1.x, player1.y))
        player1.animCount += 1
    if player1.is_jumpr:
        win.blit(Sprit.jr[player1.animCount // 3], (player1.x, player1.y))
        player1.animCount += 1
    if player1.is_jumpl:
        win.blit(Sprit.jl[player1.animCount // 3], (player1.x, player1.y))
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
        win.blit(Sprit.start[player1.bg_count // 4],(-670, -870))
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

        player_rect = Sprit.rect1.get_rect(topleft=(player1.x + 200, player1.y))

        if item_list:
            for (i, j) in enumerate(item_list):
                win.blit(Sprit.item[player1.bg_count // 26], j)
                if score < 200:
                    j.x -= random.choice(rand1)
                if 100 <= score <= 400:
                    j.x -= random.choice(rand2)
                if score > 600:
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
            win.blit(Sprit.over[player1.bg_count // 4], (200, -80))
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
                item_list.append(Sprit.rect2.get_rect(topleft=(1600, 350)))

    pygame.display.update()
    Player.update_key(player1)




