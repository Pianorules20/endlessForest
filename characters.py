# characters.py

import pygame, goodGuys, enemies
'''name, left, right, up, down, jump, facing, inverted, speed, speak, skin, xAxis, yAxis, rect'''

class Cast():

    rufus = goodGuys.Hero('Felix', 0, 0, 0, 0, 0, 'right', 'not inverted', 10, 'Good morning!', \
                'sprites/_iso/Walk/Tuscan_Walk_00000.png', 
                0,0, pygame.Rect(0,0,100,100))


    larky = enemies.Soldier('Larky', 0, 0, 0, 0, 0, 'right', 'not inverted', 10, 'Avant Guarde!', \
                'sprites/_top/Walk/_layers/shadow/_no-sword/shadow_top-Tuscan_Walk_00000.png', 
                0, 0, pygame.Rect(0,0, 100, 100))