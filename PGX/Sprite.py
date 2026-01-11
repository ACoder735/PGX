import pygame
from PIL import Image

class Sprite:
    def __init__(self, x, y, image, scale=1.0):
        self.x = x
        self.y = y
        self.path = image
        # 1. Load the raw image
        base_image = self._load_image(image)
        # 2. Calculate scaled dimensions
        new_width = int(base_image.get_width() * scale)
        new_height = int(base_image.get_height() * scale)
        # 3. Scale the image immediately
        self.image = pygame.transform.scale(base_image, (new_width, new_height))
        self.width = new_width
        self.height = new_height

    def _load_image(self, path):
        """Loads an image using Pillow and converts it to a Pygame Surface."""
        try:
            img = Image.open(path)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            mode = img.mode
            size = img.size
            data = img.tobytes()
            
            return pygame.image.fromstring(data, size, mode)
        except Exception as e:
            print(f"[PGX Error] Could not load image '{path}': {e}")
            # Fallback: Return a red square
            surf = pygame.Surface((50, 50))
            surf.fill((255, 0, 0))
            return surf

    def draw(self, surface):
        """Draws the sprite centered at (self.x, self.y)."""
        rect = self.image.get_rect(center=(self.x, self.y))
        surface.blit(self.image, rect)

    def flip_h(self):
        """ Flips the sprite Horizontally (Left <-> Right). """
        self.image = pygame.transform.flip(self.image, True, False)

    def flip_v(self):
        """ Flips the sprite Vertically (Upside Down). """
        self.image = pygame.transform.flip(self.image, False, True)


class Group:
    """
    A container for managing multiple sprites together.
    """
    def __init__(self, *sprites):
        """ Accepts any number of sprite objects to add immediately. """
        self.sprites = list(sprites)

    def add(self, *sprites):
        """ Adds a sprite (or many) to the group. """
        self.sprites.extend(sprites)

    def remove(self, sprite):
        """ Removes a sprite from the group. """
        if sprite in self.sprites:
            self.sprites.remove(sprite)

    def draw(self, surface):
        """ Draws all sprites in the group to the surface. """
        for sprite in self.sprites:
            sprite.draw(surface)


__all__ = ['Sprite', 'Group']
        
