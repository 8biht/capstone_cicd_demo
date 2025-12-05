import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, subtract, multiply, divide, log, square, sin, cos, square_root, percentage

def test_add():
    assert add(5, 6) == 11

def test_add():
    assert add(5, 6) != 10 

def test_subtract():
    assert subtract(5, 6) == -1

def test_subtract():
    assert subtract(5, 6) != 10 

def test_multiply():
    assert multiply(2, 3) == 6

def test_multiply():
    assert multiply(2, 3) != 5

def test_divide():
    assert divide(4, 2) == 2

def test_divide():
    assert divide(4, 2) != 5

def test_log():
    assert log(math.e) == 1

def test_log():
    assert log(math.e) != 5

def test_square():
    assert square(5) == 25

def test_square():
    assert square(5) != 6

def test_sin():
    assert sin(math.pi) == 0

def test_sin():
    assert sin(math.pi) != 5

def test_cos():
    assert cos(math.pi) == -1

def test_cos():
    assert cos(math.pi) != 5

def test_square_root():
    assert square_root(25) == 5

def test_square_root():
    assert square_root(25) != 6

def test_square_root():
    assert square_root(-25) == None

def test_square_root():
    assert square_root(-25) != 5

def test_percentage():
    assert percentage(3, 4) == 75

def test_percentage():
    assert percentage(3, 4) != 55

def test_percentage():
    assert percentage(-3, 4) == None

def test_percentage():
    assert percentage(-3, 4) != 75
