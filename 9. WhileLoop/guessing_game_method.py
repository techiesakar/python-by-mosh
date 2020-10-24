# Secret Number is "9"
# Max Guess allowed is 3
# Ask for guess
# If max_guess limit crossed
#   "Sorry you failed"
# Correct guess
# "Your guess is correct"


secret_number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Guess is correct")
        break
else:
    print("limit Reached")

