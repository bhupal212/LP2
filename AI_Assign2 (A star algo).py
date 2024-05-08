#8 Puzzle Problem

from heapq import heappop, heappush
from copy import deepcopy

class PuzzleState:
    def __init__(self, board):
        self.board = board
        self.empty_pos = self.find_empty_position()

    def find_empty_position(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return (r, c)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))

    def __lt__(self, other):
        return False  # Placeholder for heap comparison

    def successors(self):
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        r, c = self.empty_pos
        for dr, dc in moves:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                new_board = deepcopy(self.board)
                new_board[r][c], new_board[new_r][new_c] = new_board[new_r][new_c], 0
                yield PuzzleState(new_board)

    def manhattan_distance(self, goal_state):
        distance = 0
        for r in range(3):
            for c in range(3):
                value = self.board[r][c]
                if value != 0:
                    goal_r, goal_c = goal_state.find_position(value)
                    distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    def find_position(self, value):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == value:
                    return (r, c)

def solve_8_puzzle(initial_board, goal_board):
    initial_state, goal_state = PuzzleState(initial_board), PuzzleState(goal_board)
    open_set, g, parent = [(initial_state.manhattan_distance(goal_state), initial_state)], {initial_state: 0}, {}

    while open_set:
        _, current = heappop(open_set)

        if current == goal_state:
            path = []
            while current:
                path.append(current.board)
                current = parent.get(current)
            return path[::-1]

        for next_state in current.successors():
            new_cost = g[current] + 1

            if next_state not in g or new_cost < g[next_state]:
                g[next_state] = new_cost
                f = new_cost + next_state.manhattan_distance(goal_state)
                heappush(open_set, (f, next_state))
                parent[next_state] = current

    return None

# Example usage
initial_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution_path = solve_8_puzzle(initial_board, goal_board)
if solution_path:
    print("Solution found! Steps:")
    for i, state in enumerate(solution_path):
        print(f"Step {i + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")





