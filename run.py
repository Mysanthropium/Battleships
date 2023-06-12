# Legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot


from random import randint
import sys
import os


BOAT = """
                __/___            
          _____/______|           
  _______/_____\_______\_____     
  \              < < <       |    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


"""
Board for holding the ship locations.
"""


"""
List of all letters and numbers, converted.
"""
letters_to_numbers = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7
}


"""
Clear the screen based on the operating system to only show the game itself
"""


def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')


"""
Defining the board row and columns, creating seperators through each iteration.
"""


def print_board(board):
    print('  A B C D E F G H')
    print('  -+-+-+-+-+-+-+-')
    row_number = 1

    # Gives the battlefield a nicer and cooler look.
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1


"""
Define a function to let the computer create ships randomly over the board.
Check if X exists, or check X.
"""


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


"""
Ask the player where they want to place their battleships.
If not in a valid row or column, get error message.
Convert the letters to numbers to pass it the correct column.
"""


def get_ship_location():
    while True:
        try:
            row = input("Please enter a ship row 1-8:\n")
            if row in '1, 2, 3, 4, 5, 6, 7, 8':
                row = int(row) - 1
                break
            else:
                print('Enter a valid row between 1-8')
        except ValueError:
            print('Enter a valid row between 1-8')
    while True:
        try:
            column = input("Please enter a ship column A-H:\n").upper()
            if column in 'A, B, C, D, E, F, G, H':
                column = letters_to_numbers[column]
                break
            else:
                print('Enter a valid letter between A-H')
        except KeyError:
            print('Enter a valid letter between A-H')
    return row, column


"""
Loop through each row and column to check if there's a ship on the board.
"""


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


clear_screen()  # Clears the screen depending on the players operating system.


def start_game():
    HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
    GUESS_BOARD = [[' '] * 8 for x in range(8)]
    create_ships(HIDDEN_BOARD)
    turns = 15
    while turns > 0:
        print(
            '\nTries left: ' + str(turns) + '\n\nGood Luck!\n'
        )
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == '-':
            print("You've already guessed that")
        elif HIDDEN_BOARD[row][column] == 'X':
            print('\n--------------------------------------\nYou HIT!')
            GUESS_BOARD[row][column] = 'X'
            turns -= 1
        else:
            print('\n--------------------------------------\nYou MISS!')
            GUESS_BOARD[row][column] = '-'
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print('\nCongratulations! You sunk all the battleships!\n')
            play_again = input("Play again? Type 'y':\n")
            if play_again == 'y':
                clear_screen()
                start_screen()
                create_ships(HIDDEN_BOARD)
            else:
                clear_screen()
                print('Thanks for playing!')
        if turns == 0:
            print('\nYou ran out of turns and the game is over...\n')
            play_again = input("Play again? Type 'y':\n")
            if play_again == 'y':
                clear_screen()
                start_screen()
                create_ships(HIDDEN_BOARD)
            else:
                clear_screen()
                print('Thanks for playing!')


"""
Start screen to show name of the game and settings.
"""


def start_screen():
    print(
        '\n!!!!!!!!!!!! BATTLESHIPS !!!!!!!!!!!!!'
        )
    print(BOAT)
    print(
        'How to play:'
        )
    print(
        'You first get to choose a row between 1-8, then a column between A-H.'
        )
    print(
        'There is 5 hidden ships, you got 15 tries to hit them all!\n'
        )
    print(
        'Guess a battleship location to strike!\n'
        )
    print(
        'Rows 1-8\nColumns A-H\nTotal ships: 5'
        )
    print(
        '\n- = MISS'
        )
    print(
        'X = HIT'
        )
    print(
        '\n--------------------------------------'
        )
    game_on = input("Type 'a' to start game:\n")
    if game_on == 'a':
        start_game()
    else:
        print('Invalid input')
        clear_screen()
        start_screen()


start_screen()
