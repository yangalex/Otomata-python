import pygame
# initialize Pygame
pygame.init()

# Class Label
# Creates a label object (a sprite); it's exactly the same as a button class, but for the sake of simplicity and clarity
# I decided to make it into two separate classes.
class Label(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, w, h, text):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        buttonText = font.render(text, 1, ((255, 255, 255)))
        self.image.blit(buttonText, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

