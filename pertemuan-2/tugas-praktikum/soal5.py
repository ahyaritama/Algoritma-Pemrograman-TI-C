import math

def jarak(x1, y1, x2, y2):
    if (
        type(x1) not in (int, float)
        or type(y1) not in (int, float)
        or type(x2) not in (int, float)
        or type(y2) not in (int, float)
    ):
        return
    
    x = math.pow(x2 - x1, 2)
    y = math.pow(y2 - y1, 2)
    return math.sqrt(x + y)