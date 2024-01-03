MENU_CONTENT = """WELCOME TO THE GAME OF WONDERS!\n"""
START_GAME = """ \n                  ***** GAME STARTED ***** """
FIRST_PLAYER = " Please select the first player name :\n "
SECOND_PLAYER = " Please select the second player name :\n"
TIE = "IT'S A TIE!\n"
PLAYER_CARDS = "\nPLAYERS CARDS"
CARDS_GAME = "ALL CARDS IN THE GAME:"
SAME_CARD_NUMBER = "BOTH PLAYERS MUST HAVE THE SAME NUMBER OF CARDS."
NUMBERS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Prince", "Queen", "King", "Ace"]
SHAPES = ["♣", "♥", "♦", "♠"]
MIN = 1000
FIRST_MIDDLE = 2000
SECOND_MIDDLE = 3000
MAX = 4000
ROUND_RESULT_MESSAGE = (
    "GAME ROUND {game_round} : {player1_name} has played {card1_number} of {card1_shape}, its "
    "value is {value1}\n"
    "{player2_name} has played {card2_number} of {card2_shape}, its value is {value2}"
)
WIN_ROUND_MESSAGE = "{player_name}'s WIN ROUND {game_round}.\n"
PLAYER_CARDS_HEADER_MESSAGE = "\n{player_name}'s cards : \n"
WINNER_MESSAGE = (
    "\n **********   THE WINNER IS {winner_name} WHO WON IN {round_counter} ROUNDS   ********** \n \n \n"
)
CARD_REPRESENTATION = "{card_number} of {card_shape}"
