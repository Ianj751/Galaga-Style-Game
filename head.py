import pygame,os
import random
WIDTH = 350
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screenrect = screen.get_rect()

playerSprite = pygame.sprite.Group()
bulletSprite = pygame.sprite.Group()
enemySprite = pygame.sprite.Group()



class playerShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("spaceship.jpg")).convert()
        self.rect = self.image.get_rect(center = (WIDTH // 2, HEIGHT - 100))
        self.direction = pygame.math.Vector2()
        self.speed = 8
    
    def drawShip(self):
        screen.blit(self.image, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.center += self.direction * self.speed

        if (self.rect.x + self.image.get_width()) > WIDTH:
            self.rect.x = WIDTH - self.image.get_width()
        elif self.rect.x < 0:
            self.rect.x = 0

        if (self.rect.y + self.image.get_height()) > HEIGHT:
            self.rect.y = HEIGHT - self.image.get_height()
        elif self.rect.y < 0:
            self.rect.y = 0

    def createLaser(self):
        return playerWeapon(self.rect.x + self.image.get_width() //2 , self.rect.y )
            
    
class playerWeapon(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([6, 6])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))

    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()
            del self

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("alien.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.image.get_width())
        self.rect.y = -self.image.get_height()
        self.direction = pygame.math.Vector2()
        self.death_sound = pygame.mixer.Sound('boom.mp3')
        self.speed = random.randrange(3, 8)

    def update(self):
        self.rect.y += self.speed

    def damaged(self):
        self.image = pygame.image.load(os.path.join("explosion.jpg")).convert()
        #self.death_sound.play()
        self.kill()
        del self

class EnemySpawner:
    def __init__(self):
        self.enemygroup = pygame.sprite.Group()
        self.spawntimer = random.randrange(30, 120)
        

    def update(self):
        self.enemygroup.update()
        if self.spawntimer == 0:
            self.spawnEnemy()
            self.spawntimer = random.randrange(30, 120)
        
        else:
            self.spawntimer -= 1

        
    def spawnEnemy(self):
        newEnemy = Enemy()
        self.enemygroup.add(newEnemy)







    