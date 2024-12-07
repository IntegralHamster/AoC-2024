with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

goal = []
numbers = []
for line in lines:
    left, right = line.split(': ')
    goal.append(int(left))
    numbers.append(right.split(' '))

import re

def line_combinations (num_inp):
    if len(num_inp) == 2:
        return [num_inp[0]+'+'+num_inp[1], num_inp[0]+'*'+num_inp[1], num_inp[0]+'~'+num_inp[1]]
    else:
        ans = []
        for option in line_combinations(num_inp[1:]):
            ans.append(num_inp[0] + '+' + option)
            ans.append(num_inp[0] + '*' + option)
            ans.append(num_inp[0] + '~' + option)
        return ans

def evaluate_line (expression):
    ans = int(expression[0])
    for i in range(len(expression)):
        if expression[i] == '+':
            ans += int(expression[i+1])
        if expression[i] == '*':
            ans *= int(expression[i+1])
        if expression[i] == '~':
            ans = int(str(ans) + expression[i + 1])
    return ans

part12 = 0
for i in range(len(goal)):
    for option in line_combinations(numbers[i]):
        if goal[i] == evaluate_line(re.split(r'(\W)', option)):
            part12 += goal[i]
            break

print(part12)

# for part 1 comment out the ~ parts in line_combinations. Expect runtime of around 30-40 seconds for part 2, faster for part 1
