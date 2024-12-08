with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

antennas = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] != '.':
            if lines[y][x] not in antennas.keys():
                antennas[lines[y][x]] = [(x,y)]
            else:
                antennas[lines[y][x]].extend([(x,y)])


def possible_overlaps (antenna_array, limit_x, limit_y):
    overlaps = []
    for i in range(len(antenna_array)-1):
        for j in range(i+1,len(antenna_array)):
            ant_dist = [antenna_array[i][0] - antenna_array[j][0], antenna_array[i][1] - antenna_array[j][1]]
            if 0 <= antenna_array[i][0] + ant_dist[0] <= limit_x and 0 <= antenna_array[i][1] + ant_dist[1] <= limit_y:
                overlaps.append((antenna_array[i][0] + ant_dist[0], antenna_array[i][1] + ant_dist[1]))
            if 0 <= antenna_array[j][0] - ant_dist[0] <= limit_x and 0 <= antenna_array[j][1] - ant_dist[1] <= limit_y:
                overlaps.append((antenna_array[j][0] - ant_dist[0], antenna_array[j][1] - ant_dist[1]))
    return overlaps

def possible_overlaps2 (antenna_array, limit_x, limit_y):
    overlaps = []
    for i in range(len(antenna_array)-1):
        for j in range(i+1,len(antenna_array)):
            ant_dist = [antenna_array[i][0] - antenna_array[j][0], antenna_array[i][1] - antenna_array[j][1]]
            dist_mul = 0
            plus_fl = minus_fl = False
            while True:
                if 0 <= antenna_array[i][0] + dist_mul*ant_dist[0] <= limit_x and 0 <= antenna_array[i][1] + dist_mul*ant_dist[1] <= limit_y:
                    overlaps.append((antenna_array[i][0] + dist_mul*ant_dist[0], antenna_array[i][1] + dist_mul*ant_dist[1]))
                else:
                    plus_fl = True
                if 0 <= antenna_array[i][0] - dist_mul*ant_dist[0] <= limit_x and 0 <= antenna_array[i][1] - dist_mul*ant_dist[1] <= limit_y:
                    overlaps.append((antenna_array[i][0] - dist_mul*ant_dist[0], antenna_array[i][1] - dist_mul*ant_dist[1]))
                else:
                    minus_fl = True
                if plus_fl and minus_fl:
                    break
                else:
                    dist_mul += 1
    return overlaps

x = len(lines[0])-1
y = len(lines)-1

part1 = []
part2 = []
for key in antennas.keys():
    part1.extend(possible_overlaps(antennas[key],x,y))
    part2.extend(possible_overlaps2(antennas[key], x, y))
print(len(set(part1)))
print(len(set(part2)))

