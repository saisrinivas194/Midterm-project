import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.commands.multiply import multiply


def test_multiply():
    assert multiply(3, 5) == 15
