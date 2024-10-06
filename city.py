import sys

ROW_INDEX = 0
COLUMN_INDEX = 1
START_INDECIES = (2, 3)
MONEY_INDEX = 4
END_INDECIES = (5, 6)


def get_neighbour_cells(cell, grid_r, grid_c):
    """
    Returns neighbour cells (left, up, right, down) if found of the current cells from a grid
    :param cell: cell dimen
    :param grid_r: number of rows in a grid
    :param grid_c: number of columns in a grid
    :return: list of cell tuple that resemble r, c of a surrounding cell
    """
    row_cell, col_cell = cell
    neighbour_cells = []

    # Case: first row
    if row_cell == 0:
        # Case: first column (top-left corner)
        if col_cell == 0:
            if row_cell != grid_r - 1:  # if not last row
                neighbour_cells.append((row_cell + 1, col_cell))  # below
            if col_cell != grid_c - 1:  # if not last column
                neighbour_cells.append((row_cell, col_cell + 1))  # right

        # Case: last column (top-right corner)
        elif col_cell == grid_c - 1:
            if row_cell != grid_r - 1:  # if not last row
                neighbour_cells.append((row_cell + 1, col_cell))  # below
            neighbour_cells.append((row_cell, col_cell - 1))  # left

        # Case: middle columns (0 < col_cell < grid_c - 1)
        else:
            neighbour_cells.append((row_cell, col_cell - 1))  # left
            neighbour_cells.append((row_cell, col_cell + 1))  # right
            if row_cell != grid_r - 1:  # if not last row
                neighbour_cells.append((row_cell + 1, col_cell))  # below

    # Case: last row
    elif row_cell == grid_r - 1:
        # Case: first column (bottom-left corner)
        if col_cell == 0:
            neighbour_cells.append((row_cell - 1, col_cell))  # above
            if col_cell != grid_c - 1:  # if not last column
                neighbour_cells.append((row_cell, col_cell + 1))  # right

        # Case: last column (bottom-right corner)
        elif col_cell == grid_c - 1:
            neighbour_cells.append((row_cell - 1, col_cell))  # above
            neighbour_cells.append((row_cell, col_cell - 1))  # left

        # Case: middle columns (0 < col_cell < grid_c - 1)
        else:
            neighbour_cells.append((row_cell - 1, col_cell))  # above
            neighbour_cells.append((row_cell, col_cell - 1))  # left
            neighbour_cells.append((row_cell, col_cell + 1))  # right

    # Case: middle rows (1 <= row_cell <= grid_r - 2)
    else:
        # Case: first column (middle-left)
        if col_cell == 0:
            neighbour_cells.append((row_cell - 1, col_cell))  # above
            neighbour_cells.append((row_cell + 1, col_cell))  # below
            neighbour_cells.append((row_cell, col_cell + 1))  # right

        # Case: last column (middle-right)
        elif col_cell == grid_c - 1:
            neighbour_cells.append((row_cell - 1, col_cell))  # above
            neighbour_cells.append((row_cell + 1, col_cell))  # below
            neighbour_cells.append((row_cell, col_cell - 1))  # left

        # Case: middle columns
        else:
            neighbour_cells.append((row_cell - 1, col_cell))  # above
            neighbour_cells.append((row_cell + 1, col_cell))  # below
            neighbour_cells.append((row_cell, col_cell - 1))  # left
            neighbour_cells.append((row_cell, col_cell + 1))  # right

    return neighbour_cells


def get_neighbour_cells_improved_without_visited_cells(cell, grid_r, grid_c, visited_cells):
    row_cell, col_cell = cell
    neighbour_cells = []

    if row_cell > 0:  # Up
        to_be_appended_cell = (row_cell - 1, col_cell)
        if not visited_cells[to_be_appended_cell[0]][to_be_appended_cell[1]]:
            neighbour_cells.append(to_be_appended_cell)
    if row_cell < grid_r - 1:  # Down
        to_be_appended_cell = (row_cell + 1, col_cell)
        if not visited_cells[to_be_appended_cell[0]][to_be_appended_cell[1]]:
            neighbour_cells.append(to_be_appended_cell)
    if col_cell > 0:  # Left
        to_be_appended_cell = (row_cell, col_cell - 1)
        if not visited_cells[to_be_appended_cell[0]][to_be_appended_cell[1]]:
            neighbour_cells.append(to_be_appended_cell)
    if col_cell < grid_c - 1:  # Right
        to_be_appended_cell = (row_cell, col_cell + 1)
        if not visited_cells[to_be_appended_cell[0]][to_be_appended_cell[1]]:
            neighbour_cells.append(to_be_appended_cell)

    return neighbour_cells


def get_least_cell_value(current_value, cells, grid):
    min = -1
    new_cell = cells[0]
    for r, c in cells:
        if grid[r][c] + current_value < min:
            min = grid[r][c] + current_value
            new_cell = (r, c)
    return min, new_cell


def get_minimum_value_cell(cost_table, visited_cell):
    min = sys.maxsize
    min_cell = (-1, -1)
    for cell, value in cost_table.items():
        if not visited_cell[cell[0]][cell[1]] and value < min:
            min = value
            min_cell = cell


    return min_cell


def update_cells(src_value, cells, grid, cost_table):
    for row, col in cells:
        updated_value = grid[row][col] + src_value

        if updated_value < cost_table[(row, col)]:
            cost_table[(row, col)] = updated_value


def dijkstra(grid_info, grid):
    r = grid_info[ROW_INDEX]
    c = grid_info[COLUMN_INDEX]
    start_cell_indices = grid_info[START_INDECIES[0]] - 1, grid_info[START_INDECIES[1]] - 1
    money = grid_info[MONEY_INDEX]
    end_cell_indices = grid_info[END_INDECIES[0]], grid_info[END_INDECIES[1]]

    cost_table = {}

    visited_cells = [[False for _ in range(c)] for _ in range(r)]

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            cost_table[(row, column)] = sys.maxsize
    cost_table[start_cell_indices] = 0

    src = start_cell_indices
    src_value = 0
    # O(V^2)
    i = 0
    while i < (r * c)-1:
        visited_cells[src[0]][src[1]] = True

        cells = get_neighbour_cells_improved_without_visited_cells(src, r, c, visited_cells)

        update_cells(src_value, cells, grid, cost_table)

        src = get_minimum_value_cell(cost_table, visited_cells)
        src_value = cost_table[src]
        i += 1
    return cost_table


def test():
    grid_info = [3, 4, 1, 4, 500, 3, 4]
    grid = [
        [0, 100, 0, 200],
        [100, 0, 100, 300],
        [100, 100, 0, 50],
    ]

    print(dijkstra(grid_info, grid))


def run():
    while True:

        grid_info_str = input()
        if grid_info_str == "0 0 0 0 0 0 0":
            break

        grid_info = [int(num) for num in grid_info_str.strip().split()]

        grid = [[]] * grid_info[ROW_INDEX]

        for i in range(grid_info[ROW_INDEX]):
            row = [int(num) for num in input().strip().split()]
            grid[i] = row

        city(grid_info, grid)


test()
