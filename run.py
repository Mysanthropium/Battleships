#Legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot

from random import randint

"""
Board for holding the ship locations.
"""
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]

"""
Playing board to show hits and misses.
"""
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


"""
Defining the board row and columns, creating seperators through each iteration.
"""
def print_board(board):
    print('  A B C D E F G H')
    print('  -+-+-+-+-+-+-+-')
    row_number = 1
    for row in board:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1


"""
Define a function to let the computer create ships randomly over the board.
Check if X exists, or check X.
"""
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row] [ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row] [ship_column] = 'X'


"""
Ask the player where they want to place their battleships.
If not in a valid row or column, get error message to please enter a valid row and column.
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


create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('++++WELCOME TO BATTLESHIP++++\n\nGuess a battleship location to strike it!\n\nYou have 10 tries to get all 5 battleships\n')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row] [column] == '-':
        print("You've already guessed that")
    elif HIDDEN_BOARD[row] [column] == 'X':
        print('\nBOOM! You hit a battleship!')
        GUESS_BOARD[row] [column] = 'X'
        turns -= 1
    else:
        print('\nYou missed!')
        GUESS_BOARD[row] [column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print('Congratulations! You sunk all the battleships!')
        break
    print('You have ' + str(turns) + ' turns left!')
    if turns == 0:
        print('You ran out of turns and the game is over...')
        break




