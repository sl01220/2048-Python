import random
def guess_number():
    secret_number = random.randint(1, 100)
    remaining_attempts = 10
    for i in range(10):
        guess = int(input("guess:"))
        remaining_attempts -= 1
        if guess == secret_number:
            print("BINGO!")
            return
        elif guess > secret_number:
            print("Too big")
        else:
            print("Too small")
        print("You have", remaining_attempts, "attempts left.")
    print("ans=", secret_number)
guess_number()