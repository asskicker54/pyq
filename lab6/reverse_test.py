import pytest

# Тестируемая функция
def reverse(s):
    if type(s) != str:
        raise TypeError(f'Expected str, got {type(s)}')

    return s[::-1]

def test_empty():
    assert reverse('') == ''
    
def test_any_s():
    assert reverse('q') == 'q'
    
def test_pal():
    assert reverse('мадам') == 'мадам'
    
def test_basic():
    assert reverse('qwe') == 'ewq'
    
def test_type():
    with pytest.raises(TypeError):
        reverse(4)
        
def test_iter():
    with pytest.raises(TypeError):
        reverse(['q'])