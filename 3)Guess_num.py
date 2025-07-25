import random

while True:
    guessed_number = random.randint(1, 100)
    no_tries = 5
    while no_tries > 0:
        guess = input("Enter your Guess: ")
        if guess.lower() == 'exit':
            break
        if not guess.isdigit():
            print("Enter Valid number : ")
            continue
        guess = int(guess)
    
        if guess == guessed_number:
            print("You guessed it")
            break
        else:
            no_tries -= 1
            if guess < guessed_number:
                print("Please guess higher number")
            elif guess > guessed_number:
                print("Please guess lower number")
            print(f"Wrong guess! Try again. Tries left: {no_tries}")
    
    if no_tries == 0:
        print(f"Sorry, you ran out of tries. The number was {guessed_number}.")
