import pygame
import os

# Initialize mixer once
pygame.mixer.init()

class Sound:
    """ Handles short sound effects (Jump, Shoot, etc.) """
    def __init__(self, path):
        self.path = path
        try:
            self.sound = pygame.mixer.Sound(path)
        except Exception as e:
            print(f"[PGX Error] Could not load sound '{path}': {e}")
            self.sound = None

    def play(self):
        """ Plays the sound once. """
        if self.sound:
            self.sound.play()

    def stop(self):
        """ Stops the sound if it is playing. """
        if self.sound:
            self.sound.stop()

class Music:
    """ Handles background music (long loops). """
    
    @staticmethod
    def play(path, loops=-1):
        """
        Plays background music.
        loops=-1 means loop forever.
        """
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(loops)
        except Exception as e:
            print(f"[PGX Error] Could not play music '{path}': {e}")

    @staticmethod
    def stop():
        """ Stops the music. """
        pygame.mixer.music.stop()
        
    @staticmethod
    def pause():
        """ Pauses the music. """
        pygame.mixer.music.pause()
        
    @staticmethod
    def unpause():
        """ Resumes the music. """
        pygame.mixer.music.unpause()
        
    @staticmethod
    def volume(val):
        """
        Sets volume. 
        val should be between 0.0 (silent) and 1.0 (max).
        """
        pygame.mixer.music.set_volume(val)





__all__ = ['Sound', 'Music']


        
