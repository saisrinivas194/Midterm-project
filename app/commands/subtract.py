# app/commands/subtract.py

from app.commands.command import Command

class Subtract(Command):
    def execute(self, x, y):
        return x - y
def subtract(x, y):
    return x - y
