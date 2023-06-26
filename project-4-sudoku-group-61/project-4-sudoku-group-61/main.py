from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku

def main():
    board = generate_sudoku(9, 30)
    for i in range(0, 9):
        print(board[i])
    
    


if __name__ == "__main__":
    main()