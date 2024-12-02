with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

left = []
right = []
for line in lines:
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

dist = 0
similarity = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])
    similarity += left[i] * right.count(left[i])
print(dist, similarity)
