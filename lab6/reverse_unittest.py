import unittest

# Тестируемая функция
def reverse(s):
    if type(s) != str:
        raise TypeError(f'Expected str, got {type(s)}')

    return s[::-1]

class ReverseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')
        
    def test_any_symbol(self):
        self.assertEqual(reverse('q'), 'q')
        
    def test_pal(self):
        self.assertEqual(reverse('мадам'), 'мадам')
        
    def test_basic(self):
        self.assertEqual(reverse("hello"), 'olleh')
        
    def test_type(self):
        with self.assertRaises(TypeError):
            reverse(42)
            
    def test_iter(self):
        with self.assertRaises(TypeError):
            reverse(['q', 'w', 'e'])
        

if __name__ == '__main__':
    unittest.main()

