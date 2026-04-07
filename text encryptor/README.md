# Vigenere Cipher Tool

A Python-based encryption and decryption tool using the Vigenere Cipher algorithm. This project was developed as part of the **freeCodeCamp** Scientific Computing with Python curriculum.

## Personal Tweaks
I have modified the original freeCodeCamp project to make it more functional and interactive:
* **Interactive CLI Menu**: Added a menu system so users can choose between encryption and decryption modes without changing the code.
* **User-Centric Flow**: Refined the input handling to provide a more intuitive "tool-like" experience.

## Features
* **Encryption**: Secure your messages using a custom keyword.
* **Decryption**: Recover the original message using the same keyword.
* **Case Insensitive**: Automatically handles text in lowercase.
* **Non-Alpha Support**: Keeps spaces and special characters intact.

## Project Structure
Inside this repository, you will find:
* `encrypt.py` — The main Python script that contains the Vigenere Cipher logic (encryption & decryption).
* `README.md` — The documentation you are reading right now.

## How it Works
The Vigenere Cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers. Unlike a simple Caesar cipher that shifts every letter by the same amount, this tool uses a keyword to determine the shift for each letter. The shift amount is determined by the position of the corresponding letter of the keyword in the alphabet.

## Documentation
Here is how the program looks when executed in the terminal:

### Option 1: Encrypting a Message (Locking)
```bash
=== Vigenere Cipher Tool ===
1. Encrypt a message (Lock)
2. Decrypt a message (Unlock)
Choose (1/2): 1

Enter the text: hello world
Enter the key: secret
Original text: hello world
Encrypted result: zincs pgvnu
```

### Option 2: Decrypting a Message (Unlocking)
```bash
=== Vigenere Cipher Tool ===
1. Encrypt a message (Lock)
2. Decrypt a message (Unlock)
Choose (1/2): 2

Enter the text: zincs pgvnu
Enter the key: secret

Ciphertext: zincs pgvnu
Decrypted result: hello world
```
