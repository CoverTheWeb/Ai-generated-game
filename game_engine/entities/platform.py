"""
Platform Entity - Static platforms for player to stand on
"""
import pygame
from .entity import Entity


class Platform(Entity):
    """Static platform entity."""
    
    def __init__(self, x: float, y: float, width: int = 100, height: int = 20):
        super().__init__(x, y, width, height)
        self.color = (139, 69, 19)  # Brown color
        self.add_tag("platform")
        
    def update(self, delta_time: float) -> None:
        """Platforms don't move."""
        pass
