import game_data
import random
import art


logo = art.logo
vs = art.vs

score =0
game_over = False

def get_random_person():
    return random.choice(game_data.data)

def format_person_data(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"


person1 =get_random_person()
person2 = get_random_person()

print(logo)

while not game_over:
    print(f"Welcome to the guessing game! You have {score} points.")

    print(format_person_data(person1))
    print(vs)
    print(format_person_data(person2))

    guess = input("Who has more followers? (a/b): ").lower()

    if guess == 'a' and person1['follower_count'] > person2['follower_count'] or \
            guess == 'b' and person2['follower_count'] > person1['follower_count']:
        score += 1
        print("You're right!")
        person1 = person2
        person2 = get_random_person()
    else:
        game_over = True
        print(f"Sorry, your score is {score}. Better luck next time!")



