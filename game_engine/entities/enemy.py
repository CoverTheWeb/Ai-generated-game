"""
Enemy Entity - AI controlled obstacles
"""
import pygame
from .entity import Entity
from ..utils.vector import Vector2


class Enemy(Entity):
    """Simple enemy that moves back and forth."""
    
    def __init__(self, x: float, y: float, range_x: int = 100, speed: float = 50.0):
        super().__init__(x, y, 30, 30)
        self.color = (255, 64, 64)  # Red color
        self.start_x = x
        self.range_x = range_x
        self.speed = speed
        self.direction = 1
        self.add_tag("enemy")
        
    def update(self, delta_time: float) -> None:
        """Move back and forth within range."""
        self.position.x += self.direction * self.speed * delta_time
        
        if self.position.x > self.start_x + self.range_x:
            self.direction = -1
        elif self.position.x < self.start_x:
            self.direction = 1
            
    def render(self, screen: pygame.Surface) -> None:
        """Render enemy with eyes."""
        super().render(screen)
        # Draw eyes
        eye_offset = self.width // 4
        eye_y = int(self.position.y) + 8
        pygame.draw.circle(screen, (255, 255, 255), 
                          (int(self.position.x) + eye_offset, eye_y), 4)
        pygame.draw.circle(screen, (255, 255, 255), 
                          (int(self.position.x) + self.width - eye_offset, eye_y), 4)
