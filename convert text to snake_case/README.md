# Text Converter to snake_case
I built this converter because sometimes you get data or code from other systems (like JavaScript or Java) that use `PascalCase` or `camelCase`. This tool helps automate the boring task of renaming everything to keep your Python code consistent.

## 🛠️ Personal Tweak
This project is based on the FreeCodeCamp (FCC) Scientific Computing with Python curriculum. And I added `if __name__ == '__main__':` to make the script **smart**.

* **With it**: The script knows the difference between being run directly (it executes the `main()` function) and being imported as a tool (it stays quiet and just lets the other script use the function). It’s basically a "safety switch" for professional code.
* **Without it**: If another script tried to "borrow" (import) my conversion function, the program would accidentally start asking for user input immediately.

## 🚀 Features
* **Universal Input**: Handles both `camelCase` (starts lowercase) and `PascalCase` (starts uppercase).
* **Auto-formatting**: Automatically inserts underscores before capital letters and converts them to lowercase.
* **Clean Output**: Uses `.strip('_')` to make sure there are no messy underscores at the very beginning or end of your new string.

## 📂 Project Structure
Inside this repository, you will find:
* `convert.py` — The main Python script that converts `PascalCase/camelCase` text to a `snake_case`
* `README.md` — The documentation you are reading right now.

## 💡 How It Works
The logic follow a simple "Check and Change" loop:
1. **Iterate**: It looks at every single character in your text one by one.
2. **Detect**: If it finds an Uppercase letter, it thinks: *"Aha! This is a new word,"* and adds an underscore before it.
3. **Lower**: It then turns that uppercase letter into a lowercase one.
4. **Join**: Once it’s done with the whole list, it glues everything back together into a single string.
5. **Trim**: Finally, it trims off any leading underscores (which usually happen if the first letter was capitalized).

## 💻 Documentation
For an example, I want to turn "HelloWorld" to a `snake_case`. And this is what it looks in the terminal:
```bash
Enter a PascalCase or camelCase string: HelloWorld

hello_world
```