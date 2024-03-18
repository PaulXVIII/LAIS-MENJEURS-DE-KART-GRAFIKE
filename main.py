import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Arie Peauteure")
screen = pygame.display.set_mode((1280, 720))

game = Game()

running = True

while running:
    screen.fill((74, 65, 42))
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