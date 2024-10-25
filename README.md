
# Advanced Python Calculator

## Table of Contents
- [Introduction](#introduction)
- [Design Patterns](#design-patterns)
  - [Command Pattern](#command-pattern)
  - [Facade Pattern](#facade-pattern)
  - [Singleton Pattern](#singleton-pattern)
  - [Factory Method Pattern](#factory-method-pattern)
- [Environment Variables](#environment-variables)
- [Logging Practices](#logging-practices)
- [Exception Handling](#exception-handling)
  - [LBYL (Look Before You Leap)](#lbyl-look-before-you-leap)
  - [EAFP (Easier to Ask for Forgiveness than Permission)](#eafp-easier-to-ask-for-forgiveness-than-permission)
- [Video Demonstration](#video-demonstration)
- [Linting and Type Checking Compliance](#linting-and-type-checking-compliance)
- [Final GitHub Actions Configuration](#final-github-actions-configuration)

## Introduction
This repository contains an advanced calculator application implemented in Python, showcasing various design patterns, robust error handling, and logging capabilities. The application supports basic arithmetic operations and provides a command-line interface (REPL) for user interaction.

## Design Patterns

### Command Pattern
The Command pattern encapsulates a request as an object, allowing for parameterization of clients with different requests. This pattern is used in the calculator to separate the invocation of operations from their implementations.

**Implementation:** In the `app/commands` directory, each operation (e.g., addition, subtraction) is represented as a command class that implements a common interface.

**Code Example:**
```python
# app/commands/command.py
class Command:
    def execute(self, *args):
        raise NotImplementedError("You should implement this method.")
```
```python
# app/commands/add.py
from app.commands.command import Command

class Add(Command):
    def execute(self, x, y):
        return x + y
```

### Facade Pattern
The Facade pattern provides a simplified interface to a complex subsystem. In this application, the REPL acts as a facade that allows users to interact with different commands without needing to understand the underlying complexity.

**Implementation:** The `repl()` function in `app/repl.py` serves as the facade, managing user input and invoking the appropriate command.

**Code Example:**
```python
def repl():
    add_command = Add()
    # ...
    while True:
        user_input = input(">> ")
        # Process user input and execute the corresponding command
```

### Singleton Pattern
The Singleton pattern restricts the instantiation of a class to one single instance. While this pattern is not explicitly implemented in the current code, it can be applied for the `PluginManager` to ensure that only one instance manages the plugins.

**Code Example (Hypothetical):**
```python
class PluginManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory Method Pattern
The Factory Method pattern defines an interface for creating an object but allows subclasses to alter the type of objects that will be created. This pattern can be applied in the plugin system where different plugins can be created without specifying the exact class.

**Implementation:** The `PluginManager` can dynamically load and instantiate plugin classes.

**Code Example:**
```python
# app/plugins/plugin.py
class Plugin:
    def run(self, *args):
        raise NotImplementedError("Plugins must implement the 'run' method.")
```

## Environment Variables
Environment variables are utilized for configuring various aspects of the application, including logging levels. This approach allows for flexibility and security, especially when dealing with sensitive configurations.

**Usage:** You can set environment variables in a `.env` file or directly in your system. The application loads these variables to configure logging.

**Code Example:**
```python
# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv()
log_level = os.getenv('LOG_LEVEL', 'INFO')
```

## Logging Practices
Logging is configured using a dedicated configuration file to manage severity levels and output format effectively. Logs are crucial for debugging and tracking the application's behavior.

**Configuration:** The logging configuration is managed through `logging.conf`, which specifies log levels, handlers, and formatters.

**Code Example:**
```ini
[logger_root]
level=INFO
handlers=fileHandler,consoleHandler
```

**Logging in Code:**
```python
import logging
logger = logging.getLogger(__name__)

logger.info("This is an info message.")
logger.error("This is an error message.")
```

## Exception Handling

### LBYL (Look Before You Leap)
The LBYL approach checks conditions before executing actions. This is evident in operations where we verify input validity before performing arithmetic calculations.

**Code Example:**
```python
if y == 0:
    raise ValueError("Cannot divide by zero.")
```

### EAFP (Easier to Ask for Forgiveness than Permission)
EAFP attempts to execute code and catches exceptions if they arise. This is commonly used in the calculator's REPL for arithmetic operations.

**Code Example:**
```python
try:
    result = divide_command.execute(a, b)
except ValueError as e:
    print(e)
```

## Video Demonstration
A video demonstration showcasing the key features of the calculator, including basic operations, history management, plugins, and logging behavior, can be found here: [Link to Video](#).

## Linting and Type Checking Compliance
To maintain code quality, `flake8` and `mypy` checks are run regularly. Ensure you address any remaining issues such as line length errors, unused imports, or missing type hints.

### Running Linting and Type Checking
Linting and type-checking can be run locally with the following commands:
```bash
flake8 .
mypy .
```

## Final GitHub Actions Configuration
The GitHub Actions workflow is set up to automatically run tests, lint checks, and type checks. This ensures that all tests pass before merging changes into the main branch.

**GitHub Actions Configuration:**
```yaml
name: Python application

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python 3.10
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Tests
        run: |
          pytest
          flake8 .
          mypy .
```

