import pygame
from Constants import Constants as const
from random import choice, randint
from enemy import Enemy
from projectile import Bullet


class Enemies:
    def __init__(self, count=const.ENEMY_COUNT_STARTING, speed=const.ENEMY_SPEED_STARTING):
        self.alive_enemies = []
        self.dead_enemies = []
        for _ in range(count):
            self.alive_enemies.append(Enemy(x=randint(const.TILE_SIZE, const.SCREEN_W - const.TILE_SIZE - 32),
                                            y=randint(const.TILE_SIZE, const.SCREEN_H - const.TILE_SIZE - 32),
                                            speed=speed))

    def draw(self, screen):
        for enemy in self.alive_enemies:
            enemy.draw(screen)

    def move(self):
        for enemy in self.alive_enemies:
            enemy.move()

    def check_if_dead(self, active_projectiles):
        kill_count = 0

        for enemy in self.alive_enemies:
            for proj in active_projectiles:
                if enemy.is_colliding(proj.x, proj.y, Bullet.bullet_radius, Bullet.bullet_radius):
                    kill_count += 1
                    self.dead_enemies.append(enemy)
                    self.alive_enemies.remove(enemy)  # FIXME bad to remove from an existing list, crashes when multiple projectiles hit

        return kill_count
