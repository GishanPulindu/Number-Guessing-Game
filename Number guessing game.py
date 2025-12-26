import random

print("""Welcome to the number guessing game!
I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it.""")
RandomNo = random.randint(1, 100)
max_attempts = 7
attempts = 0

while attempts <= max_attempts:
    if attempts == 7:
        print("Game Over!")
        print(f"The number is {RandomNo}")
        break
    else:
        try:
            Num = int(input("Enter your guess : "))
        except ValueError:
            print("Invalid Input! Try again")
            attempts += 1
            continue
        if Num > 100 or Num < 1:
            print("Enter a number between 1 and 100")
        else:
            if Num > RandomNo:
                print("Too High, Try Again!")
                attempts += 1
            elif Num < RandomNo:
                print("Too Low, Try Again!")
                attempts += 1
            else:
                print(f"Congratulations! You guessed the number in {attempts+1}attempts")
                break













