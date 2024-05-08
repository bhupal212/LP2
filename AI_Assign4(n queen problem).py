# N-Queen Problem

class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        return all(board[r] != col and abs(r - row) != abs(board[r] - col) for r in range(row))

    def backtrack(self, board, row):
        if row == self.n:
            self.solutions.append(board[:])
        else:
            for col in range(self.n):
                if self.is_safe(board, row, col):
                    board[row] = col
                    self.backtrack(board, row + 1)
                    board[row] = -1

    def solve(self):
        self.backtrack([-1] * self.n, 0)

        if not self.solutions:
            print(f"No solutions exist for {self.n}-queens problem.")
            return False

        print(f"Found {len(self.solutions)} solution(s) for {self.n}-queens problem:")
        for idx, solution in enumerate(self.solutions):
            print(f"Solution {idx + 1}:")
            for row in range(self.n):
                line = ["Q" if col == solution[row] else "." for col in range(self.n)]
                print(" ".join(line))
            print()

        return True

    
if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    solver = NQueens(n)
    solver.solve()




