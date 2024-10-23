# app/plugins/greet/greet_plugin.py

from app.plugins.plugin import Plugin

class GreetPlugin(Plugin):
    def run(self, *args):
        print("Hello, welcome to the Advanced Python Calculator!")
