# app/commands/multiply.py

from app.commands.command import Command

class Multiply(Command):
    def execute(self, x, y):
        return x * y
def multiply(x, y):
    return x * y
