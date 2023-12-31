from itertools import product


class SudokuSolver:
    """
    Solve a sudoku puzzle given as a 81-digit string with . denoting empty
    """

    SHAPE = 9
    GRID = 3
    EMPTY = '.'
    DIGITS = set([str(num) for num in range(1, SHAPE + 1)])

    def __init__(self, sudoku):
        # convert str into list for item assignment in guessing
        self.sudoku = list(sudoku)
        self.solved = None

    # main utility
    def solve(self):
        self.search()
        if self.solved:
            self.print_sudoku(self.solved)
            return ''.join(self.solved)
        else:
            print('Error: No solution found.')

    # helpers
    def idx_to_row_col(self, idx):
        row = idx // self.SHAPE
        col = idx % self.SHAPE
        return row, col

    def get_kth_row(self, k):
        return self.sudoku[self.SHAPE * k: self.SHAPE * k + self.SHAPE]

    def get_rows(self):
        return [
            self.sudoku[col: col + self.SHAPE]
            for col in range(0, self.SHAPE * self.SHAPE, self.SHAPE)
        ]

    def get_kth_col(self, k):
        return [self.sudoku[row * self.SHAPE + k] for row in range(self.SHAPE)]

    def get_cols(self):
        return [
            [self.sudoku[row * self.SHAPE + col] for row in range(self.SHAPE)]
            for col in range(self.SHAPE)
        ]

    def get_grid_at_row_col(self, row, col):
        row = row // self.GRID * self.GRID
        col = col // self.GRID * self.GRID
        return [
            self.sudoku[r * self.SHAPE + c] for r, c in
            product(range(row, row + self.GRID), range(col, col + self.GRID))
        ]

    def get_grids(self):
        return [
            [self.sudoku[r * self.SHAPE + c] for r, c in
             product(range(row, row + self.GRID), range(col, col + self.GRID))]
            for row in range(0, self.SHAPE, self.GRID)
            for col in range(0, self.SHAPE, self.GRID)
        ]

    def print_sudoku(self, sudoku=None):
        if sudoku is None:
            sudoku = self.sudoku
        rows = [
            sudoku[col: col + self.SHAPE]
            for col in range(0, self.SHAPE * self.SHAPE, self.SHAPE)
        ]
        print('\n'.join([' '.join(row) for row in rows]), end='\n\n')

    # backtracing algo helpers
    def is_valid(self):
        for row in self.get_rows():
            if not set(row) == self.DIGITS:
                return False
        for col in self.get_cols():
            if not set(col) == self.DIGITS:
                return False
        for grid in self.get_grids():
            if not set(grid) == self.DIGITS:
                return False
        return True

    def get_candidates(self, idx):
        row, col = self.idx_to_row_col(idx)
        used_digits = set()
        used_digits.update(self.get_kth_row(row))
        used_digits.update(self.get_kth_col(col))
        used_digits.update(self.get_grid_at_row_col(row, col))
        used_digits -= set([self.EMPTY])
        return self.DIGITS - used_digits

    def search(self):
        if self.solved:
            return
        if self.is_valid():
            self.solved = self.sudoku.copy()
            return
        if '.' in self.sudoku:  # still has empty spots for guessing
            fill_idx = self.sudoku.index('.')  # find the first empty spot
            for candidate in self.get_candidates(fill_idx):
                self.sudoku[fill_idx] = candidate
                self.search()  # recurse on sudoku with new guess
                self.sudoku[fill_idx] = '.'  # undo wrong guess
