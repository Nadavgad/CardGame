# Card Game System

## Overview

The Card Game System manages a simple card game between two players. Players are assigned cards, and the winner of each round is determined based on the values of the cards played.
The game concludes with the announcement of the overall winner.

## Classes

### 1. `Card`

- Represents a playing card.
- Attributes:
  - `number`: The number or face of the card (2-10, prince, queen, king, ace).
  - `shape`: The suit of the card (Clover, Heart, Diamond, Leaf).
- Methods:
  - `calculate`: Calculates the value of the card based on its number and shape.
  - `__str__`: Returns a string representation of the card.

### 2. `Player`

- Represents a player in the card game.
- Attributes:
  - `name`: The name of the player.
  - `round_counter`: The number of rounds won by the player.
  - `cards`: An array containing the player's cards.
- Methods:
  - `add_card(card)`: Adds a card to the player's cards.

### 3. `System`

- Manages the card game.
- Attributes:
  - `cards_array`: An array containing all the cards in the game.
  - `player1` and `player2`: Instances of the `Player` class.
- Methods:
  - `__init__()`: Initializes the card game system.
  - `start()`: Initiates the game, prompts users for player names, distributes cards, prints players' cards, and determines the winner.
  - `__print_cards(player)`: Prints the cards of a given player.
  - `generate_cards()`: Generates a list of cards with numbers and shapes.
  - `distribute_cards()`: Distributes cards to player1 and player2, shuffling the deck.
  - `display_cards()`: Displays all cards in the system.
  - `find_winner()`: Determines the winner of the game based on the values of the played cards.

## Usage

1. Create an instance of the `System` class.
2. Call the `start()` method to initiate the game.
3. Follow the prompts to enter player names.
4. Observe the game as it progresses and find out the winner.

## Example

```python
if __name__ == '__main__':
    system = System()
    system.start()
