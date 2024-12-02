with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
def line_check(report):
    flag = 0
    for i in range(len(report) - 1):
        if 1 <= int(report[i+1]) - int(report[i]) <= 3:
            if flag == 0:
                flag = 1
            if flag < 0:
                return 0
            if flag > 0:
                continue
        elif -3 <= int(report[i+1]) - int(report[i]) <= -1:
            if flag == 0:
                flag = -1
            if flag > 0:
                return 0
            if flag < 0:
                continue
        else:
            return 0
    return 1

safe = []
for line in lines:
    report = line.split()
    safe.append(line_check(report))

safe2 = []
for j in range(len(lines)):
    if safe[j] == 1:
        safe2.append(1)
        continue
    else:
        found = 1
        report = lines[j].split()
        for k in range(len(report)):
            check_list = report.copy()
            del check_list[k]
            found = line_check(check_list)
            if found == 1:
                break
        if found == 1:
            safe2.append(1)
            continue
        else:
            safe2.append(0)

print(safe.count(1), safe2.count(1))
