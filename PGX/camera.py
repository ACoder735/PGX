import pygame

class Camera:
    """ 
    A camera that scrolls the screen to follow an object.
    """
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.target = None
        # Smooth movement (Lerp)
        self.smooth_speed = 0.1

    def follow(self, target_obj):
        """ Makes the camera stick to an object (e.g., player). """
        self.target = target_obj

    def update(self):
        """ 
        Call this to update camera position. 
        If following a target, it centers it on screen.
        """
        if self.target:
            # Lerp (Linear Interpolation) for smoothness
            target_x = self.target.x - (self.width // 2)
            target_y = self.target.y - (self.height // 2)
            
            self.x += (target_x - self.x) * self.smooth_speed
            self.y += (target_y - self.y) * self.smooth_speed

    def clamp(self, map_w, map_h):
        """
        Stops the camera from showing empty space outside the map.
        """
        # Don't let X go below 0 or above map_w
        self.x = max(0, min(self.x, map_w - self.width))
        
        # Don't let Y go below 0 or above map_h
        self.y = max(0, min(self.y, map_h - self.height))
        
    def apply(self, x, y):
        """
        Use this helper when drawing.
        It converts World Coordinates to Screen Coordinates.
        
        Usage:
            rect.x = PGX.camera.apply(rect.x, rect.y)[0]
        """
        return (x - self.x, y - self.y)






    
