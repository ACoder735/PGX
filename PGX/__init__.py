""" The PGX (Picture GraphiX) library.
    Made for making games simply
    It is designed to be begginer-freindly
    It is bulit on top of pygame, and may not be available on the latest python versions.
    (3.14+ in 2025.)
"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

# Window and Text and others
from PGX.window import Window
from PGX.text import Text
from PGX.camera import Camera
from PGX.spritesheet import SpriteSheet

# Requeried submoudles
import PGX.color as Color
import PGX.Pen
import PGX.Sprite
import PGX.Events as Event
import PGX.Sound
import PGX.Timer
import PGX.Player
import PGX.UI
import PGX.Scenes

# Initalize pygame
pygame.init()





__version__ = '1.0.0'

__all__ = ['Window', 'Color', 'Pen', 'Sprite', 'Event', 'Text', 'Sound', 'Timer', 'Player', 'UI', 'Camera', 'SpriteSheet', 'Scenes']



