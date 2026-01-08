import pygame
import PGX.Events.keys as key
import PGX.Events.joy as joy

_down_handlers = []
_up_handlers = []
_mouse_down_handlers = []
_mouse_up_handlers = [] 

def onkey(key, function):
    """
    Binds a function to run when a specific key is pressed down.
    Usage: PGX.Events.onkey(PGX.Events.key.space, my_jump_function)
    """
    _down_handlers.append((key, function))

def onrelease(key, function):
    """
    Binds a function to run when a specific key is released.
    Usage: PGX.Events.onrelease(PGX.Events.key.space, my_shoot_function)
    """
    _up_handlers.append((key, function))

def is_pressed(key):
    """
    Returns True if the specific key is currently held down.
    Usage: PGX.Events.is_pressed(PGX.Events.key.up)
    """
    keys = pygame.key.get_pressed()
    return keys[key]



def onmousedown(button, function):
    """ 
    Binds a function to run when a specific mouse button is clicked.
    Button IDs: Use mouseleft, mouseright, mousemid, mouseScrollUp and mouseScrollDown
    """
    _mouse_down_handlers.append((button, function))

def onmouseup(button, function):
    """ Binds a function to run when a mouse button is released. """
    _mouse_up_handlers.append((button, function))

mouseleft = 1
mousemid = 2
mouseright = 3

mousex = 0
mousey = 0

def ismousevisible():
    pygame.mouse.get_visible()


__all__ = ['onkey', 'onrelease', 'key', 'is_pressed', 'onmousedown', 'onmouseup', 'mouseleft', 'mouseright', 'mousemid', 'mousex', 'mousey', 'joy']





