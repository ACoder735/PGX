import pygame

class SpriteSheet:
    """ 
    Handles an animation strip (SpriteSheet).
    
    Args:
        x, y: Position (Center Anchored).
        path: Path to your .png sheet.
        frame_w: Width of ONE frame in pixels.
        frame_h: Height of ONE frame in pixels.
        scale: How much to zoom in (1.0 = normal).
        fps: How fast it plays (Higher = faster).
    """
    def __init__(self, x, y, path, frame_w, frame_h, scale=1.0, fps=10):
        self.x = x
        self.y = y
        # Calculate scaled size
        self.width = int(frame_w * scale)
        self.height = int(frame_h * scale)
        # Load the full strip
        try:
            self.full_image = pygame.image.load(path).convert_alpha()
        except:
            # Fallback red box if image fails
            self.full_image = pygame.Surface((50, 50))
            self.full_image.fill((255, 0, 0))
        # Slice image into frames
        self.frames = []
        # Number of frames = Total Width / Frame Width
        num_frames = self.full_image.get_width() // int(frame_w)
        
        for i in range(num_frames):
            # Calculate where this frame is in the big image
            rect = pygame.Rect(i * int(frame_w), 0, int(frame_w), int(frame_h))
            # Cut it out (Subsurface)
            frame_surf = self.full_image.subsurface(rect).copy()
            # Scale it
            if scale != 1.0:
                frame_surf = pygame.transform.scale(frame_surf, (self.width, self.height))
            self.frames.append(frame_surf)
        # Animation timing
        self.current_frame = 0
        self.fps = fps
        self.delay = 1000 // fps # Milliseconds per frame
        self.last_update = 0
        self.animating = True

    def set_anim(self, state):
        """ 
        True to animate, False to pause on current frame. 
        """
        self.animating = state

    def update(self):
        """ 
        Call this in your draw loop to advance frames. 
        """
        if self.animating:
            now = pygame.time.get_ticks()
            if now - self.last_update > self.delay:
                self.current_frame += 1
                if self.current_frame >= len(self.frames):
                    self.current_frame = 0 # Loop back to start
                self.last_update = now

    def draw(self, surface):
        """ 
        Draws the current frame at (x, y).
        Uses Center Anchoring.
        """
        rect = self.frames[self.current_frame].get_rect(center=(self.x, self.y))
        surface.blit(self.frames[self.current_frame], rect)



        
