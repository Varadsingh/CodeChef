import sys

def reverse(tmp1):
    for i in range(0,len(tmp1)):
        if tmp1[i] == 'T':
            tmp1[i] = 'H'
        elif tmp1[i] == 'H':
            tmp1[i] = 'T'
        else:
            tmp1[i] = tmp1[i]
    return(tmp1.copy())
            
        
linenum = 1
for line in sys.stdin:
    
    if linenum == 1:
        numTestCases = int(line)
        if numTestCases >= 1 and numTestCases <= 200:
            pass
        else:
            break
    
    if linenum > 1 and linenum <= (numTestCases*2)+1 and linenum % 2 == 0:
        tmp = str(line)
        length = int(tmp.split()[0])
        removal = int(tmp.split()[1])
        
    if linenum > 1 and linenum <= (numTestCases*2)+1 and linenum % 2 != 0:
        tmp = str(line)
        tmp = tmp.split(' ')
        if removal >= 1 and removal < length and length <= 100:
            while removal > 0:
                if tmp[len(tmp)-1] == 'H':
                    tmp = reverse(tmp.copy())
                tmp = tmp[0:len(tmp)-1]
                removal = removal - 1
            print(tmp.count('H'))
        else:
            break
    linenum = linenum + 1