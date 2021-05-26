# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

'''import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

'''import pygame
pygame.mixer.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
input('Musica')'''

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta?')
