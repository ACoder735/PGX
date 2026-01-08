import pygame

def get_time():
    """
    Returns the time (in milliseconds) since the game started.
    Useful for calculating delta time.
    """
    return pygame.time.get_ticks()

import pygame

def get_time():
    return pygame.time.get_ticks()

class Timer:
    """ 
    A timer that triggers a callback function every 'interval' seconds.
    """
    def __init__(self, interval, callback, loops=-1):
        self.interval = interval  # Seconds
        self.callback = callback  # Function to run
        self.loops = loops       # -1 = Forever, 1 = Run Once, 5 = Run 5 times
        self.active = True        # Is the timer running?
        
        self.start_time = pygame.time.get_ticks()

    def update(self):
        """ 
        Call this inside your update loop. 
        Returns True if the timer triggered.
        """
        if not self.active:
            return False 
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.interval * 1000:
            self.start_time = current_time
            self.callback() 
            if self.loops > 0:
                self.loops -= 1
                if self.loops == 0:
                    self.stop()
                    
            return True
        return False

    def stop(self):
        """ Pauses/Stops the timer. """
        self.active = False

    def start(self):
        """ Starts/Resumes the timer. """
        self.start_time = pygame.time.get_ticks()
        self.active = True


__all__ = ['get_time', 'Timer']
