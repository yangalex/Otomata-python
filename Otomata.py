"""
RUN FROM THIS FILE

Alexandre Yang
ITP 115
Final Project
05/08/2014

Description:
Refer to readme.txt
"""

import pygame
from Oto import Oto
from Button import Button
from Label import Label


# Input: pygame.Surface, tuple, int, int, int, int
# Output: none
# Side-effect: Draws the grid on the screen
def drawBoard(surface, color, w, h, tileWidth, tileHeight):
    # Draw lines
    for x in range(tileWidth, w+1, tileWidth):
        pygame.draw.line(surface, color, (x, 0), (x, h))
    for y in range(tileHeight, h+1, tileHeight):
        pygame.draw.line(surface, color, (0, y), (w, y))


# Input: int, int
# Output: pygame.sprite.Sprite
# Side-effect: none
# Description: Creates a sprite to represent the position of the mouse-click
def createMouseClick(mouseX, mouseY):
    mouseClick = pygame.sprite.Sprite()
    mouseClick.image = pygame.Surface((1, 1))
    mouseClick.rect = mouseClick.image.get_rect()
    mouseClick.rect.x = mouseX
    mouseClick.rect.y = mouseY

    return mouseClick


def main():
    # Set general variables
    screenW = 850
    screenH = 775
    boardW = 675
    boardH = 675
    tileWidth = 75
    tileHeight = 75
    running = True
    screen = pygame.display.set_mode((screenW, screenH))    # Create pygame Surface
    clock = pygame.time.Clock()     # Create pygame Clock
    BPM = 4
    active = False
    bgColor = 0, 0, 0
    lineColor = 255, 255, 255

    # Create sprite groups (necessary to call draw() method)
    otoList = pygame.sprite.Group()
    buttonList = pygame.sprite.Group()
    labelList = pygame.sprite.Group()

    # Create Menu Buttons and add them to buttonList sprite group
    playButton = Button(screen, 100, boardH+40, 50, 50, "Play")
    buttonList.add(playButton)
    pauseButton = Button(screen, 200, boardH+40, 75, 50, "Pause")
    buttonList.add(pauseButton)
    clearButton = Button(screen, 320, boardH+40, 70, 50, "Clear")
    buttonList.add(clearButton)
    plusBPMButton = Button(screen, 430, boardH+40, 65, 50, "BPM+")
    buttonList.add(plusBPMButton)
    minusBPMButton = Button(screen, 530, boardH+40, 65, 50, "BPM-")
    buttonList.add(minusBPMButton)
    originalButton = Button(screen, 700, 30, 140, 50, "Original")
    buttonList.add(originalButton)
    clarinetButton = Button(screen, 700, 130, 140, 50, "Clarinet")
    buttonList.add(clarinetButton)
    guitarButton = Button(screen, 700, 220, 140, 50, "Guitar")
    buttonList.add(guitarButton)
    synthButton = Button(screen, 700, 320, 140, 50, "Synth")
    buttonList.add(synthButton)
    pianoButton = Button(screen, 700, 420, 140, 50, "Piano")
    buttonList.add(pianoButton)
    piano2Button = Button(screen, 700, 520, 140, 50, "Piano2")
    buttonList.add(piano2Button)
    trumpetButton = Button(screen, 700, 620, 140, 50, "Trumpet")
    buttonList.add(trumpetButton)

    # main Pygame loop
    while running:
        # Resets the screen
        screen.fill(bgColor)
        # Draws the grid
        drawBoard(screen, lineColor, boardW, boardH, tileWidth, tileHeight)

        # Draw menu
        buttonList.draw(screen)

        # Listen for events
        for event in pygame.event.get():
            # If user closes window
            if event.type == pygame.QUIT:
                running = False
            # If user clicks mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                # Rounds mouse positions down to nearest hundred (Used to position the cells and for simplicity)
                otoPosX = (mouseX // tileWidth) * tileWidth
                otoPosY = (mouseY//tileHeight) * tileHeight

                # Create a tiny sprite where the mouse was clicked to use in collision detection
                mouseClick = createMouseClick(mouseX, mouseY)

                # If left button was clicked
                if event.button == 1:
                    # Check to see if mouseClick collided with any sprite in the otoList
                    clickedBlock = pygame.sprite.spritecollide(mouseClick, otoList, False)
                    # Check to see if mouseClick collided with any menu button
                    clickedMenu = pygame.sprite.spritecollide(mouseClick, buttonList, False)

                    # If a cell was clicked, then delete it
                    if clickedBlock:
                        otoList.remove(clickedBlock[0])
                    # Handle the menu button click events
                    elif clickedMenu:
                        if clickedMenu[0] == playButton:
                            active = True
                        elif clickedMenu[0] == pauseButton:
                            active = False
                        elif clickedMenu[0] == clearButton:
                            otoList.empty()
                        elif clickedMenu[0] == plusBPMButton:
                            BPM += 1
                        elif clickedMenu[0] == minusBPMButton and BPM != 1:
                            BPM -= 1
                        elif clickedMenu[0] == originalButton:
                            Oto.changeInstrument("")
                        elif clickedMenu[0] == clarinetButton:
                            Oto.changeInstrument("clarinet")
                        elif clickedMenu[0] == guitarButton:
                            Oto.changeInstrument("Guitar")
                        elif clickedMenu[0] == synthButton:
                            Oto.changeInstrument("Synth")
                        elif clickedMenu[0] == pianoButton:
                            Oto.changeInstrument("Piano")
                        elif clickedMenu[0] == piano2Button:
                            Oto.changeInstrument("Piano2")
                        elif clickedMenu[0] == trumpetButton:
                            Oto.changeInstrument("trumpet")

                    # If the grid was clicked then create a new cell at the position (an 'Oto' object)
                    else:
                        if mouseY < boardH and mouseX < boardW:
                            oto = Oto(screen, tileWidth, tileHeight, boardW, boardH)
                            oto.rect.x = otoPosX
                            oto.rect.y = otoPosY
                            otoList.add(oto)

                # if right button was clicked
                elif event.button == 3:
                    clickedBlock = pygame.sprite.spritecollide(mouseClick, otoList, False)
                    # Rotate cell clockwise
                    if clickedBlock:
                        clickedBlock[0].changeState()

        # Draw every cell to the screen
        otoList.draw(screen)
        # Move the cells
        if active:
            otoList.update()

        # Check to see if any cells collided
        for oto in otoList:
            oto.checkCollision(otoList)

        # Draw and update BPM label
        BPMLabel = Label(screen, 620, boardH+40, 50, 50, str(BPM))
        labelList.empty()
        labelList.add(BPMLabel)
        labelList.draw(screen)

        # Update the screen
        pygame.display.flip()
        # Set the Frames Per Second
        clock.tick(BPM)

main()