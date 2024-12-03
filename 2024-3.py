with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

import re
search = re.findall(r"(mul\([0-9]+,[0-9]+\))",lines[0])
ans = 0
for found in search:
    digits = re.findall(r"([0-9]+)", found)
    ans += int(digits[0])*int(digits[1])

search2 = re.findall(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))", lines[0])
flag = 1
ans2 = 0
for found in search2:
    if found[1] != '':
        flag = 1
    elif found[2] != '':
        flag = 0
    else:
        digits = re.findall(r"([0-9]+)", found[0])
        ans2 += int(digits[0]) * int(digits[1]) * flag
print(ans,ans2)