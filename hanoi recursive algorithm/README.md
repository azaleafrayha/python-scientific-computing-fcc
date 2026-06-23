# Tower of Hanoi Puzzle

The Tower of Hanoi is a mathematical puzzle where the objective is to move a stack of disks from the source rod to the target rod using an auxiliary rod, following three simple rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one stack and placing it on top of another.
3. No disk may be placed on top of a smaller disk.


## Project Structure

This project features two different solving methods implemented as separate files within the same folder:

* **`recursive.py`** — Solves the puzzle using functions that call themselves.
* **`iterative.py`** — Solves the puzzle using loops and explicit mathematical logic.


## Recursive vs. Iterative: In a Nutshell

Here is a simple way to understand and remember how both approaches solve the same problem:

### 1. Recursive Approach (`recursive.py`)
* **The Logic:** *"To solve for $n$ disks, I will divide it into smaller sub-tasks. I'll move $n-1$ disks out of the way first, move the largest disk to the target, and then move those $n-1$ disks back on top."*
* **How it works:** The function literally calls itself with a smaller number of disks ($n-1$) until it hits the base case (1 disk).
* **Pros & Cons:** Extremely elegant and matches human logic perfectly, but uses more memory because computer has to remember every function call stack.

### 2. Iterative Approach (`iterative.py`)
* **The Logic:** *"I will not call any functions inside themselves. Instead, I will use a simple loop (`while` or `for`) and calculate the exact legal move step-by-step from move $1$ all the way to move $2^n - 1$."*
* **How it works:** It uses sequential repetition and mathematical rules (like checking if the move number is odd/even or using the modulo operator) to determine which disk moves next.
* **Pros & Cons:** Highly memory-efficient because it doesn't create a call stack, but the code requires more manual tracking of the disks' states.