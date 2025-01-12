import pygame

#Inicializar o mixer de áudio do pygame
pygame.mixer.init()

#Carregar o arquivo mp3
pygame.mixer.music.load('D:/BACKUP RAFAEL/Feeling.mp3')

#Reproduzir o áudio
pygame.mixer.music.play()

#Manter o programa em execução enquanto o áudio estiver aberto
while pygame.mixer.music.get_busy():
    pass
