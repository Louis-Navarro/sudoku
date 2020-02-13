import random

import numpy as np
from colorama import Fore, init

init()

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RESET = Fore.RESET


def print_grid(hidden_grid, showed_grid):
    for i in range(81):
        row = i // 9
        col = i % 9

        index = (row, col)

        if hidden_grid[index] == 0:
            print(GREEN, showed_grid[index], end='')
        else:
            print(RED, showed_grid[index], end='')

        if col in (2, 5, 8):
            print(' ', end=' ')

        if row in (2, 5, 8) and col == 8:
            print()

        if col == 8:
            print(RESET)


def create_grid():
    grid = np.zeros((9, 9), int)
    grid[0, 0] = np.random.randint(1, 10)

    nums = list(range(1, 10))
    random.shuffle(nums)

    rows, cols = np.where(grid == 0)
    indexes = list(zip(rows, cols))

    i = 1
    while i <= len(indexes):
        index = indexes[i - 1]
        row, col = index

        current_num = grid[index]
        if current_num != 0:
            current_index = nums.index(current_num) + 1
        else:
            current_index = 0
        grid[index] = 0

        top = row // 3 * 3
        left = col // 3 * 3
        bottom = top + 3
        right = left + 3
        square = grid[top:bottom, left:right].reshape(9)

        for num in nums[current_index:]:
            if num not in (*grid[row], *grid[:, col], current_num, *square):
                grid[index] = num
                break

        i += 1 if grid[index] != 0 else -1

    return grid


def hide_grid(grid, percent=70):
    chance = np.random.randint(100, size=(9, 9))

    grid[chance < percent] = 0

    return grid


def check_grid(grid):
    if 0 in grid:
        return False

    transposed = grid.transpose()

    for i in range(9):
        if len(set(grid[i])) != 9:
            return False

        elif len(set(transposed[i])) != 9:
            return False

    combinations = [0, 3, 6, 9]

    for index1 in range(3):
        for index2 in range(3):
            row_min = combinations[index1]
            row_max = combinations[index1 + 1]

            col_min = combinations[index2]
            col_max = combinations[index2 + 1]

            square = grid[row_min:row_max, col_min:col_max].reshape(9)
            if len(set(square.tolist())) != 9:
                return False

    return True
