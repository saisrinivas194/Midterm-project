import importlib.util
import os
import sys
from app.plugins.plugin import Plugin
import logging


class PluginManager:
    def __init__(self, plugins_dir):
        self.plugins_dir = plugins_dir
        self.plugins = []

    def load_plugins(self):
        for filename in os.listdir(self.plugins_dir):
            if filename.endswith("_plugin.py"):
                module_name = filename[:-3]
                module_path = os.path.join(self.plugins_dir, filename)

                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                for name in dir(module):
                    obj = getattr(module, name)
                    if (
                        isinstance(obj, type)
                        and issubclass(obj, Plugin)
                        and obj is not Plugin
                    ):
                        self.plugins.append(obj())

    def run_plugins(self):
        outputs = []
        for plugin in self.plugins:
            outputs.append(plugin.run())
        return outputs
