import unittest
from app.calculator import add, subtract, multiply, divide

# --- PyTest Tests (Works with `pytest`) ---
def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(6, 7) == 42

def test_divide():
    assert divide(20, 5) == 4.0

def test_divide_by_zero():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."

# --- PyUnit (unittest) Tests (Works with `python -m unittest`) ---
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 6), 4)

if __name__ == "__main__":
    unittest.main()

