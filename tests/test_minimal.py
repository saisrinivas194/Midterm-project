# tests/test_minimal.py

from app.commands.divide import divide
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(1, 0)
    assert str(excinfo.value) == "Cannot divide by zero."
