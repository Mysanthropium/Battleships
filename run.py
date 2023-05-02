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


"""
Ask the player where they want to place their battleships.
If not in a valid row or column, get error message to please enter a valid row and column.
Convert the letters to numbers to pass it the correct column.
"""
def get_ship_location():
    row = input('Please enter a ship row 1-8')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-8')
    column = input('Please enter a ship column A-H').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter a ship column A-H').upper()
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
print_board(HIDDEN_BOARD)
print_board(GUESS_BOARD)
#while turns > 0:




