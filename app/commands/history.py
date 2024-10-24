import pandas as pd
import os

history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result', 'Timestamp'])

def add_to_history(operation, operand1, operand2, result):
    global history_df
    new_entry = pd.DataFrame([{
        'Operation': operation,
        'Operand1': operand1,
        'Operand2': operand2,
        'Result': result,
        'Timestamp': pd.Timestamp.now()
    }])

    if not new_entry.empty and new_entry.notna().all().all():

        history_df = pd.concat([history_df, new_entry], ignore_index=True)
        print(f"Added to history: {operation} {operand1} {operand2} = {result}")
    else:
        print("Invalid entry: not added to history.")

def save_history(filename='calculation_history.csv'):
    global history_df

    history_df.to_csv(filename, index=False)
    print(f"History saved to {filename}.")

def load_history(filename='calculation_history.csv'):
    global history_df
    if os.path.exists(filename):
        history_df = pd.read_csv(filename)
        print("History loaded.")
    else:
        print("No history file found.")

def clear_history():
    global history_df

    history_df = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result', 'Timestamp'])
    print("History cleared.")
