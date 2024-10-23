import pandas as pd
import os

# Initialize an empty DataFrame for history
history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result', 'Timestamp'])

def add_to_history(operation, operand1, operand2, result):
    global history_df
    # Create a new DataFrame for the new entry
    new_entry = pd.DataFrame([{
        'Operation': operation,
        'Operand1': operand1,
        'Operand2': operand2,
        'Result': result,
        'Timestamp': pd.Timestamp.now()
    }])
    
    # Use pd.concat to add the new entry to history_df
    history_df = pd.concat([history_df, new_entry], ignore_index=True)
    print(f"Added to history: {operation} {operand1} {operand2} = {result}")

def save_history(filename='calculation_history.csv'):
    global history_df
    # Save the history DataFrame to a CSV file
    history_df.to_csv(filename, index=False)
    print(f"History saved to {filename}.")

def load_history(filename='calculation_history.csv'):
    global history_df
    # Load history from a CSV file if it exists
    if os.path.exists(filename):
        history_df = pd.read_csv(filename)
        print("History loaded.")
    else:
        print("No history file found.")

def clear_history():
    global history_df
    # Clear the history DataFrame
    history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result', 'Timestamp'])
    print("History cleared.")
