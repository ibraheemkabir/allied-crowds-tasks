def maximum_adjacent_product_in_matrix(grid):
    grid_length = len(grid)

    product = 0
    maximum = 0

    for i in range(0, grid_length):
        for j in range(0, grid_length-3):
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]

            if product > maximum:
                maximum = product
            
    for i in range(0, grid_length):
        for j in range(0, grid_length-3):
            product = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i]

            if product > maximum:
                maximum = product

    for i in range(0, grid_length-3):
        for j in range(0, grid_length-3):
            product = grid[j][i] * grid[j+1][i+1] * grid[j+2][i+2] * grid[j+3][i+3]

            if product > maximum:
                maximum = product

    for i in range(0, grid_length-3):
        for j in range(3, grid_length):
            product = grid[j][i] * grid[j-1][i+1] * grid[j-2][i+2] * grid[j-3][i+3]
            
            if product > maximum:
                maximum = product

    return maximum
