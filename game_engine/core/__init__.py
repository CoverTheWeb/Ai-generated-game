"""
Game Engine Core - Main Game Loop and Engine Management
"""
import pygame
import sys
from typing import List, Optional
from .scene import Scene


class Game:
    """Main game engine class that manages the game loop."""
    
    def __init__(self, title: str = "Game Engine", width: int = 800, height: int = 600, fps: int = 60):
        pygame.init()
        try:
            pygame.mixer.init()
        except pygame.error:
            # Audio not available (e.g., in headless environment)
            pass
        
        self.title = title
        self.width = width
        self.height = height
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        
        self.running = False
        self.current_scene: Optional[Scene] = None
        self.scenes: dict = {}
        self.delta_time = 0.0
        
    def add_scene(self, name: str, scene: Scene) -> None:
        """Add a scene to the game."""
        self.scenes[name] = scene
        scene.game = self
        
    def set_scene(self, name: str) -> None:
        """Switch to a different scene."""
        if self.current_scene:
            self.current_scene.exit()
        if name in self.scenes:
            self.current_scene = self.scenes[name]
            self.current_scene.enter()
            
    def handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if self.current_scene:
                self.current_scene.handle_event(event)
                
    def update(self) -> None:
        """Update game logic."""
        if self.current_scene:
            self.current_scene.update(self.delta_time)
            
    def render(self) -> None:
        """Render the game."""
        self.screen.fill((0, 0, 0))
        if self.current_scene:
            self.current_scene.render(self.screen)
        pygame.display.flip()
        
    def run(self, initial_scene: str) -> None:
        """Start the game loop."""
        self.set_scene(initial_scene)
        self.running = True
        
        while self.running:
            self.delta_time = self.clock.tick(self.fps) / 1000.0
            self.handle_events()
            self.update()
            self.render()
            
        pygame.quit()
        sys.exit()
