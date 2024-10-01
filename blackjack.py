import random
def game():
    """The entire game created as a function for resuablity and file sharing"""
    def deal_cards():
        """Function to deal the cards to the user and player."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        """Function to calculate the score of the user and the computer."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0  
        if sum(cards) > 21 and 11 in cards:  
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    def compare(c_score, u_score):
        """Compares the score to determine the winner."""
        if u_score == c_score:
            return "It's a draw!"
        elif c_score == 0:
            return "Computer has blackjack. You lose!"
        elif u_score == 0:
            return "You have blackjack! You win!"
        elif u_score > 21:
            return "You went over 21. You lose!"
        elif c_score > 21:
            return "Computer went over 21. You win!"
        elif u_score > c_score:
            return "You win!"
        else:
            return "You lose!"

    def play_game():
        """The function to start a game."""
        user_cards = []
        computer_cards = []
        for _ in range(2):
            user_cards.append(deal_cards())
            computer_cards.append(deal_cards())

        IS_GAME_OVER = False

        while not IS_GAME_OVER:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                IS_GAME_OVER = True
            else:
                choice = input("Do you want to draw another card? Type 'y' for yes and 'n' for no: ").lower()
                if choice == "y":
                    user_cards.append(deal_cards())
                else:
                    IS_GAME_OVER = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_cards())
            computer_score = calculate_score(computer_cards)

        print(f"\nYour final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(computer_score, user_score))

    # Main game loop
    while input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no: ").lower() == "y":
        play_game()
game()