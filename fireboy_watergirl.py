import pygame
import sys
 
pygame.init()
 
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("Jumping in PyGame")

originalIMG = pygame.image.load(r"bakgrunn.jpg")
IMG = pygame.transform.scale(originalIMG, (1280, 800))

X_POSITION, Y_POSITION = 200, 510
 
jumping = False
 
Y_GRAVITY = 0.5
JUMP_HEIGHT = 15
Y_VELOCITY = JUMP_HEIGHT

STANDING_SURFACE = pygame.transform.scale(pygame.image.load(r"Fireboy-0.webp"), (48, 64))


mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    keys_pressed = pygame.key.get_pressed()
 
    if keys_pressed[pygame.K_UP]:
        jumping = True

    if keys_pressed[pygame.K_LEFT]:
      X_POSITION -= 5

    if keys_pressed[pygame.K_RIGHT]:
      X_POSITION += 5
 
    SCREEN.blit(IMG, (0, 0))
    
    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, mario_rect)
    else:
        mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, mario_rect)
        
 
    pygame.display.update()
    CLOCK.tick(60)