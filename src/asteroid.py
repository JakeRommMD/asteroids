import pygame
import random
from constants import *
from circleshape import CircleShape 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # Initial rotation angle in degrees

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Remove the current asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Create two smaller asteroids using the rotate method on the asteroid's velocity vector to create 
        #2 new vectors that are rotated by random_angle and -random_angle
        random_angle = random.uniform(-20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create two new asteroid objects at the current asteroid position with the new radius
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity1 * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = new_velocity2 * 1.2


