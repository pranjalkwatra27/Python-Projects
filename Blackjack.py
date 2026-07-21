import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(user_cards, computer_cards):

    # Player's Turn
    while True:

        print(f"\nYour Cards: {user_cards}")
        print(f"Your Total: {sum(user_cards)}")

        # Convert Ace (11 -> 1)
        while sum(user_cards) > 21 and 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)

        if sum(user_cards) > 21:
            print("\nPlayer Busted. Dealer Wins!")
            return

        choose = input("\nHit or Stand? ").lower()

        if choose == "hit":
            user_cards.append(random.choice(cards))
        elif choose == "stand":
            break
        else:
            print("Invalid Choice!")

    # Dealer's Turn
    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))

    while sum(computer_cards) > 21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)

    player_total = sum(user_cards)
    dealer_total = sum(computer_cards)

    print("\n-------------------------")
    print(f"Your Cards: {user_cards}")
    print(f"Your Total: {player_total}")
    print(f"Dealer Cards: {computer_cards}")
    print(f"Dealer Total: {dealer_total}")
    print("-------------------------")

    if dealer_total > 21:
        print("Dealer Busted. Player Wins!")
    elif player_total > dealer_total:
        print("Player Wins!")
    elif dealer_total > player_total:
        print("Dealer Wins!")
    else:
        print("Draw!")


# ==========================
# Main Game Loop
# ==========================

while True:

    print("\n====== BLACKJACK ======\n")

    user_cards = [
        random.choice(cards),
        random.choice(cards)
    ]

    computer_cards = [
        random.choice(cards),
        random.choice(cards)
    ]

    print(f"Your Cards: {user_cards}")
    print(f"Computer's First Card: {computer_cards[0]}")

    calculate_score(user_cards, computer_cards)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break
