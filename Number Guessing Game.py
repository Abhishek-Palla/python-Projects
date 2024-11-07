import random

print("Welcome to the number guessing game!")

difficulty = input("choose the difficulty level. Type 'easy' or 'hard' ").lower()
print("I'm thinking of a number between 1 and 100.")

lives = 0


def set_difficulty(difficulty):
    global lives
    if difficulty == 'easy':
        lives = 10
    elif difficulty == 'hard':
        lives = 5
    else:
        print("Invalid difficulty level. Please choose 'easy' or 'hard'.")

# Call the function with the user's input
set_difficulty(difficulty)

# Print the number of lives after setting the difficulty
print(f"You have {lives} lives.")

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

if difficulty == 'easy':
    while lives >0:
        guess = int(input("Guess the number: "))
        if guess == random_number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < random_number:
            lives -= 1
            print("Too low. Try again.")
            print("You have", lives, "lives left.")
        elif guess > random_number:
            lives -= 1
            print("Too high. Try again.")
            print("You have", lives, "lives left.")
        if lives == 0:
            print("Game over. You ran out of lives.")

if difficulty == 'hard':
    while lives >0:
        guess = int(input("Guess the number: "))
        if guess == random_number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < random_number:
            lives -= 1
            print("Too low. Try again.")
            print("You have", lives, "lives left.")
        elif guess > random_number:
            lives -= 1
            print("Too high. Try again.")
            print("You have", lives, "lives left.")
        if lives == 0:
            print("Game over. You ran out of lives.")






