import pygame
from constants import *
from circleshape import CircleShape 


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # Initial rotation angle in degrees
        self.shot_timer = 0
        

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:    
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt) 
        if keys[pygame.K_SPACE]:
            shot = self.shoot()
            
        self.shot_timer -= dt

    def move(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation) 
        velocity = direction * PLAYER_SHOOT_SPEED
        shot_position = self.position + direction * self.radius
        if self.shot_timer > 0:
            return None
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        return Shot(shot_position.x, shot_position.y, self.rotation, velocity)
        

class Shot(CircleShape):
    def __init__(self, x, y, rotation, velocity):
        super().__init__(x, y, SHOT_RADIUS)  

        self.rotation = rotation
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), self.radius)