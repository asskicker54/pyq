import pytest

class Rectangle:
    
    def __init__(self, width, height):
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("Uncorrect value")
        
        if width <= 0 and height <= 0:
            raise ValueError("Values must be positive")
        self.width = width 
        self.height = height
        
    def get_area(self):
        return self.height * self.width
    
    def get_per(self):
        return 2 * (self.height + self.width)
    

def test_type():
    with pytest.raises(TypeError):
        Rectangle('q', 66)
        
def test_val():
    with pytest.raises(ValueError):
        Rectangle(-1, 0)
        
@pytest.fixture
def rect():
    return Rectangle(4, 3)

def test_area(rect: Rectangle):
    assert rect.get_area() == 12
    
def test_per(rect: Rectangle):
    assert rect.get_per() == 14
        