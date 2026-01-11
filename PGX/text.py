import pygame

class Text:
    def __init__(self, text, x, y, size=20, font_name="Arial", color=(0, 0, 0)):
        self.text = str(text)
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.font_name = font_name 
        
        # Load the system font
        try:
            self.font = pygame.font.SysFont(self.font_name, self.size)
        except:
            self.font = pygame.font.SysFont(None, self.size)
            print('[PGX Error] Font '+str(font_name)+' was not found.')

        self._render()

    def _render(self):
        """ Internal method to update the surface image. """
        self.surface = self.font.render(self.text, True, self.color)

    def draw(self, surface):
        """ Draws the text centered at (self.x, self.y). """
        width = self.surface.get_width()
        height = self.surface.get_height()
        left = self.x - (width // 2)
        top = self.y - (height // 2)
        surface.blit(self.surface, (left, top))

    def set_text(self, new_text):
        """ Updates the text string. """
        self.text = str(new_text)
        self._render()

    def set_color(self, color):
        """ Updates the text color. """
        self.color = color
        self._render() 

    def set_size(self, size):
        """ Updates the font size. """
        self.size = size
        try:
            self.font = pygame.font.SysFont(self.font_name, self.size)
        except:
            self.font = pygame.font.SysFont(None, self.size)
        self._render()
            
    def set_font(self, font_name):
        """ Updates the font family. """
        self.font_name = font_name
        try:
            self.font = pygame.font.SysFont(self.font_name, self.size)
        except:
            self.font = pygame.font.SysFont(None, self.size)
            print('[PGX Error] Font '+str(font_name)+' was not found.')
        self._render()




