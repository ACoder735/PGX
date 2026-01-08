""" PGX.pen - Shapes that keep a reference and are anchored to the center. """

import pygame
import math

class Shape:
    def __init__(self, x, y, color=(0,0,0), thickness=0):
        self.x = x
        self.y = y
        self.color = color
        self.thickness = thickness 

    def draw(self, surface):
        pass

class rect(Shape):
    def __init__(self, x, y, width, height=None, color=(0,0,0), thickness=0):
        super().__init__(x, y, color, thickness)
        self.width = width
        self.height = height if height is not None else width

    def draw(self, surface):
        left = self.x - (self.width // 2)
        top = self.y - (self.height // 2)
        rect_obj = pygame.Rect(left, top, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect_obj, self.thickness)
        

class circle(Shape):
    def __init__(self, x, y, radius, radius_y=None, color=(0,0,0), thickness=0):
        super().__init__(x, y, color, thickness)
        self.radius = radius
        self.radius_y = radius_y

    def draw(self, surface):
        ry = self.radius_y if self.radius_y else self.radius
        left = self.x - self.radius
        top = self.y - ry
        bounding_rect = pygame.Rect(left, top, self.radius * 2, ry * 2)
        pygame.draw.ellipse(surface, self.color, bounding_rect, self.thickness)
        

class arc(Shape):
    """
    Draws an arc (part of a circle or ellipse).
    Angles are in degrees (0 is East, goes counter-clockwise).
    """
    def __init__(self, x, y, radius, start_angle, stop_angle, radius_y=None, color=(0,0,0), width=1):
        super().__init__(x, y, color, thickness=width)
        
        self.radius = radius
        self.radius_y = radius_y if radius_y else radius
        
        # Convert degrees to radians for Pygame
        self.start_angle = math.radians(start_angle)
        self.stop_angle = math.radians(stop_angle)

    def draw(self, surface):
        ry = self.radius_y if self.radius_y else self.radius
        
        left = self.x - self.radius
        top = self.y - ry
        w = self.radius * 2
        h = ry * 2
        
        rect_obj = pygame.Rect(left, top, w, h)
        pygame.draw.arc(surface, self.color, rect_obj, self.start_angle, self.stop_angle, self.thickness)
        

class poly(Shape):
    def __init__(self, x, y, points, color=(0,0,0), thickness=0):
        super().__init__(x, y, color, thickness)
        self.points = points

    def draw(self, surface):
        shifted_points = []
        for px, py in self.points:
            shifted_points.append((px + self.x, py + self.y))
        pygame.draw.polygon(surface, self.color, shifted_points, self.thickness)
        

class line(Shape):
    def __init__(self, x, y, end_x, end_y, color=(0,0,0), thickness=1):
        super().__init__(x, y, color, thickness=thickness)
        self.end_x = end_x
        self.end_y = end_y

    def draw(self, surface):
        pygame.draw.line(surface, self.color, (self.x, self.y), (self.end_x, self.end_y), self.thickness)


class lines(Shape):
    """
    Draws a series of connected lines (polyline).
    Unlike Polygon, this does NOT close the loop back to the start.
    """
    def __init__(self, points, color=(255, 255, 255), thickness=1):
        # We pass 0, 0 for x,y because the points are absolute coordinates
        super().__init__(0, 0, color, thickness=thickness)
        self.points = points

    def draw(self, surface):
        # Only draw if we have at least 2 points to connect
        if len(self.points) > 1:
            pygame.draw.lines(surface, self.color, False, self.points, self.thickness)


            

__all__ = ['rect', 'line', 'circle', 'arc', 'poly', 'lines']
        


