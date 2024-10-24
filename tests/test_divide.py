import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.commands.divide import divide
from app.commands.divide import Divide


def test_divide_by_zero():
    divide_command = Divide()
    with pytest.raises(ValueError) as excinfo:
        divide_command.execute(10, 0)

    assert str(excinfo.value) == "Cannot divide by zero."


def test_divide():

    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-6, 2) == -3
    assert divide(0, 1) == 0

    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert str(excinfo.value) == "Cannot divide by zero."
