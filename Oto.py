import pygame

# initialize sounds
pygame.mixer.init(buffer=200)   # This can be increased for better sound quality, but causes latency (incorrect tempo)
pygame.mixer.set_num_channels(100)

# Set variables used to represent the arrows in each cell
LEFT = ((10, 37.5), (65, 10), (65, 65))
RIGHT = ((10, 10), (10, 65), (65, 37.5))
UP = ((10, 65), (65, 65), (37.5, 10))
DOWN = ((10, 10), (65, 10), (37.5, 65))


# Class Oto
# Creates an Oto object (a cell in the grid)
# It is able to: move itself, play music, check if it collides with anything and change its state (direction)
class Oto(pygame.sprite.Sprite):

    # Initialize instruments and sounds
    instrument = ""
    sounds = []
    C1 = pygame.mixer.Sound("Sounds/{}C1.wav".format(instrument))
    sounds.append(C1)
    D = pygame.mixer.Sound("Sounds/{}D.wav".format(instrument))
    sounds.append(D)
    E = pygame.mixer.Sound("Sounds/{}E.wav".format(instrument))
    sounds.append(E)
    F = pygame.mixer.Sound("Sounds/{}F.wav".format(instrument))
    sounds.append(F)
    G = pygame.mixer.Sound("Sounds/{}G.wav".format(instrument))
    sounds.append(G)
    A = pygame.mixer.Sound("Sounds/{}A.wav".format(instrument))
    sounds.append(A)
    B = pygame.mixer.Sound("Sounds/{}B.wav".format(instrument))
    sounds.append(B)
    C2 = pygame.mixer.Sound("Sounds/{}C2.wav".format(instrument))
    sounds.append(C2)
    D2 = pygame.mixer.Sound("Sounds/{}D2.wav".format(instrument))
    sounds.append(D2)

    # Set volumes
    for sound in sounds:
        sound.set_volume(1)   # value from 0.0-1.0; increase for higher volume


    # Constructor
    # input: pygame.Surface, int, int, int, int
    def __init__(self, screen, width, height, boardW, boardH):
        pygame.sprite.Sprite.__init__(self)     # call parent constructor
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
        pygame.draw.polygon(self.image, (255, 255, 255), DOWN, 0)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.orientation = "v"
        self.width = width
        self.height = height
        self.boardW = boardW
        self.boardH = boardH
        self.vy = width
        self.vx = height
        self.color = 255, 255, 255
        self.oscillating = False

    # Input: none
    # Output: none
    # Side-effect: changes the orientation of the object (vertical or horizontal)
    def changeOrientation(self):
        if self.orientation == "v":
            self.orientation = "h"
        elif self.orientation == "h":
            self.orientation = "v"

    # Called each time the group sprite is updated
    def update(self):
        if self.orientation == "v":
            # If the cell hits either the top or bottom wall
            if (self.rect.y+self.height == self.boardH and self.vy > 0) or (self.rect.y == 0 and self.vy < 0):
                # Change direction
                self.vy *= -1
                # Play sounds depending on coordinates
                if self.rect.x == 0:
                    Oto.C1.play()
                elif self.rect.x == self.width:
                    Oto.D.play()
                elif self.rect.x == self.width*2:
                    Oto.E.play()
                elif self.rect.x == self.width*3:
                    Oto.F.play()
                elif self.rect.x == self.width*4:
                    Oto.G.play()
                elif self.rect.x == self.width*5:
                    Oto.A.play()
                elif self.rect.x == self.width*6:
                    Oto.B.play()
                elif self.rect.x == self.width*7:
                    Oto.C2.play()
                elif self.rect.x == self.width*8:
                    Oto.D2.play()

                # Redraw the arrow depending on which wall it hits
                if self.rect.y+self.height == self.boardH:
                    self.image.fill((0, 0, 0))
                    pygame.draw.polygon(self.image, (255, 255, 255), UP, 0)
                elif self.rect.y == 0:
                    self.image.fill((0, 0, 0))
                    pygame.draw.polygon(self.image, (255, 255, 255), DOWN, 0)

            # This is a special case that happens when two arrows at the edge meet and start going around in circles (oscillating)
            # This ensures that they still continue playing when they hit the wall
            if self.oscillating and (self.rect.x+self.width == self.boardW or self.rect.x == 0):
                if self.rect.y == 0:
                    Oto.D2.play()
                elif self.rect.y == self.height:
                    Oto.C2.play()
                elif self.rect.y == self.height*2:
                    Oto.B.play()
                elif self.rect.y == self.height*3:
                    Oto.A.play()
                elif self.rect.y == self.height*4:
                    Oto.G.play()
                elif self.rect.y == self.height*5:
                    Oto.F.play()
                elif self.rect.y == self.height*6:
                    Oto.E.play()
                elif self.rect.y == self.height*7:
                    Oto.D.play()
                elif self.rect.y == self.height*8:
                    Oto.C1.play()

            # Move object
            self.rect.y += self.vy

        elif self.orientation == "h":
            # If the cell hits the right or left wall
            if (self.rect.x+self.width == self.boardW and self.vx > 0) or (self.rect.x == 0 and self.vx < 0):
                self.vx *= -1
                if self.rect.y == 0:
                    Oto.D2.play()
                elif self.rect.y == self.height:
                    Oto.C2.play()
                elif self.rect.y == self.height*2:
                    Oto.B.play()
                elif self.rect.y == self.height*3:
                    Oto.A.play()
                elif self.rect.y == self.height*4:
                    Oto.G.play()
                elif self.rect.y == self.height*5:
                    Oto.F.play()
                elif self.rect.y == self.height*6:
                    Oto.E.play()
                elif self.rect.y == self.height*7:
                    Oto.D.play()
                elif self.rect.y == self.height*8:
                    Oto.C1.play()

                # Redraw the arrow depending on which wall it hits
                if self.rect.x+self.width == self.boardW:
                    self.image.fill((0, 0, 0))
                    pygame.draw.polygon(self.image, (255, 255, 255), LEFT, 0)
                elif self.rect.x == 0:
                    self.image.fill((0, 0, 0))
                    pygame.draw.polygon(self.image, (255, 255, 255), RIGHT, 0)

            # This is a special case that happens when two arrows at the edge meet and start going around in circles (oscillating)
            # This ensures that they still continue playing when they hit the wall
            if self.oscillating and (self.rect.y+self.height == self.boardH or self.rect.y == 0):
                if self.rect.x == 0:
                    Oto.C1.play()
                elif self.rect.x == self.width:
                    Oto.D.play()
                elif self.rect.x == self.width*2:
                    Oto.E.play()
                elif self.rect.x == self.width*3:
                    Oto.F.play()
                elif self.rect.x == self.width*4:
                    Oto.G.play()
                elif self.rect.x == self.width*5:
                    Oto.A.play()
                elif self.rect.x == self.width*6:
                    Oto.B.play()
                elif self.rect.x == self.width*7:
                    Oto.C2.play()
                elif self.rect.x == self.width*8:
                    Oto.D2.play()

            # Move object
            self.rect.x += self.vx

    # Check Collisions
    def checkCollision(self, spritesList):
        for sprite in spritesList:
            # Make sure that object is not comparing against itself
            if self != sprite:
                # Change orientation depending on which direction it was going initially
                if pygame.sprite.collide_rect(self, sprite):
                    if self.orientation == "v" and self.vy > 0:
                        self.changeOrientation()
                        self.vx = -self.width
                        self.image.fill((0, 0, 0))
                        pygame.draw.polygon(self.image, (255, 255, 255), LEFT, 0)
                    elif self.orientation == "v" and self.vy < 0:
                        self.changeOrientation()
                        self.vx = self.width
                        self.image.fill((0, 0, 0))
                        pygame.draw.polygon(self.image, (255, 255, 255), RIGHT, 0)
                    elif self.orientation == "h" and self.vx > 0:
                        self.changeOrientation()
                        self.vy = self.height
                        self.image.fill((0, 0, 0))
                        pygame.draw.polygon(self.image, (255, 255, 255), DOWN, 0)
                    elif self.orientation == "h" and self.vx < 0:
                        self.changeOrientation()
                        self.vy = -self.height
                        self.image.fill((0, 0, 0))
                        pygame.draw.polygon(self.image, (255, 255, 255), UP, 0)

                    # Check to see if sprite is in oscillating mode (The arrows are exactly the same in every attribute)
                    if (self.orientation == sprite.orientation and self.vx == sprite.vx and self.rect.x == sprite.rect.x
                        and self.rect.y == sprite.rect.y) or (self.orientation == sprite.orientation and self.vy == sprite.vy
                        and self.rect.x == sprite.rect.x and self.rect.y == sprite.rect.y):

                        self.oscillating = True
                    else:
                        self.oscillating = False

    # Change the state of the arrow to left, right, up or down (User right click)
    def changeState(self):
        if self.orientation == "v":
            self.orientation = "h"
            if self.vy > 0:
                self.vx = -self.width
                self.image.fill((0, 0, 0))
                pygame.draw.polygon(self.image, (255, 255, 255), LEFT, 0)
            elif self.vy < 0:
                self.vx = self.width
                self.image.fill((0, 0, 0))
                pygame.draw.polygon(self.image, (255, 255, 255), RIGHT, 0)
        elif self.orientation == "h":
            self.orientation = "v"
            if self.vx > 0:
                self.vy = self.height
                self.image.fill((0, 0, 0))
                pygame.draw.polygon(self.image, (255, 255, 255), DOWN, 0)
            elif self.vx < 0:
                self.vy = -self.height
                self.image.fill((0, 0, 0))
                pygame.draw.polygon(self.image, (255, 255, 255), UP, 0)

    # input: string
    # output: none
    # side-effect: changes the instrument being played
    # Has to be a class method in other to affect all other instances of the Oto objects
    @classmethod
    def changeInstrument(cls, newInstrument):
        Oto.instrument = newInstrument

        # Reload sounds
        sounds = []
        Oto.C1 = pygame.mixer.Sound("Sounds/{}C1.wav".format(Oto.instrument))
        sounds.append(Oto.C1)
        Oto.D = pygame.mixer.Sound("Sounds/{}D.wav".format(Oto.instrument))
        sounds.append(Oto.D)
        Oto.E = pygame.mixer.Sound("Sounds/{}E.wav".format(Oto.instrument))
        sounds.append(Oto.E)
        Oto.F = pygame.mixer.Sound("Sounds/{}F.wav".format(Oto.instrument))
        sounds.append(Oto.F)
        Oto.G = pygame.mixer.Sound("Sounds/{}G.wav".format(Oto.instrument))
        sounds.append(Oto.G)
        Oto.A = pygame.mixer.Sound("Sounds/{}A.wav".format(Oto.instrument))
        sounds.append(Oto.A)
        Oto.B = pygame.mixer.Sound("Sounds/{}B.wav".format(Oto.instrument))
        sounds.append(Oto.B)
        Oto.C2 = pygame.mixer.Sound("Sounds/{}C2.wav".format(Oto.instrument))
        sounds.append(Oto.C2)
        Oto.D2 = pygame.mixer.Sound("Sounds/{}D2.wav".format(Oto.instrument))
        sounds.append(Oto.D2)

        # Set volumes
        for sound in sounds:
            sound.set_volume(1)

    # input: none
    # output: x coordinates of object
    # side-effect: none
    # Not really used, but here just in case
    def getX(self):
        return self.rect.x

    # input: none
    # output: y coordinates of object
    # side-effect: none
    # Not really used, but here just in case
    def getY(self):
        return self.rect.y


