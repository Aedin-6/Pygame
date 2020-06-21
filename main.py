import os
import pygame
import time
import random
pygame.font.init()


WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPace Shooter")


red_ship = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
green_ship = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
bule_ship = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
player_ship = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))


red_laser = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
green_laser = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
blue_laser = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
yellow_laser = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    player_vel = 5

    ship = Ship(200, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(bg, (0,0))

        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}",1, (255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 1))

        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            ship.x -= player_vel
        if keys[pygame.K_d]:
            ship.x += player_vel
        if keys[pygame.K_s]:
            ship.y += player_vel
        if keys[pygame.K_w]:
            ship.y -= player_vel



main()