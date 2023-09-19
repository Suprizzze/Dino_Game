from sys import exit
import pygame
import random

# Initialize Pygame
pygame.init()

# Define the Pygame window and settings
win = pygame.display.set_mode((1600, 670))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8
        self.width = 150
        self.height = 150
        self.jump_count = 10
        self.is_jumping_right = False
        self.is_jumping_left = False
        self.left = False
        self.right = False
        self.animCount = 0
        self.fire = False
        self.ps = False
        self.bg_count = 0

    def move(self):
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

        if not (self.is_jumping_right or self.is_jumping_left):
            if keys[pygame.K_m]:
                self.is_jumping_right = True
            elif keys[pygame.K_n]:
                self.is_jumping_left = True
        else:
            if self.jump_count >= -10:
                if self.jump_count < 0:
                    self.y += (self.jump_count ** 2 / 2)
                else:
                    self.y -= self.jump_count ** 2 / 2
                self.jump_count -= 0.5
            else:
                self.is_jumping_left = False
                self.is_jumping_right = False
                self.jump_count = 10


# Function to draw the game window
def draw_window():

    if player1.bg_count + 1 >= MAX_BG_COUNT:
        player1.bg_count = 0

    if player1.bg_count + 1 == BG_CHANGE_SOUND_TRIGGER:
        bg_mol.play(fade_ms=1)

    bg_image_index = player1.bg_count // 20
    win.blit(image_collections['bg'][bg_image_index], (bg_x, 0))
    win.blit(image_collections['bg'][bg_image_index], (bg_x + 1600, 0))

    score_label = label.render(f"Score {score}", False, (0, 255, 0))
    win.blit(score_label, (1350, 50))

    if player1.animCount + 1 >= ANIM_COUNT_LIMIT:
        player1.animCount = 0

    if player1.left and not (player1.is_jumping_right or player1.is_jumping_left):
        win.blit(image_collections['l'][player1.animCount // 3], (player1.x, player1.y))
    elif player1.right and not (player1.is_jumping_right or player1.is_jumping_left) and not player1.ps:
        win.blit(image_collections['r'][player1.animCount // 3], (player1.x, player1.y))
    elif player1.ps:
        win.blit(image_collections['stand_r'][player1.animCount // 4], (player1.x, player1.y))
    elif player1.is_jumping_right:
        win.blit(image_collections['jr'][player1.animCount // 3], (player1.x, player1.y))
    elif player1.is_jumping_left:
        win.blit(image_collections['jl'][player1.animCount // 3], (player1.x, player1.y))

    player1.animCount += 1


start_play = True
gameplay = False
game_over = False


# Function to start the game
def start_game(player, s_gameplay, s_start_play):
    clock.tick(50)
    if s_start_play:
        player1.bg_count += 1
        win.fill((139, 0, 0))
        win.blit(image_collections['start'][player1.bg_count // 4], (-670, -870))
        if player1.bg_count + 1 >= 60:
            player1.bg_count = 0
        win.blit(start_label, start_label_rect)
        win.blit(upr_label, (1100, 50))
        win.blit(jump_label, (1100, 100))
        win.blit(pause_label, (1100, 150))
        mouse = pygame.mouse.get_pos()

        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            s_gameplay = True
            s_start_play = False

    return s_gameplay, s_start_play


def play_gameplay(s_bg_x, s_score, s_gameplay):
    if not player1.ps:
        s_bg_x -= 2
    elif player1.left:
        s_bg_x += 2
    if s_bg_x == -1600:
        s_bg_x = 0

    player1.bg_count += 1

    player_rect = image_collections['rect1'].get_rect(topleft=(player1.x + 200, player1.y))

    if item_list:
        for (i, j) in enumerate(item_list):
            win.blit(image_collections['item'][player1.bg_count // 26], j)
            if s_score < 200:
                j.x -= random.choice(rand1)
            if 200 <= s_score < 400:
                j.x -= random.choice(rand2)
            if 400 <= s_score:
                j.x -= random.choice(rand3)
            if j.x < -25:
                item_list.pop()
                s_score += 10
            if player_rect.colliderect(j):
                s_gameplay = False
                player1.bg_count = 0
    return s_bg_x, s_score, s_gameplay


# Function to display the game over screen
def show_game_over_screen(player, s_score, s_gameplay):
    if player1.bg_count >= 120:
        win.fill((139, 0, 0))
        win.blit(pygame.image.load("pic\\over\\30.png").convert_alpha(), (200, -80))
        win.blit(lose_label, (600, 250))
        win.blit(by_label, (1000, 0))
        win.blit(restart_label, restart_label_rect)
        label_score = label.render(f"Score = {s_score}", False, (0, 120, 0))
        win.blit(label_score, (200, 50))
    mouse1 = pygame.mouse.get_pos()
    if player1.bg_count < 120:
        win.fill((139, 0, 0))
        win.blit(image_collections['over'][player1.bg_count // 4], (200, -80))
        player1.bg_count += 1

    if restart_label_rect.collidepoint(mouse1) and pygame.mouse.get_pressed()[0]:
        s_gameplay = True
        player1.x = -200
        item_list.clear()
        s_score = 0

    return s_gameplay, s_score


if __name__ == "__main__":
    player1 = Player(-200, -80)

    image_path = ""
    bg_music = pygame.mixer.Sound(image_path + "Sound/bgg.mp3")
    bg_mol = pygame.mixer.Sound(image_path + "Sound/mol.mp3")
    bg_mol.set_volume(0.1)
    bg_music.play(-1)

    image_collections = {
        'bg': [pygame.image.load(image_path + f'pic\\bg\\stom-land-{i}.png').convert() for i in range(0, 20)],
        'stand_r': [pygame.image.load(image_path + f'pic\\d\\{i}.png').convert_alpha() for i in range(1, 31)],
        'l': [pygame.image.load(image_path + f'pic\\l\\{i}.png').convert_alpha() for i in range(1, 21)],
        'r': [pygame.image.load(image_path + f'pic\\r\\{i}.png').convert_alpha() for i in range(1, 21)],
        'jl': [pygame.image.load(image_path + f'pic\\jl\\{i}.png').convert_alpha() for i in range(1, 25)],
        'jr': [pygame.image.load(image_path + f'pic\\jr\\{i}.png').convert_alpha() for i in range(1, 25)],
        'item': [pygame.image.load(image_path + f'pic\\item\\{i}.png').convert_alpha() for i in range(1, 14)],
        'rect1': pygame.image.load(image_path + 'pic\\rect1.png'),
        'rect2': pygame.image.load(image_path + 'pic\\rect2.png'),
        'start': [pygame.image.load(image_path + f'pic\\start\\{i}.png').convert_alpha() for i in range(1, 31)],
        'over': [pygame.image.load(image_path + f'pic\\over\\{i}.png').convert_alpha() for i in range(1, 31)],
    }

    bg_x = 0

    item_list = []

    rand1 = [10, 20, 30]
    rand2 = [25, 30, 35, 40]
    rand3 = [40, 45, 50, 55]

    item_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(item_timer, 4000)

    score = 0
    label = pygame.font.SysFont("arial", 50)
    lose_label = label.render("   Oops. You lost!!!", False, (193, 196, 199))
    restart_label = label.render("Try again, Click me", False, (115, 132, 148))
    restart_label_rect = restart_label.get_rect(topleft=(400, 350))
    by_label = label.render("By Petrosyan Gegham", False, (193, 196, 199))

    upr_label = label.render("Controls - ← →", False, (193, 196, 199))
    jump_label = label.render("Jump - N, M", False, (193, 196, 199))
    pause_label = label.render("Pause - B", False, (193, 196, 199))

    start_label = label.render("Start the game", False, (139, 0, 0))
    start_label_rect = start_label.get_rect(topleft=(650, 370))

    MAX_BG_COUNT = 320
    BG_CHANGE_SOUND_TRIGGER = 35
    ANIM_COUNT_LIMIT = 60
    ANIM_COUNT_JUMP_LIMIT = 200

    while True:
        clock.tick(50)

        if start_play:
            gameplay, start_play = start_game(player1, gameplay, start_play)
        elif gameplay:
            draw_window()
            bg_x, score, gameplay = play_gameplay(bg_x, score, gameplay)
        else:
            score, gameplay = show_game_over_screen(player1, score, gameplay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == item_timer:
                if not player1.ps and not start_play:
                    item_list.append(image_collections['rect2'].get_rect(topleft=(1600, 350)))

        pygame.display.update()
        Player.move(player1)
