with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
def line_check(report):
    flag = 0
    unsafefl = 0
    for i in range(len(report) - 1):
        if 1 <= int(report[i+1]) - int(report[i]) <= 3:
            if flag == 0:
                flag = 1
            if flag < 0:
                unsafefl = 1
                break
            if flag > 0:
                continue
        elif -3 <= int(report[i+1]) - int(report[i]) <= -1:
            if flag == 0:
                flag = -1
            if flag > 0:
                unsafefl = 1
                break
            if flag < 0:
                continue
        else:
            unsafefl = 1
            break
    return unsafefl

safe = []
for line in lines:
    report = line.split()
    safe.append(1 - line_check(report))

safe2 = []
for j in range(len(lines)):
    if safe[j] == 1:
        safe2.append(1)
        continue
    else:
        found = 0
        report = lines[j].split()
        for k in range(len(report)):
            check_list = report.copy()
            del check_list[k]
            found = line_check(check_list)
            if found == 0:
                break
        if found == 0:
            safe2.append(1)
            continue
        else:
            safe2.append(0)

print(safe.count(1), safe2.count(1))