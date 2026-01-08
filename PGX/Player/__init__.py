import PGX.Player.collisions as collisions
import PGX.Player.physics as physics


def clamp(value, minimum, maximum):
    """
    Keeps a number between a minimum and maximum.
    
    Example:
        # Keep player_x between 0 and 800
        player.x = PGX.clamp(player.x, 0, 800)
    """
    return max(minimum, min(value, maximum))


__all__ = ['collisions', 'clamp', 'phyiscs']
