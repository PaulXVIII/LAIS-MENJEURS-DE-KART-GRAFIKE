import pygame
from game import Game
from pygame.locals import *
from time import monotonic


pygame.init()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def studio_fade_in(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(255, 0, -4):
        screen.blit(studio_screen, (0, 0))
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(50)
    pygame.time.delay(300)

def fade_out(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 80):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(50)

def menu_fade_in(width, height):
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(255, 0, -5):
        screen.blit(background, (0, 0))
        screen.blit(menu, (x_bouton, y_bouton))
        screen.blit(title, (x_titre, y_titre))
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)


text_font = pygame.font.SysFont("Arial", 30)
jingle = pygame.mixer.Sound("Assets\\studio\\jingle.wav")
pygame.display.set_caption("Caesar Quest")
icon = pygame.image.load("Assets\\icon.jpg")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1280, 720))
studio_screen = pygame.image.load("Assets\\studio\\studiostrum.jpg")
studio_screen = pygame.transform.scale(studio_screen, (1280, 720))
background = pygame.image.load("Assets\\menu\\background.jpg")
background = pygame.transform.scale(background, (1280, 720))
menu = pygame.image.load("Assets\\menu\\menu_buttons.png")
title = pygame.image.load("Assets\\menu\\title.png")
title = pygame.transform.scale(title, (500, 500))
game = Game()
x_bouton = (1280 - menu.get_width()) / 2
y_bouton = (720 - menu.get_height()) / 2
x_titre = (1280 - title.get_width()) / 2
y_titre = (720 - title.get_height()) / 2 - 350
running = True
leave_menu = False
text_displayed = False

zone1_rect = pygame.Rect(444, 257, 398, 37)
zone2_rect = pygame.Rect(444, 306, 398, 37)
zone3_rect = pygame.Rect(444, 353, 398, 37)
zone4_rect = pygame.Rect(444, 426, 193, 37)
zone5_rect = pygame.Rect(649, 426, 193, 37)

constante_de_pesanteur = 0.2
vitesse_chute = 0

transparent_surface = pygame.Surface((1280, 720), pygame.SRCALPHA)
transparent_surface.fill((0, 0, 5, 3))

jingle.play()
studio_fade_in(1280, 720)
fade_out(1280, 720)

menu_fade_in(1280, 720)

while running:
    screen.blit(background, (0, 0))
    screen.blit(menu, (x_bouton, y_bouton))
    screen.blit(title, (x_titre, y_titre))

    temps_actuel = monotonic()
    
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

    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    
    vitesse_chute += constante_de_pesanteur
    game.player.rect.y += vitesse_chute
    
    if game.pressed.get(pygame.K_SPACE) and not en_l_air: # le joueur ne peut sauter que quand il touche le sol 
        vitesse_chute = -7
        en_l_air = True # Permet de savoir si le joueur touche le sol (pour l'instant le bas de l'écran, mais au fur et à mesur ça sera les platerformes)
    elif game.player.rect.y + game.player.rect.height >= screen.get_height(): # évite qu'il tombre en dehors de l'écran, mais ça sera valable pour les plateformes
        game.player.rect.y = screen.get_height() - game.player.rect.height
        en_l_air = False
    
    
    manual_quit = False
    
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and not leave_menu:  # Bouton gauche de la souris
                # Début du dessin de la zone
                if zone1_rect.collidepoint(event.pos):
                    print("Clic dans la zone 1!")
                    leave_menu = True
                elif zone2_rect.collidepoint(event.pos):
                    pass
                elif zone3_rect.collidepoint(event.pos):
                    pass
                elif zone4_rect.collidepoint(event.pos):
                    pass
                else:
                    manual_quit = True
        if manual_quit:
            pygame.event.Event(pygame.QUIT)
            running = False
            pygame.quit()
        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()
            # une touche pressée
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # une touche relâchée
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif manual_quit:
            pygame.quit()  # Fermer pygame
            sys.exit()
    if leave_menu:
        screen.blit(game.player.image, game.player.rect)
        menu.fill((0, 0, 0, 0))
        title.fill((0, 0, 0, 0))
        background.fill((0, 0, 0, 0))
        draw_text("Nous sommes en 1701, après la victoire de Marik", text_font, (255, 255, 255), 200, 200)
        text_displayed = True


    pygame.display.flip()
