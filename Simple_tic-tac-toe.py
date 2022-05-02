def is_finished(grid):
    """Returns the tic-tac-toe game state of the given grid"""
    if 'X' in row_of_three(grid) or 'X' in column_of_three(grid):
        return 'X wins'
    elif 'O' in row_of_three(grid) or 'O' in column_of_three(grid):
        return 'O wins'
    elif diag_of_three(grid):
        return diag_of_three(grid) + ' wins'
    elif are_there_blanks(grid):
        return 'Game not finished'
    else:
        return 'Draw'


def column_of_three(grid):
    """Takes a 3x3 grid, and returns a list indicating which shape (if any)
    completely fills the column corresponding to the element's list index"""
    column_winners = []
    for j in range(3):
        column = []
        for k in range(3):
            column.append(grid[k][j])

        x_wins = all([play == 'X' for play in column])
        o_wins = all([play == 'O' for play in column])

        if x_wins:
            column_winners.append('X')
        elif o_wins:
            column_winners.append('O')
        else:
            pass

    return column_winners


def row_of_three(grid):
    """Takes a 3x3 grid, and returns a list indicating which shape (if any)
        completely fills the row corresponding to the element's list index"""
    row_winners = []
    for k in range(3):
        row = []
        for j in range(3):
            row.append(grid[k][j])

        x_wins = all([play == 'X' for play in row])
        o_wins = all([play == 'O' for play in row])

        if x_wins:
            row_winners.append('X')
        elif o_wins:
            row_winners.append('O')
        else:
            pass

    return row_winners


def diag_of_three(grid):
    """Takes a 3x3 grid and returns the shape (if any) that completely fills either of the grid's diagonals"""
    main = []
    second = []
    for k in range(3):
        main.append(grid[k][k])
        second.append(grid[k][2 - k])

    if all([play == 'X' for play in main]) or all([play == 'O' for play in main]):
        return main[0]
    elif all([play == 'X' for play in second]) or all([play == 'O' for play in second]):
        return second[0]
    else:
        pass


def are_there_blanks(grid):
    """Boolean - determines if there are any open spaces left in the given grid"""
    for row in grid:
        for move in row:
            if move == ' ':
                return True
            else:
                pass


def count_x(moves):
    """Counts the number of Xs on the grid"""
    x_count = 0
    for move in moves:
        if move == 'X':
            x_count += 1
        else:
            pass

    return x_count


def count_o(moves):
    """Counts the number of Os on the grid"""
    o_count = 0
    for move in moves:
        if move == 'O':
            o_count += 1

    return o_count


def print_matrix(grid):
    print(f"""---------
| {grid[0][0]} {grid[0][1]} {grid[0][2]} |
| {grid[1][0]} {grid[1][1]} {grid[1][2]} |
| {grid[2][0]} {grid[2][1]} {grid[2][2]} |
---------""")


def create_matrix():
    state = input("Enter cells: ")
    cells = [play if play != '_' else ' ' for play in state]

    grid = [
        [cells[0], cells[1], cells[2]],
        [cells[3], cells[4], cells[5]],
        [cells[6], cells[7], cells[8]]
            ]

    return grid


def update_matrix(coordinates):
    """Updates the matrix with the player's move"""
    global matrix
    global i
    if i % 2 == 0:
        matrix[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'X'
    else:
        matrix[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'O'


def get_move():
    """Gets the grid location (in form [row, column] where the player wants to play an 'X'"""
    location = input("Enter the coordinates: ").split()
    return location


def analyze_move(location):
    global matrix
    row = int(location[0]) - 1
    column = int(location[1]) - 1
    if any([row > 2, column > 2]):
        return "Coordinates should be from 1 to 3!"
    elif any([str(row).isnumeric() is False, str(column).isnumeric() is False]):
        return "You should enter numbers!"
    elif matrix[row][column] != ' ':
        return "This cell is occupied! Choose another one!"
    else:
        return ''


def game_loop():
    global i
    global matrix
    coordinates = get_move()
    if analyze_move(coordinates):
        return game_loop()
    else:
        update_matrix(coordinates)
        print_matrix(matrix)
        i += 1

    state = is_finished(matrix)

    if 'wins' in state or state == 'Draw':
        print(state)
        return
    else:
        return game_loop()


i = 0
matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_matrix(matrix)

game_loop()
