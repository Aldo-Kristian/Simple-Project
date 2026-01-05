secret_number = 9
guess_attempt = 0 
guess_limit = 3

while guess_attempt < guess_limit:
    guess = int(input("Guess: "))
    guess_attempt += 1
    if guess == secret_number:
        print("You won")
        break
else:
    print("You lose")