# Card Game README

The game involves players and cards, and the goal is to determine the winner based on the values of the cards played in each round.

## Classes

### 1. Player

- **Attributes:**
  - `name`: The name of the player.
  - `win_round_counter`: Counter for the number of rounds won by the player.
  - `cards`: An array containing the player's cards after the initial card distribution.

- **Methods:**
  - `add_card(card)`: Adds a card to the player's cards array.

### 2. Card

- **Attributes:**
  - `number`: The number or type of the card (e.g., 2, Ace, Prince).
  - `shape`: The shape of the card (e.g., Heart, Clover).

- **Methods:**
  - `calculate(card)`: Calculates the value of the card based on specific rules.
  - `__str__()` : Returns a string representation of the card.

### 3. Game

- **Attributes:**
  - `deck_array`: The deck of cards created at the beginning of the game.
  - `player1`: An instance of the `Player` class representing the first player.
  - `player2`: An instance of the `Player` class representing the second player.

- **Methods:**
  - `generate_cards()`: Generates a new deck of cards.
  - `get_player_names()`: Takes input for player names.
  - `distribute_cards()`: Distributes the cards to the players.
  - `Validate_same_number_cards()`: Validates that both players have the same number of cards.
  - `game_rounds(card1, card2, game_round)`: Conducts a round of the game, determining the winner.
  - `find_round_winner()`: Finds the winner of each round.
  - `__print_cards(player)`: Prints the cards of a specific player.
  - `print_players_cards()`: Prints the cards of both players.
  - `print_winner(winner)`: Prints the winner of the game.
  - `find_game_winner()`: Determines the overall winner of the game.
  - `start()`: Starts the game, executing various steps to determine the winner.

### Constants

```python
MENU_CONTENT = """WELCOME TO THE GAME OF WONDERS!\n"""
START_GAME = """ \n                  ***** GAME STARTED ***** """
FIRST_PLAYER = " Please select the first player name :\n "
SECOND_PLAYER = " Please select the second player name :\n"
TIE = "IT'S A TIE!"
PLAYER_CARDS = "\nPLAYERS CARDS"
CARDS_GAME = "ALL CARDS IN THE GAME:"
SAME_CARD_NUMBER = "BOTH PLAYERS MUST HAVE THE SAME NUMBER OF CARDS."
NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Prince", "Queen", "King", "Ace"]
SHAPES = ["♣", "♥", "♦", "♠"]
MIN = 1000
FIRST_MIDDLE = 2000
SECOND_MIDDLE = 3000
MAX = 4000
