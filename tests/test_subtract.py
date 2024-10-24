import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.commands.subtract import subtract


def test_subtract():
    assert subtract(10, 5) == 5
