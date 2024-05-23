def print_board(board):
    """Function to print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) for num in row))

def find_empty_location(board):
    """Function to find an empty location on the board (marked by 0)."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_safe(board, row, col, num):
    """Function to check if placing num in board[row][col] is valid."""
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    """Function to solve the Sudoku board using backtracking."""
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # No empty location means the board is solved
    row, col = empty_location

    for num in range(1, 10):  # Try numbers 1 to 9
        if is_safe(board, row, col, num):
            board[row][col] = num  # Tentatively place num

            if solve_sudoku(board):
                return True  # Continue solving with this placement

            board[row][col] = 0  # Reset (backtrack) if num doesn't lead to a solution

    return False  # Trigger backtracking

# Example usage
if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku before solved successfully:")
    print_board(board)
    
    if solve_sudoku(board):
        print("Sudoku solved successfully:")
        print_board(board)
    else:
        print("No solution exists")
