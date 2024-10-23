import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.repl import repl  # Importing the REPL function

def test_repl():
    # Add your tests for the REPL here
    pass
