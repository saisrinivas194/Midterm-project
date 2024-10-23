import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.commands.divide import divide  # Importing the divide function

def test_divide():
    assert divide(10, 2) == 5
