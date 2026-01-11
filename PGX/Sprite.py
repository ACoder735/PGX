import pygame
from PIL import Image

class Sprite:
    def __init__(self, x, y, image, scale=1.0):
        self.x = x
        self.y = y
        self.path = image
        
        try:
            img = Image.open(image)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            mode = img.mode
            size = img.size
            data = img.tobytes()
            
            self.image = pygame.image.fromstring(data, size, mode)
        except Exception as e:
            print(f"[PGX Error] Could not load image '{image}': {e}")
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))
        
        self.width = int(self.image.get_width() * scale)
        self.height = int(self.image.get_height() * scale)
        
        if scale != 1.0:
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, surface):
        rect = self.image.get_rect(center=(self.x, self.y))
        surface.blit(self.image, rect)

    def flip_h(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def flip_v(self):
        self.image = pygame.transform.flip(self.image, False, True)

class Group:
    def __init__(self, *sprites):
        self.sprites = list(sprites)

    def add(self, *sprites):
        self.sprites.extend(sprites)

    def remove(self, sprite):
        if sprite in self.sprites:
            self.sprites.remove(sprite)

    def draw(self, surface):
        for sprite in self.sprites:
            sprite.draw(surface)



__all__ = ['Sprite', 'Group']
            
