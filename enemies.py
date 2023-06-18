# enemies.py

import pygame

class Army():
    group = []

    def init(self, name, left, right, up, down, jump, facing, inverted, speed, speak, skin, xAxis, yAxis, rect):
        self.name = name
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.jump = jump
        self.facing = facing
        self.inverted = inverted
        self.speed = speed
        self.speak = speak
        self.skin = skin
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.rect = rect
    
    def speak():
        print(f'{Army.speak}')

class Soldier(Army):
    pass

class Mount(Army):
    pass

class Captain(Army):
    pass

