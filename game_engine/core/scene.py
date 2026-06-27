"""
Scene Base Class - All game scenes inherit from this
"""
import pygame
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .game import Game


class Scene(ABC):
    """Base class for all game scenes."""
    
    def __init__(self):
        self.game: 'Game' = None
        
    @abstractmethod
    def enter(self) -> None:
        """Called when the scene is entered."""
        pass
        
    @abstractmethod
    def exit(self) -> None:
        """Called when the scene is exited."""
        pass
        
    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle input events."""
        pass
        
    @abstractmethod
    def update(self, delta_time: float) -> None:
        """Update scene logic."""
        pass
        
    @abstractmethod
    def render(self, screen: pygame.Surface) -> None:
        """Render the scene."""
        pass
