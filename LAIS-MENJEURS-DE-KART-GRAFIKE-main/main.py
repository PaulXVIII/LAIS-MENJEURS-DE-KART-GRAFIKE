import pygame
from game import Game
from pygame.locals import *
import os


pygame.init()

pygame.display.set_caption("Notre RPG")
pygame.mixer.music.load("boss battle.mp3")
pygame.mixer.music.play(-1)
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load("bg.jpg")
background = pygame.transform.scale(background, (1280, 720))
menu = pygame.image.load("boutoniu.png")
title = pygame.image.load("title.png")
game = Game()
x_bouton = (1280 - menu.get_width()) / 2
y_bouton = (720 - menu.get_height()) / 2
x_titre = (1280 - title.get_width()) / 2
y_titre = (720 - title.get_height()) / 2 - 170
running = True

zone1_rect = pygame.Rect(444, 257, 398, 37)
zone2_rect = pygame.Rect(444, 306, 398, 37)
zone3_rect = pygame.Rect(444, 353, 398, 37)
zone4_rect = pygame.Rect(444, 426, 193, 37)
zone5_rect = pygame.Rect(649, 426, 193, 37)

transparent = (0, 0, 0, 0)
leave_menu = False
transparent_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
transparent_surface.fill((0, 0, 5, 3)) 


while running:
    screen.blit(background, (0, 0))
    screen.blit(menu, (x_bouton, y_bouton))
    screen.blit(title, (x_titre, y_titre))
    
    if not leave_menu:
        if zone1_rect.collidepoint(pygame.mouse.get_pos()):
            # Créer une surface semi-transparente pour la zone de collision
            transparent_surface = pygame.Surface((zone1_rect.width, zone1_rect.height), pygame.SRCALPHA)
            transparent_surface.fill((0, 0, 255, 32))  # Remplir avec du bleu semi-transparent
            screen.blit(transparent_surface, (zone1_rect.left, zone1_rect.top))
        elif zone2_rect.collidepoint(pygame.mouse.get_pos()):
            transparent_surface = pygame.Surface((zone2_rect.width, zone2_rect.height), pygame.SRCALPHA)
            transparent_surface.fill((0, 0, 255, 32))
            screen.blit(transparent_surface, (zone2_rect.left, zone2_rect.top))
        elif zone3_rect.collidepoint(pygame.mouse.get_pos()):
            transparent_surface = pygame.Surface((zone3_rect.width, zone3_rect.height), pygame.SRCALPHA)
            transparent_surface.fill((0, 0, 255, 32))
            screen.blit(transparent_surface, (zone3_rect.left, zone3_rect.top))
        elif zone4_rect.collidepoint(pygame.mouse.get_pos()):
            transparent_surface = pygame.Surface((zone4_rect.width, zone4_rect.height), pygame.SRCALPHA)
            transparent_surface.fill((0, 0, 255, 32))
            screen.blit(transparent_surface, (zone4_rect.left, zone4_rect.top))
        elif zone5_rect.collidepoint(pygame.mouse.get_pos()):
            transparent_surface = pygame.Surface((zone5_rect.width, zone5_rect.height), pygame.SRCALPHA)
            transparent_surface.fill((255, 0, 0, 32))
            screen.blit(transparent_surface, (zone5_rect.left, zone5_rect.top))
    
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()

    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
        game.player.move_down()
    
    
    manual_quit = False
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and not leave_menu:  # Bouton gauche de la souris
                # Début du dessin de la zone
                if zone1_rect.collidepoint(event.pos):
                    print("Clic dans la zone 1!")
                    leave_menu = True
                    

                # Vérifier si le clic est dans la zone 2
                elif zone2_rect.collidepoint(event.pos):
                    print("Clic dans la zone 2!")
                elif zone3_rect.collidepoint(event.pos):
                    print("Clic dans la zone 3!")
                elif zone4_rect.collidepoint(event.pos):
                    print("Clic dans la zone 4!")
                else:
                    print("Clic dans la zone 5!")
                    manual_quit = True
        elif event.type == pygame.QUIT or manual_quit:
            running = False
            pygame.quit()
            # une touche pressée
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # une touche relâchée
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
    if leave_menu:
        screen.blit(game.player.image, game.player.rect)
        menu.fill((0, 0, 0, 0))
        title.fill((0, 0, 0, 0))
        background.fill((0, 0, 0, 0))

    pygame.display.flip()
