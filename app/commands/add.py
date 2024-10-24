# app/commands/add.py

from app.commands.command import Command 

class Add(Command):
    def execute(self, x, y):
        return x + y

def add(x, y):
    return x + y
