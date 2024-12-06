with open('input.txt') as f:
    grid = [line.strip() for line in f.readlines()]

def turn(dir):
    if dir == [0, -1]:
        return [1, 0]
    if dir == [1, 0]:
        return [0, 1]
    if dir == [0, 1]:
        return [-1, 0]
    if dir == [-1, 0]:
        return [0, -1]

for i in range(len(grid)):
    if '^' in grid[i]:
        start_y = i
        start_x = grid[i].index('^')
        break

location1 = []
dir = [0, -1]
x = start_x
y = start_y
location1.append((x,y))
while True:
    if (0 <= y + dir[1] <= len(grid) - 1) and (0 <= x + dir[0] <= len(grid[0]) - 1):
        if grid[y + dir[1]][x + dir[0]] == '#':
            dir = turn(dir)
        else:
            x += dir[0]
            y += dir[1]
            location1.append((x,y))
    else:
        break

print(len(set(location1)))

def find_loop(grid,start_x,start_y):
    x = start_x
    y = start_y
    dir = [0, -1]
    location2 = []
    location2.append((x, y, dir[0], dir[1]))
    while True:
        if (0 <= y + dir[1] <= len(grid) - 1) and (0 <= x + dir[0] <= len(grid[0]) - 1):
            if grid[y + dir[1]][x + dir[0]] == '#':
                dir = turn(dir)
                location2.append((x, y, dir[0], dir[1]))
            else:
                x += dir[0]
                y += dir[1]
                if (x, y, dir[0], dir[1]) in location2:
                    return 1
                location2.append((x, y, dir[0], dir[1]))
        else:
            return 0

loop_statue = 0
for visited in set(location1):
    if visited != (start_x, start_y):
        grid[visited[1]] = grid[visited[1]][:visited[0]] + '#' + grid[visited[1]][visited[0] + 1:]
        loop_statue += find_loop(grid,start_x,start_y)
        grid[visited[1]] = grid[visited[1]][:visited[0]] + '.' + grid[visited[1]][visited[0] + 1:]

# expect runtime of couple of minutes
print(loop_statue)




