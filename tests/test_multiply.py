import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.commands.multiply import multiply  # Importing the multiply function

def test_multiply():
    assert multiply(3, 5) == 15
