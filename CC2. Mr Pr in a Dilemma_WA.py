import sys

linenum = 1
for line in sys.stdin:
    
    if linenum == 1:
        numTestCases = int(line)
        if numTestCases >= 1 and numTestCases <= 10**5:
            pass
        else:
            break
    
    if linenum > 1:
        meet = 0
        tmp = str(line)
        a = int(tmp.split()[0])
        b = int(tmp.split()[1])
        c = int(tmp.split()[2])
        d = int(tmp.split()[3])
        divisior = max(c,d) - min(c,d)
        if (b - a) % divisior == 0:
            print('YES')
        else:
            print('NO')
            
    linenum = linenum + 1