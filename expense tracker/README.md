# Expense Tracker (WIP)
Currently still learning about Streamlit, JSON and Pandas! Feedback is welcome.

-----------

A simple Python CLI tool to manage daily expenses. Built to practice working with data structures and functional programming in Python. 
<br><br>
The main script is based on the FreeCodeCamp (FCC) Scientific Computing with Python curriculum and I added some changes to it by adding:

* `try-except`: To validate so that the program doesn't error when the input is not a number.
* `JSON`:
* `Streamlit`:
* and more to go! (this project is still in progress..)

## Features (TODO: TWEAK)
* **Dynamic Data Storage**: Utilizes a list of dictionaries to manage expense records efficiently.
* **Functional Programming**: By implementing Python's built-in `map()` and `filter()` functions combined with `lambda` expressions for streamlined data processing & filtering.
* **Modular Design**: The codebase is organized into distinct, single-responsibility functions `(Add, Print, Total, Filter)` to ensure high maintainability and readability.
* **Interactive CLI Interface**: Features a robust command-line interface powered by a `while` loop, providing a seamless user experience for real time data entry and retrieval.
* **Data Transformation**: Demonstrates effective use of higher order functions to calculate totals and extract specific categories from the dataset.

## Project Structure
* `expense.py` — The main Python script that runs the expense tracker.
* `ui_expense.py` — (streamlit)
* `storage_py` — (json)
* `README.md` — The documentation you are reading right now.
* `requirements.txt` — TODO: ADD LATER
* `.gitignore` — TODO: ADD LATER

## How It Works (TODO: EXPLAIN THE MAIN PY, UI, JSON)
```bash
User Input -> Main Loop -> Function Logic -> Expenses List (Data Store) -> UI Output
```
* **Initialize**: The program starts with an empty list called `'expenses'`.
* **Menu Selection**: A `while` loop keeps the program running, presenting a menu for different actions.
* **Adding Data**: When an expense is added, the script creates a key-value pair for both `'amount'` and `'category'`, appending it to the collection.
* **Calculations**: To get the total, the program extracts all `'amount'` values from the dictionaries and sums them up using a `lambda function`.
* **Searching**: The filter feature scans the list and returns only the items where the category matches the user's input.  

## How To Use The `Terminal Ver`:
1. **Run the script**: Open your terminal and run `python track.py`
2. **Add expenses**: Choose option `1` and enter the amount and category.
3. **View result**: Choose option `2` to see all data, or `3` to see the total sum.
4. **Filter**: Choose option `4` to find specific expenses (e.g., "Food")

## How To Use The `Streamlit Ver`:
1. **TODO**: UPDATE LIST

## Output
(TODO: INSERT DOCUMENTATION 1 — TERMINAL VER)(DOCUMENTATION 2 — STREAMLIT VER)