import json

FILE = "expenses.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)
