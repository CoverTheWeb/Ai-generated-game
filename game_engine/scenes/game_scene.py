"""
Main Game Scene - Platformer gameplay
"""
import pygame
from ..core.scene import Scene
from ..entities.player import Player
from ..entities.platform import Platform
from ..entities.collectible import Collectible
from ..entities.enemy import Enemy
from ..systems.collision import CollisionSystem


class GameScene(Scene):
    """Main platformer game scene."""
    
    def __init__(self):
        super().__init__()
        self.player = None
        self.platforms = []
        self.collectibles = []
        self.enemies = []
        self.collision_system = CollisionSystem()
        self.font = None
        
    def enter(self) -> None:
        """Initialize the game scene."""
        # Create player
        self.player = Player(100, 400)
        
        # Create platforms
        self.platforms = [
            Platform(0, 550, 800, 50),      # Ground
            Platform(200, 450, 150, 20),
            Platform(400, 350, 150, 20),
            Platform(600, 250, 150, 20),
            Platform(100, 150, 150, 20),
        ]
        
        # Create collectibles
        self.collectibles = [
            Collectible(250, 410, 10),
            Collectible(450, 310, 10),
            Collectible(650, 210, 10),
            Collectible(150, 110, 10),
        ]
        
        # Create enemies
        self.enemies = [
            Enemy(400, 320, 120, 40),
            Enemy(600, 220, 100, 50),
        ]
        
        self.font = pygame.font.Font(None, 36)
        
    def exit(self) -> None:
        """Cleanup when leaving scene."""
        pass
        
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle input events."""
        pass
        
    def update(self, delta_time: float) -> None:
        """Update game logic."""
        if not self.player.is_active:
            # Player died, reset scene
            self.game.set_scene("game")
            return
            
        # Handle player input
        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)
        
        # Update player
        self.player.is_grounded = False
        self.player.update(delta_time)
        
        # Check platform collisions
        for platform in self.platforms:
            self.collision_system.resolve_platform_collision(self.player, platform)
            
        # Update enemies
        for enemy in self.enemies:
            enemy.update(delta_time)
            if self.player.collides_with(enemy):
                self.player.take_damage(1)
                
        # Check collectible collisions
        for collectible in self.collectibles:
            if not collectible.collected and self.player.collides_with(collectible):
                collectible.collected = True
                self.player.score += collectible.value
                
        # Check if player fell off screen
        if self.player.position.y > self.game.height:
            self.player.take_damage(3)
            
    def render(self, screen: pygame.Surface) -> None:
        """Render the game."""
        # Render platforms
        for platform in self.platforms:
            platform.render(screen)
            
        # Render collectibles
        for collectible in self.collectibles:
            collectible.render(screen)
            
        # Render enemies
        for enemy in self.enemies:
            enemy.render(screen)
            
        # Render player
        self.player.render(screen)
        
        # Render UI
        score_text = self.font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))
