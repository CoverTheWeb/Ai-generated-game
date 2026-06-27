"""
Collision System - Handle entity collisions
"""
import pygame
from ..entities.entity import Entity


class CollisionSystem:
    """Handles collision detection and resolution."""
    
    def __init__(self):
        self.entities = []
        
    def add_entity(self, entity: Entity) -> None:
        """Add entity to collision system."""
        self.entities.append(entity)
        
    def remove_entity(self, entity: Entity) -> None:
        """Remove entity from collision system."""
        if entity in self.entities:
            self.entities.remove(entity)
            
    def check_collisions(self) -> list:
        """Check all collisions and return collision pairs."""
        collisions = []
        for i, entity1 in enumerate(self.entities):
            for entity2 in self.entities[i+1:]:
                if entity1.collides_with(entity2):
                    collisions.append((entity1, entity2))
        return collisions
        
    def resolve_platform_collision(self, player: Entity, platform: Entity) -> bool:
        """Resolve collision between player and platform."""
        if not player.collides_with(platform):
            return False
            
        player_rect = player.get_rect()
        platform_rect = platform.get_rect()
        
        # Calculate overlap
        overlap_x = min(player_rect.right - platform_rect.left, 
                       platform_rect.right - player_rect.left)
        overlap_y = min(player_rect.bottom - platform_rect.top, 
                       platform_rect.bottom - player_rect.top)
        
        # Resolve smallest overlap
        if overlap_x < overlap_y:
            # Horizontal collision
            if player.velocity.x > 0:
                player.position.x = platform_rect.left - player.width
            else:
                player.position.x = platform_rect.right
            player.velocity.x = 0
        else:
            # Vertical collision
            if player.velocity.y > 0:
                # Landing on platform
                player.position.y = platform_rect.top - player.height
                player.is_grounded = True
                player.velocity.y = 0
            else:
                # Hitting head on platform
                player.position.y = platform_rect.bottom
                player.velocity.y = 0
                
        return True
        
    def update(self, entities: list) -> None:
        """Update collision system with current entities."""
        self.entities = [e for e in entities if e.is_active]
