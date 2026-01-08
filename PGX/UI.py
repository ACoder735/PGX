import pygame
import PGX

class Button:
    """ 
    A clickable UI element with hover effects.
    
    Args:
        x, y (int): The CENTER position of the button.
        width, height (int): The size of the button.
        text (str): The text label.
        callback (function): The function to run when clicked.
        bg_color (tuple): Normal background color.
        hover_color (tuple): Background color when mouse is over it.
        text_color (tuple): Color of the text.
        font_size (int): Size of the font.
        font_name (str): Name of the font family.
    """
    def __init__(self, x, y, width, height, text, callback, 
                 bg_color=(100, 100, 100), hover_color=(150, 150, 150), 
                 text_color=(255, 255, 255), font_size=20, font_name="Arial"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.callback = callback
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.current_color = bg_color
        
        # Create text centered on the button
        # Args: text, x, y, size, font_name, color
        self.text_obj = PGX.Text(text, self.x, self.y, font_size, font_name, text_color)

    def update(self, screen):
        """ 
        Checks mouse hover and click states, then draws.
        
        Args:
            screen: The surface to draw on.
        """
        mx = PGX.Event.mousex
        my = PGX.Event.mousey
        
        # Calculate edges based on Center Anchoring
        half_w = self.width // 2
        half_h = self.height // 2
        left = self.x - half_w
        right = self.x + half_w
        top = self.y - half_h
        bottom = self.y + half_h
        
        # Check Collision
        if left < mx < right and top < my < bottom:
            self.current_color = self.hover_color
            if pygame.mouse.get_pressed()[0]: # Left Click
                self.callback()
        else:
            self.current_color = self.bg_color
            
        self.draw(screen)

    def draw(self, screen):
        """ Draws the button background and text. """
        left = self.x - (self.width // 2)
        top = self.y - (self.height // 2)
        rect_obj = pygame.Rect(left, top, self.width, self.height)
        pygame.draw.rect(screen, self.current_color, rect_obj)
        self.text_obj.draw(screen)

class Bar:
    """ 
    A progress bar (Health, Stamina, etc.).
    
    Args:
        x, y (int): The CENTER position of the bar.
        width, height (int): Dimensions.
        max_value (int): The value representing 100% full.
        current_value (int): The current fill amount.
        bg_color (tuple): Background color of empty bar.
        fill_color (tuple): Color of the filled portion.
    """
    def __init__(self, x, y, width, height, max_value=100, current_value=100, 
                 bg_color=(50, 50, 50), fill_color=(255, 255, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = current_value
        self.bg_color = bg_color
        self.fill_color = fill_color

    def set_value(self, value):
        """ 
        Updates the bar fill amount. 
        Automatically clamps between 0 and max_value.
        
        Args:
            value (int): The new value.
        """
        self.current_value = value
        if self.current_value > self.max_value: 
            self.current_value = self.max_value
        if self.current_value < 0:
            self.current_value = 0

    def draw(self, screen):
        """ Draws the empty background and the filled portion. """
        left = self.x - (self.width // 2)
        top = self.y - (self.height // 2)
        rect_obj = pygame.Rect(left, top, self.width, self.height)
        
        # Draw Background
        pygame.draw.rect(screen, self.bg_color, rect_obj)
        
        # Calculate Fill Width
        if self.max_value > 0:
            ratio = self.current_value / self.max_value
        else:
            ratio = 0
        fill_width = self.width * ratio
        
        # Draw Fill
        if fill_width > 0:
            fill_rect = pygame.Rect(left, top, fill_width, self.height)
            pygame.draw.rect(screen, self.fill_color, fill_rect)

class Panel:
    """ 
    A decorative rectangular box (Window/Background).
    
    Args:
        x, y (int): The CENTER position of the panel.
        width, height (int): Dimensions.
        color (tuple): The fill color.
        thickness (int): Border thickness (0 = no border).
        border_color (tuple): The color of the border.
    """
    def __init__(self, x, y, width, height, color=(50, 50, 50), thickness=0, border_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.thickness = thickness
        self.border_color = border_color

    def draw(self, screen):
        """ Draws the panel and its border. """
        left = self.x - (self.width // 2)
        top = self.y - (self.height // 2)
        rect_obj = pygame.Rect(left, top, self.width, self.height)
        
        # Draw Fill
        pygame.draw.rect(screen, self.color, rect_obj)
        
        # Draw Border
        if self.thickness > 0:
            pygame.draw.rect(screen, self.border_color, rect_obj, self.thickness)

__all__ = ['Button', 'Bar', 'Panel']
