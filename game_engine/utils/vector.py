"""
Vector2 - 2D Vector Math Utility
"""
import math


class Vector2:
    """2D Vector class for position, velocity, and direction."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y
        
    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)
        
    def __mul__(self, scalar: float) -> 'Vector2':
        return Vector2(self.x * scalar, self.y * scalar)
        
    def __truediv__(self, scalar: float) -> 'Vector2':
        if scalar != 0:
            return Vector2(self.x / scalar, self.y / scalar)
        return Vector2(0, 0)
        
    def __eq__(self, other: 'Vector2') -> bool:
        return self.x == other.x and self.y == other.y
        
    def magnitude(self) -> float:
        """Get the length of the vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2)
        
    def normalize(self) -> 'Vector2':
        """Return a normalized version of this vector."""
        mag = self.magnitude()
        if mag > 0:
            return self / mag
        return Vector2(0, 0)
        
    def dot(self, other: 'Vector2') -> float:
        """Dot product with another vector."""
        return self.x * other.x + self.y * other.y
        
    def distance_to(self, other: 'Vector2') -> float:
        """Calculate distance to another vector."""
        return (other - self).magnitude()
        
    def copy(self) -> 'Vector2':
        """Create a copy of this vector."""
        return Vector2(self.x, self.y)
        
    def __repr__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
