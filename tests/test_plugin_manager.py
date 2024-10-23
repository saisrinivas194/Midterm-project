import sys
import os

# Add the parent directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.plugin_manager import PluginManager  # Importing the PluginManager

def test_plugin_manager():
    # Add your tests for the plugin manager here
    pass
