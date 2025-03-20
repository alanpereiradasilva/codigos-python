import pygame
pygame.init()
while True:
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
