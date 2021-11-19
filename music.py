import pygame
#from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load('Playlist - Beatmaker_s Arena - 500608471 --- Jamendo - MP3.zip')
mixer.music.play()

game_sound = pygame.mixer.sound('Playlist - Beatmaker_s Arena - 500608471 --- Jamendo - MP3.zip')
game_sound.play()