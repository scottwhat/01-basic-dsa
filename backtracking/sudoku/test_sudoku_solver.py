from sudoku_solver import SudokuSolver


def main():
    test = '..3.2.6..9..3.5..1..18.64....81.29..7..........67.82....26.95..8..2.3..9..5.1.3..'
    sol = '483921657967345821251876493548132976729564138136798245372689514814253769695417382'

    solver = SudokuSolver(test)
    print('Input:')
    solver.print_sudoku()

    assert solver.idx_to_row_col(2) == (0, 2)
    assert solver.get_kth_row(
        2) == ['.', '.', '1', '8', '.', '6', '4', '.', '.']
    assert solver.get_kth_col(
        8) == ['.', '1', '.', '.', '.', '.', '.', '9', '.']
    assert solver.get_grid_at_row_col(
        1, 1) == ['.', '.', '3', '9', '.', '.', '.', '.', '1']

    assert not solver.is_valid()

    solved = SudokuSolver(sol)
    assert solved.is_valid()

    print('Solution:')
    ret = solver.solve()
    assert ret == sol
    print(ret)


if __name__ == '__main__':
    main()
