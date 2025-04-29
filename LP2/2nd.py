import copy
from queue import PriorityQueue

def is_winner(board, player):
    return any([
        all([cell == player for cell in row]) for row in board
    ]) or any([
        all([board[r][c] == player for r in range(3)]) for c in range(3)
    ]) or all([
        board[i][i] == player for i in range(3)
    ]) or all([
        board[i][2 - i] == player for i in range(3)
    ])

def heuristic(board, player):
    return sum(row.count(player) for row in board)

def get_possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def make_move(board, i, j, player):
    new_board = copy.deepcopy(board)
    new_board[i][j] = player
    return new_board

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def get_clean_board():
    board = []
    print("Enter the board row by row using X, O, or E (for empty cells). Example: 'XOE' or 'XO E'")
    for i in range(3):
        while True:
            row = input(f"Row {i + 1}: ").strip().upper().replace(' ', '')
            if len(row) == 3 and all(c in ['X', 'O', 'E'] for c in row):
                board.append([' ' if c == 'E' else c for c in row])
                break
            else:
                print("❌ Please enter exactly 3 characters using X, O, or E only (e.g., 'XOE').")
    return board

def a_star_tictactoe(start_board, player):
    queue = PriorityQueue()
    queue.put((0, start_board))

    while not queue.empty():
        _, current = queue.get()

        if is_winner(current, player):
            return current

        for i, j in get_possible_moves(current):
            next_board = make_move(current, i, j, player)
            score = heuristic(next_board, player)
            queue.put((-score, next_board))  # maximize score

    return None

# Main
board = get_clean_board()
result = a_star_tictactoe(board, 'X')
print("\nBest possible board where 'X' might win:")
if result:
    print_board(result)
else:
    print("No winning path found for X.")




# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 2nd.py
# Enter the board row by row using X, O, or E (for empty cells). Example: 'XOE' or 'XO E'
# Row 1: xoe
# Row 2: oxe
# Row 3: eoe

# Best possible board where 'X' might win:
# X O
# O X
#   O X

# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 2nd.py
# Enter the board row by row using X, O, or E (for empty cells). Example: 'XOE' or 'XO E'
# Row 1: xox
# Row 2: oox
# Row 3: xoo

# Best possible board where 'X' might win:
# No winning path found for X.
# PS C:\Users\Asus\OneDrive\Desktop\LP2>