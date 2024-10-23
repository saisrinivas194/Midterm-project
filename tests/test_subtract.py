import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.commands.subtract import subtract  # Importing the subtract function

def test_subtract():
    assert subtract(10, 5) == 5
