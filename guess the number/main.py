import random
target = random.randint(1, 10) # putting it outside the loop so it only generates once per game (not every time the user wants to play again)
print(target)

print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 10. Can you guess it?")

while True:
    try:
        n = int(input("Enter your guess: "))   
    except ValueError:
        print("Write down a number between 1 to 10, you dummy! Try again.")
        continue

    if n == target: # check the correct one first, then the wrong ones
        print("WHOA YOU GUESSED IT RIGHT! Wanna try again?")            
    elif n < target:
        print("Haha, too low! Try again if you dare.")        
    elif n > target:
        print("Damn that's too high! Wanna give it another shot?")

    play_again = input("Press Y to play again, N to start a new game, and any keys to quit: ")
    if play_again.strip() == 'Y' or play_again.strip() == 'y':
        continue
    elif play_again.strip() == 'N' or play_again.strip() == 'n':
        target = random.randint(1, 10) # generate a new number for the new game
        print("Alright, a new number has been selected. Let's see if you can guess it!")
        print(target) 
    else:
        print("Oh you wanna quit? Fine, thanks for playing! Goodbye!")
        break
