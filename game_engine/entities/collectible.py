"""
Collectible Entity - Items player can collect
"""
import pygame
from .entity import Entity


class Collectible(Entity):
    """Collectible item that gives points."""
    
    def __init__(self, x: float, y: float, value: int = 10):
        super().__init__(x, y, 20, 20)
        self.color = (255, 215, 0)  # Gold color
        self.value = value
        self.add_tag("collectible")
        self.collected = False
        
    def render(self, screen: pygame.Surface) -> None:
        """Render as a circle."""
        if not self.collected:
            center = (int(self.position.x + self.width // 2), 
                     int(self.position.y + self.height // 2))
            pygame.draw.circle(screen, self.color, center, self.width // 2)
