import math

def roots(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        D = (b**2) - (4 * a * c)
        if D < 0:
            raise ValueError
        elif D == 0:
            x = -b / (2 * a)
            return (x, x)
        else: 
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return tuple(sorted([x1, x2]))
        
    except (ValueError, TypeError):
        return None

def test_type():
    assert roots('1', '2', '3') == None
    
def test_D_eq_null():
    assert roots(3, -18, 27) == (3, 3)
    
def test_norm():
    assert roots(1, 10, -24) == (-12, 2)
    
def test_no_solution():
    assert roots(2, 1, 5) == None
