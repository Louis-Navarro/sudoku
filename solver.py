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
    print('Started')
    while i < len(indexes):
        index = indexes[i]
        current_num = grid[index]
        num = find_number(grid, *index, current_num + 1)

        grid[index] = num

        i += 1 if num else -1

    return grid


if __name__ == "__main__":
    import general
    import colorama
    colorama.init()

    initial_grid = general.create_grid()

    showed_grid = general.hide_grid(initial_grid.copy())

    resolved_grid = solve(showed_grid.copy())

    print(f'Initial grid: \n{initial_grid}')
    print(f'Showed grid: \n{showed_grid}')
    print(f'Resolved grid: \n{resolved_grid}')

    if general.check_grid(resolved_grid):
        print(f'Answer {colorama.Fore.GREEN}correct')

    else:
        print(f'Answer {colorama.Fore.RED}wrong')
