import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((794, 600))
pygame.display.set_caption("Title of the game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Text/Grand9K Pixel.ttf", 100)

w = 100
h = 200

text_surface = test_font.render('Some title', True, 'White')

background_surface = pygame.image.load("Images/cep.png").convert()

bird_surface = pygame.image.load("Images/bird.png").convert_alpha()
bird_x = 30
bird_y = 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # needed as when we close the game, we want to end the while loop as well

    screen.blit(background_surface, (0, 0))
    bird_x += 4
    if bird_x > 794:
        bird_x = 0
    screen.blit(bird_surface, (bird_x, bird_y))
    screen.blit(text_surface, (140, 150))

    pygame.display.update()
    clock.tick(60)

