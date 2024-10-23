import importlib
import os
from app.plugins.plugin import Plugin  # Add this import statement
import logging
import logging.config  # Ensure this line is present

class PluginManager:
    def __init__(self, plugins_dir):
        self.plugins_dir = plugins_dir
        self.plugins = []

    def load_plugins(self):
        for filename in os.listdir(self.plugins_dir):
            if filename.endswith("_plugin.py"):
                module_name = filename[:-3]  # Remove .py
                module_path = f"{self.plugins_dir.replace('/', '.')}.{module_name}"
                module = importlib.import_module(module_path)
                # Look for the class that inherits from Plugin
                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, Plugin) and obj is not Plugin:
                        self.plugins.append(obj())

    def run_plugins(self):
        for plugin in self.plugins:
            plugin.run()
import logging
import configparser

# Load the logging configuration
config = configparser.ConfigParser()
config.read('logging.conf')
logging.config.fileConfig(config)

# Create a logger
logger = logging.getLogger(__name__)
