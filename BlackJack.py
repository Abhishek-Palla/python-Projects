import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score

def play_game():
    print("Welcome to Black Jack")
    player_cards = random.choices(cards, k=2)
    dealer_cards = random.choices(cards, k=2)

    game_over = False
    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game_over = True
        else:
            choice = input("Do you want to hit or stand? (h/s): ")
            if choice.lower() == 'h':
                player_cards.append(random.choice(cards))
            else:
                game_over = True

    while dealer_score < 17 and player_score <= 21:
        dealer_cards.append(random.choice(cards))
        dealer_score = calculate_score(dealer_cards)

    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")

    if player_score > 21:
        print("You went over. You lose!")
    elif dealer_score > 21:
        print("Dealer went over. You win!")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("You lose!")
    else:
        print("It's a draw!")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_game()

print("Thanks for playing!")
