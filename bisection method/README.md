# Finding Square Root of a Number
I practiced using the `bisection method` in Python to find square root of a number automatically.

## Personal Tweak
This project is based on the FreeCodeCamp (FCC) Scientific Computing with Python curriculum. I added the `input()` function to let users add the number theirself.

## Features
* **Safety First**: It has a built-in guard (the `ValueError`) that stops the code immediately if you try to find the square root of a negative number, which isn't possible in real numbers.
* **Instant Shortcuts**: It doesn't waste energy on obvious math. If you ask for the root of 0 or 1, it just gives you the answer instantly.
* **Adjustable Precision**: Using `tolerance`, you can decide exactly how accurate you want the answer to be. By default, it stops once it's within 0.0000001 of the true value.
* **Anti-Loop Protection**: The `max_iterations` acts like a safety timer. If the math gets too complicated and the code can't find a perfect answer quickly, it quits instead of freezing your computer lol

## Project Structure
Inside this repository, you will find:
* `bisection.py` — The main Python script.
* `README.md` — The documentation you are reading right now.

## How It Works (The Logic)
The core of this is the Bisection Method, which is just a fancy way of saying "splitting things in half until you get it right."

1. **Setting the Boundaries**: The code starts by picking a range where the answer could be. It sets low at 0 and high at the number you entered.

2. **The Guessing Game**: It picks the middle point `(mid)` between low and high. And to see if the guess is right, the code squares it `(mid**2)`. It then calculates the "gap" between that result and your target number.

3. **Checking the "Gap"**: This is where `abs()` comes in. It checks the gap between its guess and the real answer. If that gap is smaller than your `tolerance` (0.0000001), it shouts *"Found it!"* and stops.

4. **Narrowing the Search**: If the gap is still too big, the code makes a choice :
    * If the guess was too low, it moves the low boundary up to the middle.
    * If the guess was too high, it moves the high boundary down to the middle.

5. **Repeat**: It keeps cutting the search area in half over and over again. It keeps going until it either hits the target or runs out of `max_iterations`. 

## Output Example
For an example, I want to find the square root of 16:
```bash
Enter your number to find the square root: 16
The square root of 16 is approximately 4.0
```

How about something even more complex? In this case I want to find the square root of 189.45:
```bash
Enter your number to find the square root: 189.45
The square root of 189.45 is approximately 13.764083696853774
```