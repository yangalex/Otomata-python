ITP 115 Final Project
Made by: Alexandre Yang
Program Name: Otomata Clone
Teacher: Rob Parke


This project was inspired by the online generative music sequencer Otomata (http://www.earslap.com/projectslab/otomata).
It was built using the Pygame library and Python 3.3

Requirements to run the program:
- Pygame installed
    - Download from http://www.pygame.org/download.shtml
        Further instructions if needed: http://inventwithpython.com/pygame/chapter1.html
    - If having difficulties on mac or Python3 incompatibility issues refer to these guides that I used:
        http://coding2learn.org/blog/2014/03/11/installing-pygame-on-mac-os-x-with-python-3/
        http://juliaelman.com/blog/2013/04/02/installing-pygame-on-osx-mountain-lion/
        http://florian-berger.de/en/articles/installing-pygame-for-python-3-on-os-x

- Python 2 or 3
- All the sound files located in the Sounds folder (DO NOT CHANGE FILE NAMES)


Program Instructions
#====================================================================================================================#
Run from Otomata.py file

Left-click on any square to create a cell on its place and right-click it to rotate it (as many times as you want).Click
on a cell again to delete it. Then press play to start the program.

When the program is running, the cells will move in the direction determined by their states (up, down, right, left).
Every time they hit a wall, it plays a sound whose tone and pitch is determined by its x, y position and then changes
its direction. If two cells collide with each other they each rotate 90 degrees clockwise.

"This set of rules produces chaotic results in some settings, therefore you can end up with never repeating, gradually
evolving sequences." - Original Otomata website

On the bottom of the music grid, you're able to play and pause the cells, clear the board and increase or decrease
the tempo in which the program runs (caution: very low frame-rates such as 1 may use up a lot of your CPU).

On the right side, you're able to select different instruments that are played. Mess around with the settings and
have fun creating some music.

Note: Sometimes you'll notice that two cells will end up going around in circles. This is not a bug. It's part of the
program and are called "oscillators". They can be used to come up with more interesting sequences.

#====================================================================================================================#

Resources Used
#====================================================================================================================#
Official Pygame documentation
- http://www.pygame.org/docs/

Learning how to use Pygame
- https://lorenzod8n.wordpress.com/category/pygame-tutorial/
- http://eli.thegreenplace.net/category/programming/python/pygame-tutorial/

For using Sprites and other Pygame stuff
- http://programarcadegames.com/index.php?chapter=introduction_to_sprites

For general questions and etc.
- http://stackoverflow.com/

Aside from these resources, almost all of the code is my own work

#====================================================================================================================#

Thank you and hope you enjoyed it!

