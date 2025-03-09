from circleshape import *
from constants import *
from player import *
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        random_vector1 = self.velocity.rotate(random_angle)
        random_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = random_vector1 * 1.3
        asteroid2.velocity = random_vector2 * 1.3
