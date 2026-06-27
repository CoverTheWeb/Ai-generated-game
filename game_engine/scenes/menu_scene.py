"""
Menu Scene - Main menu with start button
"""
import pygame
from ..core.scene import Scene


class MenuScene(Scene):
    """Main menu scene."""
    
    def __init__(self):
        super().__init__()
        self.font_large = None
        self.font_small = None
        self.button_rect = None
        
    def enter(self) -> None:
        """Initialize the menu."""
        self.font_large = pygame.font.Font(None, 72)
        self.font_small = pygame.font.Font(None, 36)
        # Center button
        self.button_rect = pygame.Rect(
            self.game.width // 2 - 100,
            self.game.height // 2 + 50,
            200, 50
        )
        
    def exit(self) -> None:
        """Cleanup."""
        pass
        
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle button clicks."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                if self.button_rect.collidepoint(mouse_pos):
                    self.game.set_scene("game")
                    
    def update(self, delta_time: float) -> None:
        """No updates needed for menu."""
        pass
        
    def render(self, screen: pygame.Surface) -> None:
        """Render the menu."""
        # Title
        title = self.font_large.render("Platformer Game", True, (0, 128, 255))
        title_rect = title.get_rect(center=(self.game.width // 2, self.game.height // 2 - 50))
        screen.blit(title, title_rect)
        
        # Instructions
        instructions = self.font_small.render("Click START to play!", True, (255, 255, 255))
        inst_rect = instructions.get_rect(center=(self.game.width // 2, self.game.height // 2))
        screen.blit(instructions, inst_rect)
        
        # Start button
        pygame.draw.rect(screen, (0, 200, 0), self.button_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.button_rect, 3)
        start_text = self.font_small.render("START", True, (255, 255, 255))
        start_rect = start_text.get_rect(center=self.button_rect.center)
        screen.blit(start_text, start_rect)
        
        # Controls info
        controls = [
            "Controls:",
            "Arrow Keys / WASD - Move",
            "Space / W / Up - Jump",
            "ESC - Quit"
        ]
        for i, text in enumerate(controls):
            ctrl_text = self.font_small.render(text, True, (200, 200, 200))
            screen.blit(ctrl_text, (self.game.width // 2 - 100, self.game.height - 150 + i * 30))
