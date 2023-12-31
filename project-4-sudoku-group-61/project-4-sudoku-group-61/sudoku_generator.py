import math,random
import numpy as np
import pygame


"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/

"""

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for i in range(row_length)] for j in range(row_length)]
        self.box_length = int(math.sqrt(row_length))
 
        

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for row in self.board:
          print(row)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
      for i in range(self.row_length):
        if self.board[row][i] == num:
          return False
      return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    def valid_in_col(self, col, num):
        for i in range(self.row_length):
          col = int(col)
          if self.board[i][col] == num:
            return False
        return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
      box_row = row_start - row_start % self.box_length
      box_col = col_start - col_start % self.box_length
      for i in range(box_row, box_row + self.box_length):
          for j in range(box_col, box_col + self.box_length ):
              if self.board[i][j] == num:
                  return False
      return True
      
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num)

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    def fill_box(self, row_start, col_start):
        unused_nums = []
        for i in range(0, 10):
            if self.valid_in_box(row_start,col_start, i) == True:
                unused_nums.append(i)
        random.shuffle(unused_nums)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == 0:
                    self.board[i][j] = unused_nums.pop()
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)
          
    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        count = self.removed_cells
 
        while (count != 0):
            i = random.randint(0,8)
            j = random.randint(0,8)
            if (self.board[i][j] != 0):
                count -= 1
                self.board[i][j] = 0
            else:
                continue
        return

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

class cell:
  def __init__(self, value, row, col, screen, selected = False):
    self.value = value 
    self.row = row 
    self.col = col 
    self.screen = screen 
    self.sketched_value = 0 
    self.selected = selected
    '''
    Changes the value of the cell with a the new value.
    Parameters: the new value 
    Returns None  
    '''
  def set_cell_value(self, value):
    self.set_cell_value = value

    '''
    Changes the potential new value of the cell. 
    Parameters: the possible new value
    Returns None
    '''
  def set_sketched_value(self, value):
    self.set_sketched_value = value
    '''
    Computes the cells of the board in accordance to its dimensions and visuals. 
    '''

  def draw(self):
    rectleft = self.col * 60 + 120
    recttop = self.row * 60 + 50
    rectwidth = 60
    rectheight = 60
    if self.selected == True:
      pygame.draw.rect(self.screen,(255,0,0),(rectleft,recttop, rectwidth, rectheight),2)
    else:
      pygame.draw.rect(self.screen,(0,0,0),(rectleft,recttop, rectwidth, rectheight),2)
    if self.value != 0:
      font = pygame.font.SysFont("comicsansms",60)
      text = font.render(str(self.value),True, (0,0,0))
      self.screen.blit(text, (self.col * 60 + 60 / 2 - text.get_width() / 2+ 120, self.row * 60 + 60 /2 - text.get_height() / 2+ 50))
    if self.sketched_value != 0:
      font = pygame.font.SysFont("comicsansms",15)
      text = font.render(str(self.sketched_value), True,(0,0,0))
      self.screen.blit(text, (self.col * 60 + 60 / 2 - text.get_width() / 2+ 0, self.row * 60 + 60 / 2 - text.get_height() / 2+ 50))

'''
Initializes the variables needed to calculate the dimensions and different levels available. 
Parameters:
width and height - dimensions of board 
difficulty - 3 levels: easy, medium, and hard
'''      

class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen 
    self.difficulty = difficulty 
    '''
    The principal function for displaying the game board.
    Returns printed board
    '''
  def Print_Board(board):
    for i in range(9):
      for j in range(9):
        if j == 0:
            print("|", end='')
        if j != 8:
            print(board[i, j], end=' ')
        else:
            print(board[i, j], end='')
        if (j + 1) % 3 == 0:
            print("|", end='')
    if (i + 1) % 3 == 0:
        print("\n---------------------", end='')
    print()
    '''
    Searching if specific cell if available then returning the location to user. 
    Returns indexed location in board 
    '''
  def Find_Empty_Cell(self, board):
    res = []
    for i in range(9):
      for j in range(9):
        if board[i][j] == 0:
            row = i
            col = j
            res.append((row,col))

    return res 

  def Check_Validity(self, board):
    for i in range(0, len(board)):
            row_nums = board[i]
            repeat_set = set(row_nums)    
            if len(board[i]) == len(repeat_set):
                valid = True   
            else:
                return False
    for i in range(9):
        column_nums = []
        for j in range(0, len(board)):
            column_nums.append(board[j][i])
            repeat_set = set(column_nums)
            if len(column_nums) == len(repeat_set):
                valid = True
            else:
                return False
    column_of_threes = []
    for i in range(0,9):
        for j in range(0,3):
            column_of_threes.append(board[i][j])
            if len(column_of_threes) == 9:
                set_of_threes = set(column_of_threes)
                if len(column_of_threes) != len(set_of_threes):
                    return False
                else:
                    valid = True
                    column_of_threes = []
                    continue
    column_of_threes = []
    for i in range(0,9):
        for j in range(3,6):
            column_of_threes.append(board[i][j])
            if len(column_of_threes) == 9:
                set_of_threes = set(column_of_threes)
                if len(column_of_threes) != len(set_of_threes):
                    return False
                else:
                    valid = True
                    column_of_threes = []
                    continue
    column_of_threes = []
    for i in range(0,9):
        for j in range(6,9):
            column_of_threes.append(board[i][j])
            if len(column_of_threes) == 9:
                set_of_threes = set(column_of_threes)
                if len(column_of_threes) != len(set_of_threes):
                    return False
                else:
                    valid = True
                    column_of_threes = []
                    continue
    if valid == True:
        return True

    '''
    Allows user to reset cell value. 
    ''' 
  def Clear_Cell(self):
    for i in range(9):
      for j in range(9): 
        self.value == 0
        
  def draw(self, board, selected_x = 10, selected_y = 10):
    for i in range(0, len(board)):
        for l in range(0, len(board[i])):
            if i == selected_y and l == selected_x:
                if selected_x == 10 and selected_y == 10:
                    current_cell = cell(board[i][l], i, l, self.screen)
                else:
                    current_cell = cell(board[i][l], i, l, self.screen, True)
            else:
                current_cell = cell(board[i][l], i, l, self.screen)
            current_cell.draw()

                
    
  
