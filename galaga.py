import pygame
from head import *

pygame.init()


clock = pygame.time.Clock()
running = True
keys = pygame.key.get_pressed()

falcon = playerShip()
playerSprite.add(falcon)

enemy_spawner = EnemySpawner()

backgroundimg = pygame.image.load(os.path.join("stars.png"))
overlap = pygame.image.load(os.path.join("stars.png"))
back_pos = 0
over_pos = -HEIGHT
speed = 1


while running:
    if back_pos == HEIGHT:
        back_pos = -HEIGHT
    if over_pos == HEIGHT:
        over_pos = -HEIGHT

    over_pos += speed
    back_pos += speed

    screen.blit(backgroundimg, (0, back_pos))
    screen.blit(overlap, (0, over_pos))
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # can not get it to use the keyboard click for now
        if event.type == pygame.MOUSEBUTTONDOWN:
            bulletSprite.add(falcon.createLaser())
   
    collisions = pygame.sprite.groupcollide(bulletSprite, enemy_spawner.enemygroup, True, False)
    for bullet, enemy in collisions.items():
        enemy[0].damaged()

   
    playerSprite.update()
    bulletSprite.update()
    enemy_spawner.update()

    playerSprite.draw(screen)
    bulletSprite.draw(screen)
    enemySprite.draw(screen)
    enemy_spawner.enemygroup.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
