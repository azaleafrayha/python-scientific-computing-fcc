# Guess the Number

A simple, text-based guessing game built to practice core Python control flow. This was a deliberate exercise in handling state and loops sequentially *without* wrapping the logic into functions (`def`) just yet.

It also features a bit of an attitude if you enter the wrong input. 😉

## Features

* **Interactive Game Loop:** Uses a `while True` loop to keep the game alive, allowing you to replay or trigger a fresh round with a new number without restarting the script.
* **Crash Prevention:** Includes a `try/except` block to catch `ValueError` exceptions (like typing words instead of numbers) so the terminal doesn't crash.
* **Sassy Feedback:** Custom response dialogs depending on how high, low, or completely off your guess is.

## How to Run

Run the script from the root of the repository:

```bash
python "guess the number/main.py"