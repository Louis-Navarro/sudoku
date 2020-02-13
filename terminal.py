from colorama import Fore, init

import general
import solver

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


def main():
    initial_grid = general.create_grid()
    hidden_grid = general.hide_grid(initial_grid.copy())
    showed_grid = hidden_grid.copy()
    solved = solver.solve(hidden_grid.copy())

    while not general.check_grid(showed_grid):
        print_grid(hidden_grid, showed_grid)
        print(f'{RED}RED {RESET}= Immutable')
        print(f'{GREEN}GREEN {RESET}= Mutable')
        print(f'{BLUE}Row 0 {RESET}= Solution')

        row = int(input('What row do you want to change : ')) - 1

        if row == -1:
            print(f'You abandoned, the computer found :')
            print_grid(hidden_grid, solved)
            break

        col = int(input('What column do you want to change : ')) - 1
        index = (row, col)

        if hidden_grid[index] != 0:
            print('Immutable number !')
            continue

        num = int(input('Enter the number to put : '))
        showed_grid[index] = num

    if general.check_grid(showed_grid):
        print('Well done !')
        print_grid(hidden_grid, showed_grid)
        print('This is what the computer found :')
        print_grid(hidden_grid, solved)


if __name__ == "__main__":
    main()
