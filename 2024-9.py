with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

data = []
non_empty_data = []
data_count = 0
for i in range(len(lines[0])):
    if i % 2 == 0:
        for k in range(int(lines[0][i])):
            data.append(data_count)
        data_count += 1
        non_empty_data.append(int(lines[0][i]))
    else:
        if int(lines[0][i]) != 0:
            for k in range(int(lines[0][i])):
                data.append('.')

# Part 1 solution
# left = 0
# right = len(data) - 1
# while right > left:
#     if data[left] != '.':
#         left += 1
#     else:
#         if data[right] == '.':
#             while data[right] == '.':
#                 right -= 1
#         if right <= left:
#             break
#         data[left] = data[right]
#         data[right] = '.'
#         left += 1
#         right -= 1

# Part 2 solution
def search_empty(array, length):
    needed_space = ['.' for j in range(length)]
    for k in range(len(array) - length):
        if array[k:k+length] == needed_space:
            return k
    return -1

def replace(array, element):
    flag = False
    for m in range(len(array)-1, 1, -1):
        if array[m] == element:
            array[m] = '.'
            flag = True
        elif flag:
            return array

for i in range(len(non_empty_data)-1, 1, -1):
    search = search_empty(data, non_empty_data[i])
    if search != -1 and search <= data.index(i):
        data = replace(data,i)
        for l in range(search, search + non_empty_data[i]):
            data[l] = i

ans = 0
for i in range(len(data)):
    if data[i] != '.':
        ans += data[i]*i
print(ans)