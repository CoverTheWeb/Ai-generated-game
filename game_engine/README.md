# Custom 2D Game Engine with Platformer Game

A complete 2D game engine built from scratch using Python and Pygame, featuring a fully functional platformer game.

## Engine Architecture

### Core Components

- **Game Engine** (`core/`): Main game loop, scene management, event handling
- **Scenes** (`scenes/`): Different game states (menu, gameplay)
- **Entities** (`entities/`): Game objects (player, platforms, enemies, collectibles)
- **Systems** (`systems/`): Game logic systems (collision detection)
- **Utils** (`utils/`): Helper utilities (Vector2 math)

### Key Features

1. **Scene Management**: Switch between different game states
2. **Entity Component System**: Base entity class with inheritance
3. **Physics System**: Velocity, acceleration, gravity
4. **Collision Detection**: AABB collision with resolution
5. **Input Handling**: Keyboard and mouse support
6. **Delta Time**: Frame-rate independent movement

## Project Structure

```
game_engine/
├── __init__.py          # Package exports
├── main.py              # Game entry point
├── core/
│   ├── __init__.py      # Game engine class
│   └── scene.py         # Scene base class
├── entities/
│   ├── __init__.py
│   ├── entity.py        # Base entity
│   ├── player.py        # Player character
│   ├── platform.py      # Static platforms
│   ├── collectible.py   # Collectible items
│   └── enemy.py         # AI enemies
├── scenes/
│   ├── __init__.py
│   ├── menu_scene.py    # Main menu
│   └── game_scene.py    # Gameplay scene
├── systems/
│   ├── __init__.py
│   └── collision.py     # Collision system
├── utils/
│   ├── __init__.py
│   └── vector.py        # Vector2 math
└── assets/              # Game assets (images, sounds)
```

## How to Run

```bash
cd /workspace
python game_engine/main.py
```

## Controls

- **Arrow Keys / WASD**: Move left/right
- **Space / W / Up**: Jump
- **ESC**: Quit game

## Game Objective

- Collect all gold coins for points
- Avoid red enemies
- Don't fall off the platforms
- You have 3 lives

## Extending the Engine

### Adding a New Entity

```python
from game_engine.entities.entity import Entity

class MyEntity(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, width=32, height=32)
        self.color = (255, 0, 0)
    
    def update(self, delta_time):
        # Custom update logic
        pass
    
    def render(self, screen):
        # Custom rendering
        super().render(screen)
```

### Adding a New Scene

```python
from game_engine.core.scene import Scene

class MyScene(Scene):
    def enter(self):
        # Setup code
        pass
    
    def exit(self):
        # Cleanup code
        pass
    
    def handle_event(self, event):
        # Input handling
        pass
    
    def update(self, delta_time):
        # Game logic
        pass
    
    def render(self, screen):
        # Drawing code
        pass
```

## License

MIT License - Free to use and modify
