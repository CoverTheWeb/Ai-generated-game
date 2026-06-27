"""
Entity Base Class - All game entities inherit from this
"""
import pygame
from ..utils.vector import Vector2


class Entity:
    """Base class for all game entities."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0, width: int = 32, height: int = 32):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.width = width
        self.height = height
        self.color = (255, 255, 255)
        self.is_active = True
        self.tags = set()
        
    def update(self, delta_time: float) -> None:
        """Update entity physics."""
        self.velocity += self.acceleration * delta_time
        self.position += self.velocity * delta_time
        
    def render(self, screen: pygame.Surface) -> None:
        """Render the entity."""
        rect = self.get_rect()
        pygame.draw.rect(screen, self.color, rect)
        
    def get_rect(self) -> pygame.Rect:
        """Get pygame Rect for collision detection."""
        return pygame.Rect(
            int(self.position.x),
            int(self.position.y),
            self.width,
            self.height
        )
        
    def collides_with(self, other: 'Entity') -> bool:
        """Check collision with another entity."""
        return self.get_rect().colliderect(other.get_rect())
        
    def add_tag(self, tag: str) -> None:
        """Add a tag to the entity."""
        self.tags.add(tag)
        
    def has_tag(self, tag: str) -> bool:
        """Check if entity has a tag."""
        return tag in self.tags
