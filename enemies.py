import pygame
from Constants import Constants as const
from random import choice, randint
from enemy import Enemy


class Enemies:
    def __init__(self, count=6):
        self.alive_enemies = []
        for _ in range(count):
            self.alive_enemies.append(Enemy(x=randint(const.TILE_SIZE, const.SCREEN_W - const.TILE_SIZE - 32), y = randint(const.TILE_SIZE, const.SCREEN_H - const.TILE_SIZE - 32 )))

    def draw(self, screen):
        for enemy in self.alive_enemies:
            enemy.draw(screen)

    def move(self):
        for enemy in self.alive_enemies:
            enemy.move()