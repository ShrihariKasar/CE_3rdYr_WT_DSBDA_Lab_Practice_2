class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = [['.' for _ in range(N)] for _ in range(N)]
    
    def print_solution(self):
        for row in self.board:
            print(" ".join(row))
        print("\n")
    
    def is_safe(self, row, col):
        # Check column
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False

        # Check left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        # Check right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, self.N)):
            if self.board[i][j] == 'Q':
                return False

        return True

    def solve_backtracking(self, row=0):
        # If all queens are placed, print the solution
        if row == self.N:
            self.print_solution()
            return True

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                if self.solve_backtracking(row + 1):
                    return True
                self.board[row][col] = '.'  # Backtrack

        return False  # No solution found for this configuration

    def solve_branch_bound(self):
        # We'll implement the Branch and Bound method with pruning
        result = self.branch_bound_helper(0, [], [], [], [])
        if result:
            self.print_solution()
        else:
            print("Solution does not exist.")

    def branch_bound_helper(self, row, cols, left_diags, right_diags, queens):
        if row == self.N:
            # All queens are placed successfully, print the solution
            self.print_solution_from_indices(queens)
            return True
        
        for col in range(self.N):
            # Check if the column or diagonals are already occupied
            if col in cols or (row - col) in left_diags or (row + col) in right_diags:
                continue

            # Place the queen and recursively solve for the next row
            cols.append(col)
            left_diags.append(row - col)
            right_diags.append(row + col)
            queens.append(col)

            if self.branch_bound_helper(row + 1, cols, left_diags, right_diags, queens):
                return True

            # Backtrack
            cols.remove(col)
            left_diags.remove(row - col)
            right_diags.remove(row + col)
            queens.pop()

        return False

    def print_solution_from_indices(self, queens):
        # Create an empty board
        self.board = [['.' for _ in range(self.N)] for _ in range(self.N)]
        for row, col in enumerate(queens):
            self.board[row][col] = 'Q'
        self.print_solution()

def main():
    N = int(input("Enter the number of queens: "))
    nq = NQueens(N)

    print("\nChoose the method to solve the N-Queens problem:")
    print("1. Backtracking")
    print("2. Branch and Bound")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("\nSolving using Backtracking...\n")
        nq.solve_backtracking()
    elif choice == '2':
        print("\nSolving using Branch and Bound...\n")
        nq.solve_branch_bound()
    else:
        print("Invalid choice.")

# Run the program
if __name__ == "__main__":
    main()




# OUTPUT:-
# PS C:\Users\Asus\OneDrive\Desktop\LP2> python 4th.py
# Enter the number of queens: 4

# Choose the method to solve the N-Queens problem:
# 1. Backtracking
# 2. Branch and Bound
# Enter your choice (1 or 2): 1

# Solving using Backtracking...

# . Q . .
# . . . Q
# Q . . .
# . . Q .


# PS C:\Users\Asus\OneDrive\Desktop\LP2> 