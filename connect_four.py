def print_board(board) :
#This will take in the 2D character list for the board and print the board. 
    i = 1
    for row in board:
        for item in row:
            print(item, end = " ")
        print()

def initialize_board(num_rows, num_cols): 
#This will take in the num_row and num_cols from user input and this will set each spot in the list to “-”. A 2D character list with each spot set to be “-” will be returned. 
    board = [["-" for _ in range(num_cols)] for _ in range(num_rows)]
    return board
def insert_chip(board, col, chip_type, height) :
#This will take in the 2D character list for the board. This function places the token (‘x’ or ‘o’ denoted as ‘chip_type’) in the column that the user has chosen. Will find the next available spot in that column if there are already tokens there. The row that the token is placed in is returned. 
    for row in range(0, height):
            if board[row][col - 1] == "-":
                board[row - 1][col - 1] = chip_type
                return board
            else:
                board[row][col - 1] = chip_type
                return board
def check_if_winner(board, col, row, chip_type):
    return None
    
def main():
    board_height = int(input("What would you like the height of the board to be? "))
    board_length = int(input("What would you like the length of the board to be? "))
    connect_board = initialize_board(board_height,board_length)
    print_board(connect_board)
    player1_chip = input("Player 1: ")
    player2_chip = input("Player 2: ")
    game_active = True
    while game_active:
        chip_column = int(input("Player 1: Which column would you like to choose? "))
        connect_board = insert_chip(connect_board, chip_column, player1_chip, board_height)
        print_board(connect_board)
        chip_column = int(input("Player 2: Which column would you like to choose? "))
        connect_board = insert_chip(connect_board, chip_column, player2_chip, board_height)
        print_board(connect_board)
    
main()
    