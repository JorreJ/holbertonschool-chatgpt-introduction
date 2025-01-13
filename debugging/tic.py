#!/usr/bin/python3
def print_board(board):
    """
    Prints the Tic-Tac-Toe board in a user-friendly format.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * (len(board[0]) * 4 - 1))  # Dynamic line length for board width

def check_winner(board):
    """
    Checks if there is a winner in the current board state.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    """
    Checks if the game has ended in a draw.

    Returns:
        bool: True if all cells are filled and there is no winner, False otherwise.
    """
    for row in board:
        if " " in row:  # If any empty cell is found, it's not a draw
            return False
    return True

def tic_tac_toe():
    """
    Runs the Tic-Tac-Toe game.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize a 3x3 empty board
    current_player = "X"

    while True:
        print_board(board)
        try:
            # Get the player's move
            row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))

            # Validate input range
            if row < 0 or row >= 3 or col < 0 or col >= 3:
                print("Invalid input! Row and column must be 0, 1, or 2. Try again.")
                continue

            # Check if the chosen cell is empty
            if board[row][col] == " ":
                board[row][col] = current_player  # Place the player's mark

                # Check for a winner
                if check_winner(board):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break

                # Check for a draw
                if is_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break

                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter numeric values for row and column.")
        except IndexError:
            print("Invalid input! Row and column must be 0, 1, or 2. Try again.")

if __name__ == "__main__":
    tic_tac_toe()