# Mundo 1 - Desafio 021
# Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
