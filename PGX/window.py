import pygame
from PIL import Image
import PGX.color as color
import PGX.Events as Event
import os

class Window:
    """ A PGX window for creating games."""
    def __init__(self, width, height, fullscr=False):
        self.running = True
        self.event_queue = {}
        self.size = (width, height)
        self.fullscr = fullscr
        self.bg_color = color.WHITE
        self.locked = False

        lib_path = os.path.dirname(__file__)
        icon_path = os.path.join(lib_path, "Icon.png")
        if os.path.exists(icon_path):
            self.icon(icon_path)
        
        # CHANGED: Add DOUBLEBUF and HWSURFACE flags to prevent flickering
        flags = pygame.DOUBLEBUF | pygame.HWSURFACE
        if self.fullscr:
            flags |= pygame.FULLSCREEN
        if not self.locked and not self.fullscr:
            flags |= pygame.RESIZABLE
            
        self.screen = pygame.display.set_mode(self.size, flags)
        pygame.display.set_caption('PGX Window  (Ver. 1.0.0)')
        self.clock = pygame.time.Clock()
        
    def title(self, newTitle):
        """ Sets the title of the window. """
        pygame.display.set_caption(newTitle)

    def end(self):
        """ Stops the game loop and closes the window. """
        # Do the functions binded by PGX.Event.onquit(), then close the window.
        for func in Event._quit_handlers:
            func() 
        self.running = False

    def center(self):
        return (self.size[0]/2, self.size[1]/2)

    def toggle_fullscr(self):
        """ Toggles the fullscreen. """
        self.fullscr = not self.fullscr
        
        # CHANGED: Include buffering flags here too
        flags = pygame.DOUBLEBUF | pygame.HWSURFACE
        if self.fullscr:
            flags |= pygame.FULLSCREEN
        elif not self.locked:
            flags |= pygame.RESIZABLE
            
        self.screen = pygame.display.set_mode(self.size, flags)

    def set_mouse_vis(self, visible=True):
        """ Shows or hides the mouse cursor. """
        pygame.mouse.set_visible(visible)

    def lock(self, lock=True):
        """ Determine the window's resizablitiy. """
        self.locked = lock
        
        if self.fullscr:
            return 
        flags = pygame.DOUBLEBUF | pygame.HWSURFACE
        if not self.locked:
            flags |= pygame.RESIZABLE

        self.screen = pygame.display.set_mode(self.size, flags)

    def fill(self, color_val):
        """Changes the background color."""
        self.bg_color = color_val

    def icon(self, path):
        """ 
        Sets the window icon. 
        Pass the path to a small PNG file.
        """
        try:
            # 1. Open with Pillow
            img = Image.open(path)
            
            # 2. Ensure transparency (RGBA)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
                
            # 3. Convert to Pygame Surface
            mode = img.mode
            size = img.size
            data = img.tobytes()
            
            image_surf = pygame.image.fromstring(data, size, mode)
            
            # 4. Set the icon
            pygame.display.set_icon(image_surf)
        except Exception as e:
            print(f"[PGX Error] Could not set icon '{path}': {e}")

    def run(self, loop_function=None):
        """ Runs the game. """
        self.running = True
        while self.running:
            # --- UPDATE MOUSE POSITIONS ----
            mx, my = pygame.mouse.get_pos()
            Event.mousex = mx
            Event.mousey = my
            for event in pygame.event.get():
                # --- QUIT (Default PGX Behavior) ---
                if event.type == pygame.QUIT:
                    # Do the functions binded by PGX.Event.onquit(), then close the window.
                    for func in Event._quit_handlers:
                        func() 
                    self.running = False
                # --- KEYBOARD EVENTS ---
                if event.type == pygame.KEYDOWN:
                    for key_code, func in Event._down_handlers:
                        if event.key == key_code:
                            func()          
                if event.type == pygame.KEYUP:
                    for key_code, func in Event._up_handlers:
                        if event.key == key_code:
                            func()
                # --- MOUSE EVENTS ---
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for btn_code, func in Event._mouse_down_handlers:
                        if event.button == btn_code:
                            func()          
                if event.type == pygame.MOUSEBUTTONUP:
                    for btn_code, func in Event._mouse_up_handlers:
                        if event.button == btn_code:
                            func()
                # --- RESIZE EVENTS ---
                if not self.locked and event.type == pygame.VIDEORESIZE:
                    self.size = event.size
                # --- USER QUEUE ---
                if event.type in self.event_queue:
                    self.event_queue[event.type]()

            self.screen.fill(self.bg_color)
            
            if loop_function:
                loop_function(self.screen)
                
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()




