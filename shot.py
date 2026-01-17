import pygame
from constants import LINE_WIDTH, PLAYER_SHOOT_SPEED
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(self, x, y, radius)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def shoot_from_player(self):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
        self.position += rotated_with_speed_vector
