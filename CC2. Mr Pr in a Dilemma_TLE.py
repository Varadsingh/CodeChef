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
        prevdiff = 0
        while a <= b:
            if a == b:
                meet = 1
                break
            if a+max(c,d) <= b+min(c,d):
                a = a + max(c,d)
                b = b + min(c,d)
                diff = b - a
            elif a+min(c,d) <= b+max(c,d):
                a = a + min(c,d)
                b = b + max(c,d)
                diff = b - a
            else:
                meet = 0
                break
            
            if diff > prevdiff and prevdiff != 0:
                meet = 0
                break
            else:
                prevdiff = diff
                
        if meet == 1:
            print('YES')
        else:
            print('NO')
            
    linenum = linenum + 1