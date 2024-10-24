# app/plugins/plugin.py


class Plugin:
    def run(self, *args):
        raise NotImplementedError("Plugins must implement the 'run' method.")
