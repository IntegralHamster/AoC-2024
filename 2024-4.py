with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def look_nw(grid,x,y):
    if x <= 2 or y <= 2:
        return 0
    elif grid[x-1][y-1] == 'M' and grid[x-2][y-2] == 'A' and grid[x-3][y-3] == 'S':
        return 1
    else:
        return 0

def look_n(grid,x,y):
    if y <= 2:
        return 0
    elif grid[x][y-1] == 'M' and grid[x][y-2] == 'A' and grid[x][y-3] == 'S':
        return 1
    else:
        return 0

def look_ne(grid,x,y):
    if x > len(grid) - 4 or y <= 2:
        return 0
    elif grid[x+1][y-1] == 'M' and grid[x+2][y-2] == 'A' and grid[x+3][y-3] == 'S':
        return 1
    else:
        return 0

def look_sw(grid, x, y):
    if x <= 2 or y > len(grid[0]) - 4:
        return 0
    elif grid[x - 1][y + 1] == 'M' and grid[x - 2][y + 2] == 'A' and grid[x - 3][y + 3] == 'S':
        return 1
    else:
        return 0

def look_s(grid, x, y):
    if y > len(grid[0]) - 4:
        return 0
    elif grid[x][y + 1] == 'M' and grid[x][y + 2] == 'A' and grid[x][y + 3] == 'S':
        return 1
    else:
        return 0

def look_se(grid, x, y):
    if x > len(grid) - 4 or y > len(grid[0]) - 4:
        return 0
    elif grid[x + 1][y + 1] == 'M' and grid[x + 2][y + 2] == 'A' and grid[x + 3][y + 3] == 'S':
        return 1
    else:
        return 0

def look_w(grid, x, y):
    if x <= 2:
        return 0
    elif grid[x - 1][y] == 'M' and grid[x-2][y] == 'A' and grid[x-3][y] == 'S':
        return 1
    else:
        return 0

def look_e(grid, x, y):
    if x > len(grid) - 4:
        return 0
    elif grid[x + 1][y] == 'M' and grid[x + 2][y] == 'A' and grid[x + 3][y] == 'S':
        return 1
    else:
        return 0

def look_cross(grid,x,y):
    if grid[x+1][y+1] == grid[x+1][y-1] == 'M' and grid[x-1][y-1] == grid[x-1][y+1] == 'S':
        return 1
    elif grid[x+1][y+1] == grid[x+1][y-1] == 'S' and grid[x-1][y-1] == grid[x-1][y+1] == 'M':
        return 1
    elif grid[x+1][y+1] == grid[x-1][y+1] == 'M' and grid[x-1][y-1] == grid[x+1][y-1] == 'S':
        return 1
    elif grid[x+1][y+1] == grid[x-1][y+1] == 'S' and grid[x-1][y-1] == grid[x+1][y-1] == 'M':
        return 1
    else:
        return 0

xmas_count = 0
x_mas_count = 0
for j in range(len(lines)):
    for i in range(len(lines[0])):
        if lines[j][i] == 'X':
            xmas_count += look_nw(lines, j, i) + look_ne(lines, j, i) + look_n(lines, j, i) + look_e(lines, j, i) + look_w(lines, j, i) + look_sw(lines, j, i) + look_se(lines, j, i) + look_s(lines, j, i)
        if lines[j][i] == 'A' and 1 <= j <= len(lines) - 2 and 1 <= i <= len(lines[j]) - 2:
            x_mas_count += look_cross(lines,j,i)

print(xmas_count, x_mas_count)