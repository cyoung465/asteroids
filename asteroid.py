import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "pink", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            velocitya = self.velocity.rotate(rand_angle)
            velocityb = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asterA = Asteroid(self.position[0], self.position[1], new_radius)
            asterB = Asteroid(self.position[0], self.position[1], new_radius)
            asterA.velocity = velocitya*1.2
            asterB.velocity = velocityb*1.2

    def update(self, dt: float):
        self.position += self.velocity * dt
