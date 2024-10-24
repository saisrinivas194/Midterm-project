import unittest

from app.commands.command import Command

class TestCommand(Command):
    def execute(self, *args):
        return "Executed"

class TestCommandUnit(unittest.TestCase):
    
    def test_command_execute(self):
        command = TestCommand()
        result = command.execute()
        self.assertEqual(result, "Executed")

    def test_command_execute_not_implemented(self):
        """Test that calling execute on the base Command class raises NotImplementedError."""
        command = Command()
        with self.assertRaises(NotImplementedError):
            command.execute()

    def test_command_with_args(self):
        """Test that the execute method handles arguments correctly."""
        class TestCommandWithArgs(TestCommand):
            def execute(self, *args):
                return f"Executed with args: {', '.join(args)}"

        command = TestCommandWithArgs()
        result = command.execute("arg1", "arg2")
        self.assertEqual(result, "Executed with args: arg1, arg2")

if __name__ == "__main__":
    unittest.main()
