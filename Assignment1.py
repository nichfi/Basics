filename = "C:/Users/nicko/Downloads/test1.txt"

with open(filename, 'r') as f:
    # read the first line containing the width and height
    width, height = map(int, f.readline().strip().split(','))

    # initialize the 2D grid with 'H' characters
    grid = [['H' for _ in range(width)] for _ in range(height)]

    # read the remaining lines containing selected positions
    for line in f:
        x, y = map(int, line.strip().split(','))
        grid[y][x] = ' '  # replace 'H' with empty space at the selected position

    # print the grid
    for row in grid:
        print(' '.join(row))

