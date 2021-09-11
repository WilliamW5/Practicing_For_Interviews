def mine_sweeper(bombs, num_rows, num_cols):
    # NOTE: field = [[0] * num_cols] * num_rows would not work
    # because you need to create a new list for every row,
    # instead of copying the same list.
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for bomb in bombs:
        (row_i, col_i) = bomb
        field[row_i][col_i] = -1
        for i in range(row_i - 1, row_i + 2):
            for j in range(col_i - 1, col_i + 2):
                if (0 <= i < num_rows and 0 <= j < num_cols
                        and field[i][j] != -1):
                    field[i][j] += 1
    return field

    

print(mine_sweeper([[0, 0], [0, 1]], 3, 4))