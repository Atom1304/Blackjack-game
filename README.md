Blackjack Game in Python
This project is a simple text-based Blackjack game created using Python. The game allows a user to play against the computer, following the traditional rules of blackjack. It demonstrates the use of functions, control flow, random number generation, and basic user input handling.

How the Game Works
The game is played between a user and the computer (dealer).
Both players are dealt two cards to start the game.
The user can choose to draw additional cards or stop.
The computer will continue to draw cards until it reaches a score of at least 17 or goes over 21.
The goal is to get as close to 21 as possible without exceeding it.
If the player or the computer hits 21 with just two cards (Ace + 10-value card), it is considered a Blackjack.
Features
Reusable code: The game logic is encapsulated in functions for modularity and reusability.
Randomized card dealing: Cards are dealt using Python's random.choice() function.
Score calculation: The game calculates the player's and computer's scores, adjusting for the value of an Ace (either 11 or 1) to avoid exceeding 21.
Comparison function: The game compares the final scores to determine the winner.
Multiple game rounds: The player can choose to play multiple rounds of blackjack.
Rules
The card values are as follows:
Cards 2 through 10 are worth their face value.
J, Q, K are each worth 10 points.
Aces can be worth 11 points, but if the score goes over 21, they count as 1 point.
The player draws cards first and can keep drawing until they decide to stop or go over 21.
The computer draws cards until its score is 17 or higher, or it goes over 21.
A Blackjack is when the player or computer has an Ace and a 10-point card in their initial two cards.
