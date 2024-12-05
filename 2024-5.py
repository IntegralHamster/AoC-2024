with open('input.txt') as f:
    rules = [line.strip() for line in f.readlines()]
with open('input2.txt') as f:
    tests = [line.strip() for line in f.readlines()]

ans = 0
incorrect = []
for test in tests:
    pages = [int(x) for x in test.split(',')]
    flag = True
    for rule in rules:
        first, second = int(rule.split('|')[0]), int(rule.split('|')[1])
        if first in pages and second in pages and pages.index(second) <= pages.index(first):
            flag = False
            break
    if flag:
        ans += pages[(len(pages) - 1)//2]
    else:
        incorrect.append(pages)

print(ans)

order = {}
possible_pages = set()
for rule in rules:
    first, second = int(rule.split('|')[0]), int(rule.split('|')[1])
    if first not in order.keys():
        order[first] = [second]
    else:
        order[first].extend([second])
    possible_pages.add(first)
    possible_pages.add(second)

# Didn't work cause the input doesn't have one defined order, rude
# correct_order = []
# size = len(possible_pages)
# while len(correct_order) < size:
#     for page in possible_pages:
#         flag = True
#         for test in order.keys():
#             if page in order[test]:
#                 flag = False
#                 break
#         if flag:
#             correct_order.append(page)
#             possible_pages.remove(page)
#             order.pop(page)
#             break
#     if len(possible_pages) == 1:
#         correct_order.append(possible_pages.pop())

ans2 = 0
for fixing in incorrect:
    correct = []
    size = len(fixing)
    while len(correct) < size:
        for page in fixing:
            flag = True
            for check in fixing:
                if page in order[check]:
                    flag = False
                    break
            if flag:
                correct.append(page)
                fixing.remove(page)
                break
        if len(fixing) == 1:
            correct.append(fixing[0])
    ans2 += correct[(len(correct) - 1)//2]

print(ans2)











