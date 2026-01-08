def collideRect(obj1, obj2):
    """
    Returns True if obj1 and obj2 are touching.
    Objects must have x, y, width, and height attributes.
    """
    l1 = obj1.x - (obj1.width / 2)
    r1 = obj1.x + (obj1.width / 2)
    t1 = obj1.y - (obj1.height / 2)
    b1 = obj1.y + (obj1.height / 2)

    l2 = obj2.x - (obj2.width / 2)
    r2 = obj2.x + (obj2.width / 2)
    t2 = obj2.y - (obj2.height / 2)
    b2 = obj2.y + (obj2.height / 2)

    return (l1 < r2 and r1 > l2 and t1 < b2 and b1 > t2)

def collideCircle(obj1, obj2):
    """
    Returns True if obj1 and obj2 are touching (Distance-based).
    Works great for circles, balls, or coins.
    """
    # Calculate distance between centers
    dx = obj1.x - obj2.x
    dy = obj1.y - obj2.y
    distance = (dx**2 + dy**2)**0.5
    
    # Sum of radii (Assume width is diameter)
    r1 = obj1.width / 2
    r2 = obj2.width / 2
    
    return distance < (r1 + r2)

def collidePoint(obj, px, py):
    """
    Returns True if the Point (px, py) is inside the object.
    Perfect for checking if the Mouse is hovering over an object.
    """
    half_w = obj.width / 2
    half_h = obj.height / 2
    
    return (px > obj.x - half_w and 
            px < obj.x + half_w and 
            py > obj.y - half_h and 
            py < obj.y + half_h)

def collideScreen(obj, win_obj):
    """
    Checks if the object is hitting the screen edge.
    Returns 'top', 'bottom', 'left', 'right' or None.
    Useful for bouncing balls or keeping players inside.
    """
    w = win_obj.size[0]
    h = win_obj.size[1]
    half_w = obj.width / 2
    half_h = obj.height / 2
    
    if obj.y - half_h < 0: return 'top'
    if obj.y + half_h > h: return 'bottom'
    if obj.x - half_w < 0: return 'left'
    if obj.x + half_w > w: return 'right'
    
    return None







__all__ = ['collideRect', 'collideCircle', 'collidePoint', 'collideScreen']




