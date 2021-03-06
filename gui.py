import pygame as pg

import general
import solver

pg.init()

#############
# VARIABLES #
#############

# Window

win_side = 506
win = pg.display.set_mode((win_side, win_side))
pg.display.set_caption('Sudoku')

# Grid

initial_grid = general.create_grid()
hidden_grid = general.hide_grid(initial_grid.copy(), 80)
modified_grid = hidden_grid.copy()
solution = solver.solve_animation(hidden_grid.copy())

current_case = (-1, -1)

show_solution = False

#############
# FUNCTIONS #
#############


def check_click():
    global current_case, modified_grid, show_solution, solution

    clicks = pg.mouse.get_pressed()
    if clicks[0]:
        x, y = pg.mouse.get_pos()

        row = int(y / win_side * 9)
        col = int(x / win_side * 9)

        if hidden_grid[row, col] == 0:
            current_case = row, col

    keys = pg.key.get_pressed()

    if not show_solution:
        if keys[pg.K_LCTRL] & keys[pg.K_SPACE]:
            show_solution = True

        elif keys[pg.K_KP1] & (current_case != (-1, -1)):
            modified_grid[current_case] = 1

        elif keys[pg.K_KP2] & (current_case != (-1, -1)):
            modified_grid[current_case] = 2

        elif keys[pg.K_KP3] & (current_case != (-1, -1)):
            modified_grid[current_case] = 3

        elif keys[pg.K_KP4] & (current_case != (-1, -1)):
            modified_grid[current_case] = 4

        elif keys[pg.K_KP5] & (current_case != (-1, -1)):
            modified_grid[current_case] = 5

        elif keys[pg.K_KP6] & (current_case != (-1, -1)):
            modified_grid[current_case] = 6

        elif keys[pg.K_KP7] & (current_case != (-1, -1)):
            modified_grid[current_case] = 7

        elif keys[pg.K_KP8] & (current_case != (-1, -1)):
            modified_grid[current_case] = 8

        elif keys[pg.K_KP9] & (current_case != (-1, -1)):
            modified_grid[current_case] = 9

        elif keys[pg.K_DELETE] or keys[pg.K_BACKSPACE]:
            modified_grid[current_case] = 0
            current_case = (-1, -1)

        if any(keys[pg.K_KP1:pg.K_KP9 + 1]):
            current_case = (-1, -1)

    else:
        try:
            row, col, num = next(solution)
            modified_grid[row, col] = num
        except StopIteration:
            solution = solver.solve_animation(hidden_grid.copy())
            show_solution = False


def draw_window():
    win.fill((255, 255, 255))

    for i in range(1, 9):
        if not i % 3:
            pg.draw.line(win, (0, 0, 0), (56 * i, 0), (56 * i, win_side), 3)
            pg.draw.line(win, (0, 0, 0), (0, 56 * i), (win_side, 56 * i), 3)
        else:
            pg.draw.line(win, (0, 0, 0), (56 * i, 0), (56 * i, win_side), 1)
            pg.draw.line(win, (0, 0, 0), (0, 56 * i), (win_side, 56 * i), 1)

    for row in range(9):
        for col in range(9):
            num = str(modified_grid[row, col])
            init_num = hidden_grid[row, col]

            if init_num:
                text = font.render(num, True, (255, 0, 0))

                x = col * 56 + text.get_width() * 2
                y = row * 56 + text.get_height() / 2

                win.blit(text, (x, y))

            elif num != '0':
                text = font.render(num, True, (0, 255, 0))

                x = col * 56 + text.get_width() * 2
                y = row * 56 + text.get_height() / 2

                win.blit(text, (x, y))

    if current_case != (-1, -1):
        row = current_case[0]
        col = current_case[1]

        top = row * 56
        left = col * 56

        pg.draw.rect(win, (0, 0, 255), (left, top, 56, 56), 5)

    pg.display.flip()


#############
# MAIN LOOP #
#############

font = pg.font.SysFont('sourcecodepro', 20)

clock = pg.time.Clock()
run = True

while run:
    # clock.tick(60)

    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    check_click()
    draw_window()

pg.quit()
