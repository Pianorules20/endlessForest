#main.py

import pygame, sys, os, pygame.locals, pygame.mixer
import math, random, time
import awards, enemies, goodGuys, maps, movement, settings, window

pygame.init()
pygame.mixer.init()
window.Screen.blit()

class Start():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    goodGuys.Allies.Hero.left +=1
                    goodGuys.Allies.Hero.facing = 'left'
                elif event.key == pygame.K_RIGHT:
                    goodGuys.Allies.Hero.right +=1
                    goodGuys.Allies.Hero.facing = 'right'
                elif event.key == pygame.K_UP:
                    goodGuys.Allies.Hero.up +=1
                elif event.key == pygame.K_DOWN:
                    goodGuys.Allies.Hero.down +=1
            window.Screen.blit()
            pygame.display.update()
            if enemies.Army.group == [] and awards.Titles.medal == True:
                print('Congratulations!  You Won!!!')

Start()