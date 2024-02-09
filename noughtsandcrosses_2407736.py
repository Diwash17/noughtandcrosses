'''
Name =  Diwash Adhikari 
Student ID = 2407736
CourseWorktask-2
Noughts and Crosses (Tic-Tac-Toe) Game
This program allows users to play the game of Noughts and Crosses (Tic-Tac-Toe)
against a computer opponent.
This game also includes features like saving scores to a leaderboard and displaying the leaderboard.
'''

import random
import os.path
import json
random.seed()

def draw_board(board):
    '''Draws the board for  Noughts and Crosses.
    '''
    print(" ", end="")
    print("-" * 11)
    for row in board:
        print("| ", end="")
        print(" | ".join(row), end="")
        print(" |")
        print(" ", end="")
        print("-" * 11)


def welcome(board):
    '''Prints the welcome message and displays the initial board.
    Args:
      board (list): The current state of the game board represented as a 3x3 list.
    '''
    print('\nWelcome to the "Unbeatable Noughts and Crosses" game.')
    print('The board layout is shown below:')
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want. \n")


def initialise_board(board):
    """Sets all elements of the board to one space ' '.
    Returns:
     list: The initialized game board.
    """
    for row_index in range(3):
        for column_index in range(3):
            board[row_index][column_index] = ' '
    return board


def get_player_move(board):
    """Asks the user for the cell to put 'X' in and returns row and col.
    Returns:
     tuple: The row and column indices where the player wants to place their mark ('X').
    """
    while True:
        try:
            move = int(input("\nChoose your square: (1, 2, 3), (4, 5, 6), (7, 8, 9)"))
            if 1 <= move <= 9:
                row = (move - 1) // 3
                col = (move - 1) % 3
                if board[row][col] == ' ':
                    return row, col
                print("Cell already occupied. Choose another cell.")
            else:
                print("Invalid input. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")



def choose_computer_move(board):
    """Lets the computer choose a cell to put 'O' in and returns row and col.
    Returns:
      tuple: The row and column indices where the computer wants to place their mark ('O').
    """
    while True:
        move = random.randint(1, 9)
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] == ' ':
            return row, col


def check_for_win(board, mark):
    """Checks if the player or the computer have won.
    Args:
     board (list): The current state of the game board represented as a 3x3 list.
     mark (str): The mark ('X' or 'O') to check for a win.
     Returns:
    bool: True if the specified mark has won, False otherwise.
    """

   # Define all the possible winning combinations (rows, columns, and diagonals)
    win_line_comination = [
        [(0, 0), (0, 1), (0, 2)], # Top row
        [(1, 0), (1, 1), (1, 2)], # Middle row
        [(2, 0), (2, 1), (2, 2)], # Bottom row
        [(0, 0), (1, 0), (2, 0)], # Left column
        [(0, 1), (1, 1), (2, 1)], # Middle column
        [(0, 2), (1, 2), (2, 2)], # Right column
        [(0, 0), (1, 1), (2, 2)], # Diagonal from top-left to bottom-right
        [(0, 2), (1, 1), (2, 0)]  # diagonal from  top-right to bottom-left
    ]

    for line in win_line_comination:
        if all(board[row_index][column_index] == mark for row_index, column_index in line):
            return True
    return False


def check_for_draw(board):
    """Checks if all cells are occupied and returns True if they are, False otherwise."""
    return all(cell != ' ' for row in board for cell in row)


def play_game(board):
    '''
    Plays the Noughts and Crosses (Tic-Tac_Toe) game.
    This function allows the player to play against the computer in a game of Noughts and Crosses.
    The game continues until one player wins or the board is full, resulting in a draw.
    Returns:
        1 if the player wins,
        -1 if the computer wins,
        0 if it's a draw.
    '''
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)

        if check_for_win(board, 'X'):
            print("You win!")
            return 1
        if check_for_draw(board):
            print("Draw!")
            return 0

        print("\nComputer's move: ")
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)

        if check_for_win(board, 'O'):
            print("Computer's win!")
            return -1
        if check_for_draw(board):
            print("Draw!")
            return 0



def menu():
    """Gets user input of '1', '2', '3', or 'q'."""  
    print("\nEnter one of the following options: ")
    print("     1 - Play the game")
    print("     2 - Save score in file 'leaderboard.txt'")
    print("     3 - Load and display the scores from 'leaderboard.txt'")
    print("     q - End the program")
    choice = input("1, 2, 3, or q? ").strip().lower()
    print()

    return choice
        

def load_scores():
    """Loads the leaderboard scores from the file 'leaderboard.txt' and 
    Returns:
     dict: The leaderboard scores loaded from the file.
    """
    leaders = {}
    try:
        if os.path.exists('leaderboard.txt'):
            with open('leaderboard.txt', 'r', encoding="utf-8") as file:
                leaders = json.load(file)
        else:
            print("Leaderboard file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON. Leaderboard file may be corrupted.")
    except FileNotFoundError:
        print("File 'leaderboard.txt' not found.")

    return leaders



def save_score(score):
    """Asks the player for their name and saves the current score to the file 'leaderboard.txt'.
    Args:
        score (int): The score to be saved.
    """
    name = input("Enter your name: ")
    leaders = load_scores()

    if not name.isalpha() or not str(score).strip('-').isdigit():
        print("Invalid input. Please enter a valid name and score.")
        return

    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score

    try:
        with open('leaderboard.txt', 'w', encoding="utf-8") as file:
            json.dump(leaders, file)
        print("Score saved successfully.")
    except FileNotFoundError:
        print("Leaderboard file not found.")
    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON: {json_error}. Leaderboard file may be corrupted.")



def display_leaderboard(leaders):
    """Displays the leaderboard scores passed in the Python dictionary parameter 'leaders'."""
    print("Leaderboard:")
    if not leaders:
        print("No scores available.")
    else:
        for name, score in leaders.items():
            print(f"{name}: {score}")
