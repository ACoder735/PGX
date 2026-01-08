_scenes = {}
_current_scene = None

def add(name, func):
    """ 
    Adds a scene (scene function) to the manager.
    
    Usage:
        def my_menu(screen): ...
        PGX.Scenes.add("menu", my_menu)
    """
    global _scenes
    _scenes[name] = func

def set(name):
    """ 
    Switches the active scene to 'name'.
    
    Usage:
        PGX.Scenes.set("game")
    """
    global _current_scene
    
    if name in _scenes:
        _current_scene = _scenes[name]
    else:
        print(f"[PGX.Scenes] Error: Scene '{name}' does not exist.")

def get(screen):
    """ 
    Returns the current active scene function.
    You pass this to win.run().
    
    Usage:
        win.run(PGX.Scenes.get)
    """
    global _current_scene
    
    if _current_scene:
        _current_scene(screen)
    else:
        print("[PGX.Scenes] Warning: No scene set! Did you forget PGX.Scenes.set('menu')?")


__all__ = ['add', 'set', 'get']

