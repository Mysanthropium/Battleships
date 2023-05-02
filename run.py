from random import randint

HIDDEN_BOARD = [[''] * for x in range(8)]
GUESS_BOARD = [[''] * for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

"""
Define the board visuals, creating seperators through each iteration.
"""
def print_board(board):
    print('   A B C D E F G H')
    print('   +-+-+-+-+-+-+-+')
    row_number = 1
    for row in board():
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

def get_ship_location():
    pass

def count_hit_ships():
    pass

create_ships()
turns = 10
#while turns > 0:



