import copy

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def heuristic(board, player):
    if check_winner(board, 'O'):
        return 10
    elif check_winner(board, 'X'):
        return -10
    else:
        return 0

def a_star_move(board):
    best_score = float('-inf')
    best_move = None
    for move in get_empty_positions(board):
        new_board = copy.deepcopy(board)
        new_board[move[0]][move[1]] = 'O'
        score = heuristic(new_board, 'O')
        if score == 0:  # Evaluate future potential
            score -= distance_to_win(new_board, 'O')
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def distance_to_win(board, player):
    # Lower is better
    dist = 0
    for i in range(3):
        row = [board[i][j] for j in range(3)]
        col = [board[j][i] for j in range(3)]
        dist += (3 - row.count(player) - row.count('X' if player == 'O' else 'O'))
        dist += (3 - col.count(player) - col.count('X' if player == 'O' else 'O'))
    return dist

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe - You are X, Computer is O")
    print_board(board)

    while True:
        row = int(input("Enter your row (0-2): "))
        col = int(input("Enter your column (0-2): "))
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        print("Computer's move:")
        move = a_star_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("Computer wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()


# OUTPUT:
    
#     PS C:\Users\Asus\OneDrive\Desktop\LP2> python 2nd.py
# Tic Tac Toe - You are X, Computer is O
#   |   |  
# -----
#   |   |  
# -----
#   |   |  
# -----
# Enter your row (0-2): 0
# Enter your column (0-2): 0
# X |   |  
# -----
#   |   |
# -----
#   |   |
# -----
# Computer's move:
# X | O |
# -----
#   |   |
# -----
#   |   |
# -----
# Enter your row (0-2): 2
# Enter your column (0-2): 1
# X | O |  
# -----
#   |   |
# -----
#   | X |
# -----
# Computer's move:
# X | O | O
# -----
#   |   |
# -----
#   | X |
# -----
# Enter your row (0-2): 1
# Enter your column (0-2): 1
# X | O | O
# -----
#   | X |
# -----
#   | X |
# -----
# Computer's move:
# X | O | O
# -----
# O | X |
# -----
#   | X |
# -----
# Enter your row (0-2): 2
# Enter your column (0-2): 0
# X | O | O
# -----
# O | X |
# -----
# X | X |
# -----
# Computer's move:
# X | O | O
# -----
# O | X | O
# -----
# X | X |
# -----
# Enter your row (0-2): 2
# Enter your column (0-2): 2
# X | O | O
# -----
# O | X | O
# -----
# X | X | X
# -----
# You win!
# PS C:\Users\Asus\OneDrive\Desktop\LP2> 