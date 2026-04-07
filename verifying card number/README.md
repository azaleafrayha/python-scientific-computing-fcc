# Card Number Verifier (Luhn Algorithm)

This project is a Python implementation of the Luhn Algorithm, a formula used to validate various identification numbers, such as credit card numbers and IMEI numbers.

## Personal Tweak
This project is based on the FreeCodeCamp (FCC) Scientific Computing with Python curriculum. I have made a small but useful modification to the original code:

* **Interactive Input**: Instead of using a hardcoded variable, I added the input() function so users can type and verify their own card numbers directly in the terminal.

## Features
The program processes the input string using the following steps:
* **Normalization**: Removes spaces or dashes using str.maketrans and translate.
* **Reversal**: Reverses the number string to process it from right to left.
* **Odd Digits**: Sums up the digits in odd positions.
* **Even Digits**: Multiplies digits in even positions by 2. If the result is $\ge 10$, it sums the digits of the result (e.g., $14$ becomes $1 + 4 = 5$) before adding to the total.
* **Validation**: Checks if the final total is a multiple of 10 (total % 10 == 0).

## Project Structure
Inside this repository, you will find:
* `verification.py` — The main Python script that contains the Luhn Algorithm logic
* `README.md` — The documentation you are reading right now.

## How It Works
To verify a number, simply run the script and follow the on-screen prompt. The program handles formatting (like spaces or dashes) automatically.

## Documentation & Examples
What it looks like in your terminal:

### Case 1: Testing a valid Visa card
```bash
Enter credit card number: 4111-1111-1111-1111
VALID!
```

### Case 2: Testing an invalid sequence
```bash
Enter credit card number: 1234 5678 1234 5678
INVALID!
```
