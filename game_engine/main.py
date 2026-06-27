#!/usr/bin/env python3
"""
Main entry point for the Platformer Game
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game_engine import Game, MenuScene, GameScene


def main():
    """Create and run the game."""
    # Create game engine
    game = Game(
        title="Platformer Game - Custom Engine",
        width=800,
        height=600,
        fps=60
    )
    
    # Add scenes
    game.add_scene("menu", MenuScene())
    game.add_scene("game", GameScene())
    
    # Run the game starting from menu
    print("=" * 50)
    print("Platformer Game - Custom Game Engine")
    print("=" * 50)
    print("\nControls:")
    print("  Arrow Keys / WASD - Move left/right")
    print("  Space / W / Up - Jump")
    print("  ESC - Quit")
    print("\nStarting game...")
    print("=" * 50)
    
    game.run("menu")


if __name__ == "__main__":
    main()
