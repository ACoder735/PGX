import pygame
from PIL import Image

class Sprite:
    """ A PGX sprite (Image object). """
    def __init__(self, x, y, image, scale=1.0):
        self.x = x
        self.y = y
        self.path = image
        
        # ADD THIS: Track facing direction (1 = Right, -1 = Left)
        self.direction = 1 
        
        try:
            img = Image.open(image)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            mode = img.mode
            size = img.size
            data = img.tobytes()
            
            base_image = pygame.image.fromstring(data, size, mode)
        except Exception as e:
            print(f"[PGX Error] Could not load image '{image}': {e}")
            base_image = pygame.Surface((50, 50))
            base_image.fill((255, 0, 0))
            
        # Scale image
        new_width = int(base_image.get_width() * scale)
        new_height = int(base_image.get_height() * scale)
        self.image = pygame.transform.scale(base_image, (new_width, new_height))
        
        self.width = new_width
        self.height = new_height

    def draw(self, surface):
        rect = self.image.get_rect(center=(self.x, self.y))
        surface.blit(self.image, rect)

    def flip_h(self):
        """ Flips sprite Horizontally (Left <-> Right). """
        self.image = pygame.transform.flip(self.image, True, False)
        # Also update internal direction tracker (Optional but good for debugging)
        self.direction *= -1

    def flip_v(self):
        """ Flips sprite Vertically (Upside Down). """
        self.image = pygame.transform.flip(self.image, False, True)
