with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

import re
from math import gcd

quad1 = quad2 = quad3 = quad4 = 0
positions = []
velocities = []
width = 101
height = 103
for line in lines:
    variables = re.findall(r'-?\d+', line)
    x, y, vx, vy = variables
    positions.append((int(x),int(y)))
    velocities.append((int(vx),int(vy)))
    x_fin = (int(x) + 100 * int(vx)) % width
    y_fin = (int(y) + 100 * int(vy)) % height

    if 0 <= x_fin <= width // 2 - 1 and 0 <= y_fin <= height // 2 - 1:
        quad1 += 1
    elif width // 2 + 1 <= x_fin <= width - 1 and 0 <= y_fin <= height // 2 - 1:
        quad2 += 1
    elif 0 <= x_fin <= width // 2 - 1  and height // 2 + 1 <= y_fin <= height - 1:
        quad3 += 1
    elif width // 2 + 1 <= x_fin <= width - 1 and height // 2 + 1 <= y_fin <= height - 1:
        quad4 += 1

print(quad1*quad2*quad3*quad4)

time = 0
max_slopes = 999999999999
while True:
    slopes = set()
    time += 1
    new_positions = []
    for i in range(len(positions)):
        new_positions.append(((positions[i][0] + time*velocities[i][0]) % width, (positions[i][1] + time*velocities[i][1]) % height))
    for i in range(len(new_positions)):
        for j in range(len(new_positions)):
            if i != j:
                x1, y1, x2, y2 = new_positions[i][0], new_positions[i][1], new_positions[j][0], new_positions[j][1]
                if x2 - x1 == 0:
                    slopes.add((0, 1))
                elif y2 - y1 == 0:
                    slopes.add((0, 1))
                else:
                    d = gcd(y2 - y1, x2 - x1)
                    slopes.add(((x2 - x1)/d, (y2 - y1)/d))
    if len(slopes) <= max_slopes:
        max_slopes = len(slopes)
        print(time, max_slopes)
    if time % 50 == 0:
        print(time) # after all you want to know how slow it is

# settle down for runtime within 10+ min

