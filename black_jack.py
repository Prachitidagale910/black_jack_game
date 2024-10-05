import random as ran

# Game title for better UI
def display_game_title():
    print("#######################################################")
    print("#                                                     #")
    print("#   ██████╗ ██╗      █████╗  ██████╗██╗  ██╗     ██╗   #")
    print("#  ██╔═══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝    ███║   #")
    print("#  ██║   ██║██║     ███████║██║     █████╔╝     ╚██║   #")
    print("#  ██║   ██║██║     ██╔══██║██║     ██╔═██╗      ██║   #")
    print("#  ╚██████╔╝███████╗██║  ██║╚██████╗██║  ██╗     ██║   #")
    print("#   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═╝   #")
    print("#                                                     #")
    print("#######################################################")
    print("           THE ULTIMATE BLACKJACK EXPERIENCE\n")

# Rest of the game logic below

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return ran.choice(cards)

def calculate_score(card_list):
    """Calculates the score of a hand."""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0  # Blackjack (Ace + 10)
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

# Call the title function at the start of the game
display_game_title()

# Function to compare user score and dealer score
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "You lose, dealer has Blackjack!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Dealer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

# Main game logic
def play_game():
    print("Welcome to Blackjack!")
    
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal two cards to the user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Dealer's first card: {computer_cards[0]}")

        # Check if the game should end
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Dealer plays, must draw until score is 17 or above
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))  # Compare scores

# Ask the user if they want to restart the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
