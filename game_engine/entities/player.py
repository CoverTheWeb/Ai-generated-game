"""
Player Entity - Controllable character
"""
import pygame
from .entity import Entity
from ..utils.vector import Vector2


class Player(Entity):
    """Player entity with keyboard controls."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        super().__init__(x, y, 40, 40)
        self.color = (0, 128, 255)
        self.speed = 300.0
        self.jump_strength = -500.0
        self.gravity = 1200.0
        self.is_grounded = False
        self.lives = 3
        self.score = 0
        
    def handle_input(self, keys: pygame.key.ScancodeWrapper) -> None:
        """Handle player input."""
        self.acceleration = Vector2(0, self.gravity)
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.acceleration.x = -self.speed * 2
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.acceleration.x = self.speed * 2
        if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.is_grounded:
            self.velocity.y = self.jump_strength
            self.is_grounded = False
            
    def update(self, delta_time: float) -> None:
        """Update player physics."""
        super().update(delta_time)
        
        # Screen boundaries
        if self.position.x < 0:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = 0
            
    def take_damage(self, amount: int = 1) -> None:
        """Reduce player lives."""
        self.lives -= amount
        if self.lives <= 0:
            self.is_active = False
