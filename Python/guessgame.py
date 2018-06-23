import random    
guesses = 6
number = random.randint(0, 10)
win = False

while guesses > 0:
    guess = int(input("Guess: "))

    guesses -= 1

    if guess == number:
        win = True
        guesses = 0
    elif abs(guess - number) < 6: 
        print("You are very close")
    elif guess > number:
        print("Your guess is too high", guesses, "remaining")
    elif guess < number:
        print("Your guess is too low", guesses, "remaining")

if win == False:
    print("Sorry, you didn't guess the number", number)
else:
    print("Congrats, you guessed correct")