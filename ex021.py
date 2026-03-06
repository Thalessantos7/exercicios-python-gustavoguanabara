# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(r"C:\Users\Thales\Downloads\Skillet_-_Monster_CeeNaija.com_.mp3")
pygame.mixer.music.play()

input("Pressione ENTER para parar a música...")

pygame.mixer.music.stop()
pygame.quit()