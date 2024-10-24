import os
from pathlib import Path
import pytest
from unittest.mock import patch
from app.plugin_manager import PluginManager 
from app.plugins.greet.greet_plugin import GreetPlugin
from app.plugins.plugin import Plugin

def test_plugin_run_not_implemented():
    plugin = Plugin()  
    with pytest.raises(NotImplementedError) as excinfo:
        plugin.run() 
    
    assert str(excinfo.value) == "Plugins must implement the 'run' method."
def test_greet_plugin_run():
    plugin = GreetPlugin()

    with patch('builtins.print') as mock_print:
        plugin.run()
        mock_print.assert_called_once_with("Hello, welcome to the Advanced Python Calculator!")

@pytest.fixture
def setup_plugins(tmp_path: Path):
    plugins_dir = tmp_path / "plugins"
    plugins_dir.mkdir()

    valid_plugin = plugins_dir / "valid_plugin.py"
    valid_plugin.write_text("""
from app.plugins.plugin import Plugin

class ValidPlugin(Plugin):
    def run(self):
        return "Hello from valid plugin!"
""")

    bad_plugin = plugins_dir / "bad_plugin.py"
    bad_plugin.write_text("""
# This is a bad plugin
""")

    return str(plugins_dir)

def test_load_plugins(setup_plugins: str):
    plugin_manager = PluginManager(setup_plugins)
    plugin_manager.load_plugins()
    assert len(plugin_manager.plugins) == 1  
    assert "ValidPlugin" in [type(p).__name__ for p in plugin_manager.plugins]

def test_run_plugins(setup_plugins: str):
    plugin_manager = PluginManager(setup_plugins)
    plugin_manager.load_plugins()
    output = plugin_manager.run_plugins()
    assert "Hello from valid plugin!" in output

def test_bad_plugin_handling(setup_plugins: str):
    plugin_manager = PluginManager(setup_plugins)
    plugin_manager.load_plugins()

    assert len(plugin_manager.plugins) == 1 
