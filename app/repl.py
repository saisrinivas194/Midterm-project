import sys
import logging
import logging.config  # Import logging.config
import configparser

# Load the logging configuration
config = configparser.ConfigParser()
config.read('logging.conf')
logging.config.fileConfig(config)

# Create a logger
logger = logging.getLogger(__name__)

from app.commands.add import Add
from app.commands.subtract import Subtract
from app.commands.multiply import Multiply
from app.commands.divide import Divide
from app.plugin_manager import PluginManager
from app.commands.history import add_to_history, save_history, load_history, clear_history

def repl():
    logger.info("Advanced Python Calculator started. Type 'exit' to quit.")
    print("Advanced Python Calculator. Type 'exit' to quit.")
    
    # Create command instances
    add_command = Add()
    subtract_command = Subtract()
    multiply_command = Multiply()
    divide_command = Divide()
    
    # Initialize Plugin Manager
    plugin_manager = PluginManager('app/plugins/greet')  # Use file path, not module path
    plugin_manager.load_plugins()

    # Load previous history if it exists
    load_history()

    while True:
        user_input = input(">> ")
        
        if user_input.lower() == 'exit':
            save_history()  # Save history on exit
            logger.info("Calculator exited.")
            sys.exit(0)

        # Check if the user wants to run a plugin
        if user_input.lower() == 'greet':
            plugin_manager.run_plugins()
            continue

        # Commands to load and clear history
        if user_input.lower() == 'load history':
            load_history()
            continue
        elif user_input.lower() == 'clear history':
            clear_history()
            continue
        
        # Parse the user input
        parts = user_input.split()
        
        # Check the input format
        if len(parts) == 3:
            command = parts[0].lower()
            try:
                a, b = float(parts[1]), float(parts[2])
                
                if command == 'add':
                    result = add_command.execute(a, b)
                    add_to_history('add', a, b, result)  # Add to history
                    logger.debug(f"Performed addition: {a} + {b} = {result}")
                elif command == 'subtract':
                    result = subtract_command.execute(a, b)
                    add_to_history('subtract', a, b, result)  # Add to history
                    logger.debug(f"Performed subtraction: {a} - {b} = {result}")
                elif command == 'multiply':
                    result = multiply_command.execute(a, b)
                    add_to_history('multiply', a, b, result)  # Add to history
                    logger.debug(f"Performed multiplication: {a} * {b} = {result}")
                elif command == 'divide':
                    result = divide_command.execute(a, b)
                    add_to_history('divide', a, b, result)  # Add to history
                    logger.debug(f"Performed division: {a} / {b} = {result}")
                else:
                    logger.warning(f"Unknown command: {command}")
                    print("Unknown command. Please use 'add', 'subtract', 'multiply', or 'divide'.")
                    continue
                
                print(f"Result: {result}")
            except ValueError:
                logger.error("Invalid input: non-numeric value provided.")
                print("Please provide valid numbers.")
            except ZeroDivisionError:
                logger.error("Error: Division by zero attempted.")
                print("Error: Division by zero is not allowed.")
        else:
            logger.warning("Invalid input format.")
            print("Invalid input format. Use: <command> <a> <b>")

if __name__ == "__main__":
    repl()
