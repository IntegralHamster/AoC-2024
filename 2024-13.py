with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

ans1 = 0
ans2 = 0
for line in lines:
    if 'Button A' in line:
        line = (line.replace('X+','')).replace('Y+','')
        x1, y1 = line[9:].split(',')
        x1 = int(x1)
        y1 = int(y1)
    elif 'Button B' in line:
        line = (line.replace('X+','')).replace('Y+','')
        x2, y2 = line[9:].split(',')
        x2 = int(x2)
        y2 = int(y2)
    elif 'Prize' in line:
        line = (line.replace('X=', '')).replace('Y=', '')
        t1, t2 = line[7:].split(',')
        t1 = int(t1)
        t2 = int(t2)
        if (t1*y2 - t2*x2) % (x1*y2 - x2*y1) == 0:
            A = (t1*y2 - t2*x2) // (x1*y2 - x2*y1)
            if (t1 - x1*A) % x2 == 0:
                B = (t1 - x1*A) // x2
                if B >= 0 and A >= 0:
                    ans1 += 3*A + B
        t1 = 10000000000000+t1
        t2 = 10000000000000+t2
        if (t1*y2 - t2*x2) % (x1*y2 - x2*y1) == 0:
            A = (t1*y2 - t2*x2) // (x1*y2 - x2*y1)
            if (t1 - x1*A) % x2 == 0:
                B = (t1 - x1*A) // x2
                if B >= 0 and A >= 0:
                    ans2 += 3*A + B

print(ans1, ans2)


