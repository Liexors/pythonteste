import pygame

#Iniciar o pygame
pygame.init()

#Carregar a música
pygame.mixer.music.load('D:BACKUP RAFAEL/Feeling.mp3')

#Tocar o mp3
pygame.mixer_music.play()

#Espera a música terminar para finalizar o programa
pygame.event.wait()
