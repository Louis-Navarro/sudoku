import numpy as np


def find_number(grid, row, col, min):
    top = row // 3 * 3
    left = col // 3 * 3
    bottom = top + 3
    right = left + 3
    square = grid[top:bottom, left:right].reshape(9)
    for num in range(min, 10):
        if num not in (*grid[row], *grid[:, col], *square):
            return num

    return 0


def solve(grid):
    rows, cols = np.where(grid == 0)
    indexes = list(zip(rows, cols))

    i = 0
    while i < len(indexes):
        index = indexes[i]
        current_num = grid[index]
        num = find_number(grid, *index, current_num + 1)

        grid[index] = num

        i += 1 if num else -1

    return grid


def solve_animation(grid):
    rows, cols = np.where(grid == 0)
    indexes = list(zip(rows, cols))

    i = 0
    while i < len(indexes):
        row, col = indexes[i]
        current_num = grid[row, col]
        num = find_number(grid, row, col, current_num + 1)

        grid[row, col] = num

        i += 1 if num else -1

        yield (row, col, num)


if __name__ == "__main__":
    import general
    import colorama
    colorama.init()

    create = input('Do you want to input a grid ?\n').lower() == 'yes'

    if not create:
        initial_grid = general.create_grid()
        showed_grid = general.hide_grid(initial_grid.copy())
        resolved_grid = solve(showed_grid.copy())

    else:
        initial_grid = np.zeros((9, 9), int)

        for row in range(9):
            print(f'Enter numbers for row {row + 1}')

            numbers = list(input())
            initial_grid[row] = numbers

        resolved_grid = solve(initial_grid.copy())

    if 0 not in initial_grid:
        print(f'Initial grid:')
        general.print_grid(showed_grid, initial_grid)

        print(f'Showed grid:')
        general.print_grid(showed_grid, showed_grid)

        print(f'Resolved grid:')
        general.print_grid(showed_grid, resolved_grid)

    else:
        print(f'Showed grid:')
        general.print_grid(initial_grid, initial_grid)

        print(f'Resolved grid:')
        general.print_grid(initial_grid, resolved_grid)

    if general.check_grid(resolved_grid):
        print(f'Answer {colorama.Fore.GREEN}correct')

    else:
        print(f'Answer {colorama.Fore.RED}wrong')
