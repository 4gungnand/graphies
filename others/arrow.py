"a simple animation of an arrow moving from left to right" 

import pygame
import sys

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Arrow Animation")

background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (width, height))  # Resizing the background image
background_rect = background_image.get_rect()

arrow_image = pygame.image.load("arrow.png")
arrow_rect = arrow_image.get_rect()

arrow_x = 0
arrow_y = height // 2 - arrow_rect.height // 2

arrow_speed = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    arrow_x += arrow_speed

    if arrow_x > width - arrow_rect.width:  # Periksa apakah arrow sudah mencapai sisi kanan layar
        arrow_x = width - arrow_rect.width  # Menempatkan arrow di sisi kanan layar

    screen.blit(background_image, background_rect)
    screen.blit(arrow_image, (arrow_x, arrow_y))

    pygame.display.flip()

    clock.tick(60)
