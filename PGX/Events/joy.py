import pygame

class Joy:
    """ 
    Handles Gamepad/Controller input. 
    """
    # --- CONSTANTS (Accessible via joy.A, joy.X, etc.) ---
    # Xbox/PlayStation Layout
    A = 0
    B = 1
    X = 2
    Y = 3
    Cross = 0
    Circle = 1
    Square = 2
    Triangle = 3
    # Bumpers (Standard Buttons)
    LB = 4
    RB = 5    
    # Triggers (Mapped to Axes on your controller)
    L2 = 4 
    R2 = 5
    # Left stick
    LS_X = 0
    LS_Y = 1
    # Right Stick
    RS_X = 2
    RS_Y = 3
    # Standard Names
    R1 = 5
    L1 = 4
    # Menu
    Back = 6
    Select = 6
    Share = 6 
    Start = 7
    Menu = 7
    Options = 7
    # Stick Clicks
    LeftStickClick = 8
    RightStickClick = 9

    def __init__(self, index=0):
        self.index = index
        self._joy = None
        self.num_axes = 0
        self.num_buttons = 0
        self.num_hats = 0
        
        pygame.joystick.init()
        
        if pygame.joystick.get_count() > index:
            self._joy = pygame.joystick.Joystick(index)
            self._joy.init()
            self.num_axes = self._joy.get_numaxes()
            self.num_buttons = self._joy.get_numbuttons()
            self.num_hats = self._joy.get_numhats()
            print(f"[PGX] Controller {index} detected: {self._joy.get_name()}")
        else:
            print(f"[PGX] No controller {index} detected.")

    def connected(self):
        return self._joy is not None

    def button(self, button_index):
        if self._joy:
            if button_index < self.num_buttons:
                return self._joy.get_button(button_index)
        return False

    def axis(self, axis_index):
        if self._joy:
            if axis_index < self.num_axes:
                return self._joy.get_axis(axis_index)
        return 0.0
    
    def dpad(self, hat_index=0):
        if self._joy:
            if hat_index < self.num_hats:
                return self._joy.get_hat(hat_index)
        return (0, 0)

__all__ = ['Joy']
