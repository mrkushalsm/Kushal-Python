import pygame
import math
import random

from pygame import mixer

# Projects Innit
pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space_Invaders")
icon = pygame.image.load("C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\game_icon.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load(
    "C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\background_1.jpg")

# Background Sound
mixer.music.load("C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\background.wav")
mixer.music.play(-1)

# Window Frame Config
# clock = pygame.time.Clock()
# FPS_CONSTANT = 2000

# Player
player_img = pygame.image.load(
    "C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\spaceship.png")
player_x = 360
player_y = 500
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
no_of_enemies = 6
for i in range(no_of_enemies):
    enemy_img.append(
        pygame.image.load("C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\ufo.png"))
    enemy_x.append(random.randint(0, 735))
    """if enemy_x[key] - enemy_x[key - 1] < 20:
        enemy_x[key] += 65 - (enemy_x[key - 1] - enemy_x[key])
    else:
        enemy_x[key] += 65 + (enemy_x[key - 1] - enemy_x[key])"""
    enemy_y.append(random.randint(50, 150))
    """if enemy_y[key] - enemy_y[key - 1] < 35 and enemy_y[key] != 1 and enemy_y[key] != 0:
        enemy_y[key] += 65 - (enemy_y[key - 1] - enemy_y[key])
    else:
        enemy_y[key] += 65 + (enemy_y[key - 1] - enemy_y[key])"""
    enemy_x_change.append(0.3)
    enemy_y_change.append(20)

# Bullet
bullet_img = pygame.image.load(
    "C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\bullet.png")
bullet_x = 0
temp_bullet_x = 0
bullet_y = 500
bullet_x_change = 0
bullet_y_change = 1
bullet_state = "ready"

# Score Display
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 36)
score_display_x = 10
score_display_y = 10

# Game Over Display
game_over_font = pygame.font.Font('freesansbold.ttf', 86)
game_over_display_x = 277
game_over_display_y = 200

# FPS Display


# Make Player appear on the screen


def player(x, y):
    screen.blit(player_img, (x, y))
    # pygame.display.update()


# Make Enemy appear on the screen


def enemy(x, y, i_1):
    screen.blit(enemy_img[i_1], (x, y))
    # pygame.display.update()


# Make the spaceship fire the bullet


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 20, y + 10))
    # pygame.display.update()


# Calculate the distance

def collision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance < 27:
        return True
    else:
        return False


# Show the score on the screen


def scoreboard(x, y):
    score = score_font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Show the FPS on the screen

"""def fps_display(x, y):
    fps = score_font.render("FPS : " + str(score_value), True, (255, 255, 255))
    screen.blit(fps, (x, y))"""


# Show game over on the screen

def game_over_display():
    game_over = score_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (game_over_display_x, game_over_display_y))


# Game Loop
running = True

# Screen Color
# screen.fill((0, 0, 0))

while running:

    # Screen Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            elif event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # bullet_sound = mixer.Sound( "C:\\Users\\mrkus\\Kushal Code\\Kushal
                    # Python\\StudPi\\Projects\\Space_Invaders\\bullet_shot.wav") mixer.Sound.play(bullet_sound)
                    temp_bullet_x = player_x
                    fire_bullet(temp_bullet_x, bullet_y)
                    bullet_sound = mixer.Sound(
                        "C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\bullet_shot.wav")
                    mixer.Sound.play(bullet_sound)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player Movement
    player_x += player_x_change

    # Boundary Check for the Player
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    for i in range(no_of_enemies):
        # Enemy Movement
        enemy_x[i] += enemy_x_change[i]

        # Boundary Check for the Enemy
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.3
            enemy_y[i] += enemy_y_change[i]
            # screen.fill((0, 0, 0))
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -0.3
            enemy_y[i] += enemy_y_change[i]
            # screen.fill((0, 0, 0))

        # Collision of bullet with enemy
        isBulletColliding = collision(enemy_x[i], enemy_y[i], temp_bullet_x, bullet_y)
        if isBulletColliding:
            enemy_damage = mixer.Sound(
                "C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\enemy_killed.wav")
            mixer.Sound.play(enemy_damage)
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            # print(score)
            # enemy_x[key] = random.randint(0, 735)
            # enemy_y[key] = random.randint(50, 150)
            enemy_x[i] - random.randint(0, 735)
            if enemy_x[i] - enemy_x[i - 1] < 25 and enemy_x[i] != 735:
                enemy_x[i] += 65 - (enemy_x[i - 1] - enemy_x[i])
            enemy_y[i] = random.randint(50, 150)
            if enemy_y[i] - enemy_y[i - 1] < 35:
                enemy_y[i] += 65 - (enemy_y[i - 1] - enemy_y[i])

        """if enemy_y == bullet_y and temp_bullet_x in range(int(enemy_x + 14), int(enemy_x + 50)):
            # and (bullet_x in range(int(enemy_x), int(enemy_x) + 65)):
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print("enemy x=", enemy_x, "bullet x=", temp_bullet_x)
            print("enemy y=", enemy_y, "bullet y=", bullet_y)
            print(score)"""
        """if enemy_y == bullet_y and bullet_x in range(int(enemy_x), int(enemy_x) + 60):
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print("enemy x=", enemy_x, "bullet x=", temp_bullet_x)
            print("enemy y=", enemy_y, "bullet y=", bullet_y)"""
        """if enemy_y == bullet_y and temp_bullet_x == int(enemy_x + 15):
            # and (bullet_x in range(int(enemy_x), int(enemy_x) + 65)):
            bullet_y = 480
            bullet_state = "ready"
            score += 1
            print("enemy x=", enemy_x, "bullet x=", temp_bullet_x)
            print("enemy y=", enemy_y, "bullet y=", bullet_y)
            print(score)"""
        """for bullet_x in range(int(enemy_x + 15), int(enemy_x + 49)):
            if enemy_y == bullet_y:
                bullet_y = 480
                bullet_state = "ready"
                score += 1
                print(score)
                continue"""
        enemy(enemy_x[i], enemy_y[i], i)

        # Collision of enemy with the player
        """isPlayerColliding = collision(player_x, player_y, enemy_x[key], enemy_y[key])
        if isPlayerColliding:
            print("Game Over")"""

    # Bullet Movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(temp_bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Game Over

    if enemy_y[i] > 200:
        for j in range(no_of_enemies):
            enemy_y[j] = 2000
            enemy_x_change[j] = 0
            mixer.music.play(2)
            game_over_display()
        mixer.music.stop()
        game_over_sound = mixer.Sound(
                "C:\\Users\\mrkus\\Kushal Code\\Kushal Python\\StudPi\\Projects\\Space_Invaders\\game_over.wav")
        mixer.Sound.play(game_over_sound)

    player(player_x, player_y)
    scoreboard(score_display_x, score_display_y)
    # clock.tick(FPS_CONSTANT)
    # print("FPS =", str(clock.get_fps()))
    pygame.display.update()
