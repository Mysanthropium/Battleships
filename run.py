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


LOGO = """
__________    ___________________________.____     ___________ _________ ___ ___ ._____________ 
\______   \  /  _  \__    ___/\__    ___/|    |    \_   _____//   _____//   |   \|   \______   \ 
 |    |  _/ /  /_\  \|    |     |    |   |    |     |    __)_ \_____  \/    ~    \   ||     ___/
 |    |   \/    |    \    |     |    |   |    |___  |        \/        \    Y    /   ||    |    
 |______  /\____|__  /____|     |____|   |_______ \/_______  /_______  /\___|_  /|___||____|    
        \/         \/                            \/        \/        \/       \/                
"""


"""
Board for holding the ship locations.
"""
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]


"""
Playing board to show hits and misses.
"""
GUESS_BOARD = [[' '] * 8 for x in range(8)]


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
    row = input('Please enter a ship row 1-8:\n')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-8:\n')
    column = input('Please enter a ship column A-H:\n').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-H:\n').upper()
    return int(row) - 1, letters_to_numbers[column]


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

"""
Start screen to show name of the game and settings.
"""


def start_screen():
    print(
        '\n!!!!!!!!!!!! BATTLESHIPS !!!!!!!!!!!!!'
        )
    print(BOAT)
    print(
        'Guess a battleship location to strike!\n'
        )
    print(
        'Rows 1-8: 8\nColumns A-H: 8\nTotal ships: 5'
        )
    print(
        '\n--------------------------------------'
        )


start_screen()
create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print(
        '\nTries left: ' + str(turns) + '\n\nGood Luck!\n'
    )
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print("You've already guessed that")
    elif HIDDEN_BOARD[row][column] == 'X':
        print('\nYou HIT!\n--------------------------------------')
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('\nYou MISS!\n--------------------------------------')
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print('\nCongratulations! You sunk all the battleships!\n')
        break  # Preventing the game to continue running
    if turns == 0:
        print('\nYou ran out of turns and the game is over...\n')
        break  # Preventing the game to continue running
