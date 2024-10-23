from app.commands.command import Command

class Divide(Command):
    def execute(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

def divide(x, y):  # Ensure this function is defined correctly
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
