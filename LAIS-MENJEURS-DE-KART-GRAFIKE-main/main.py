import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Notre RPG")
screen = pygame.display.set_mode((1280, 720))
background = pygame.image.load("hg.jpg")
background = pygame.transform.scale(background, (1280, 720))
menu = pygame.image.load("boutoniu.png")
game = Game()
x_bouton = (1280 - menu.get_width()) / 2
y_bouton = (720 - menu.get_height()) / 2
running = True

leave_menu = False
while running:
    screen.blit(background, (0, 0))
    screen.blit(menu, (x_bouton, y_bouton))
    if game.pressed.get(pygame.K_SPACE):
        leave_menu = True

    if leave_menu:  
        screen.blit(game.player.image, game.player.rect)


    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()

    if game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
        game.player.move_down()

   
    pygame.display.flip()

    for event in pygame.event.get():
        # vérifie l'événement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            # une touche pressée
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # une touche relâchée
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False