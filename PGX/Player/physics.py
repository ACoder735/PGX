import pygame.math

# Expose Vector2 for users (Makes math easy)
Vector = pygame.math.Vector2

def apply_gravity(obj, speed=1):
    """
    Applies gravity to the object.
    Increases the Y position by 'speed'.
    """
    obj.y += speed

def apply_friction(velocity, friction=0.9):
    """
    Slows down a velocity vector over time.
    Returns the new Vector.
    Usage: obj_vel = PGX.Player.physics.apply_friction(obj_vel)
    """
    velocity *= friction
    return velocity

def move_towards(obj, target_pos, speed):
    """
    Moves an object towards a target (x, y).
    Useful for enemies chasing the player.
    """
    # Create vectors
    start_vec = Vector(obj.x, obj.y)
    target_vec = Vector(target_pos[0], target_pos[1])
    
    # Calculate direction
    direction = target_vec - start_vec
    
    # Normalize (make length 1) and multiply by speed
    if direction.length() > 0:
        direction = direction.normalize() * speed
        
    # Update position
    obj.x += direction.x
    obj.y += direction.y

def bounce(obj, direction, elasticity=1.0):
    """
    Reverses velocity based on direction and elasticity (bounciness).
    direction = Vector(1, 0) (Wall on Left), Vector(-1, 0) (Wall on Right)
    """
    velocity = Vector(direction.x * -1 * elasticity, direction.y * -1 * elasticity)
    return velocity



__all__ = ['apply_gravity', 'apply_friction', 'move_towards', 'bounce', 'Vector']
