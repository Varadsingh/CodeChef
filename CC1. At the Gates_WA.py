import sys

def onesNtwos(n):
    global ones, twos
    ones = 0
    twos = 0
    while n > 0:
        ones = ones*10 + 1
        twos = twos*10 + 2
        n = n - 1

def revCoins(n):
    n = n + ones
    n = twos - n
    return(n)

def removeCoin(n):
    n = int(n/10)
    return(n)

def genNum():
    global num
    num = 0
    for i in range(1,length+1):
        if tmp.split()[i-1] == 'H':
            num = num + (10**(length-i))
        if tmp.split()[i-1] == 'T':
            num = num
def headcount():
    global hcount,num
    hcount = 0      
    while int(num/10) > 0:
        if num%10 == 1:
            hcount = hcount + 1
        num = int(num/10)
    if num == 1:
        hcount = hcount + 1

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
        onesNtwos(length)
        removal = int(tmp.split()[1])
        if removal >= 1 and removal < length and length <= 100:
            pass
        else:
            break
    
    if linenum > 1 and linenum <= (numTestCases*2)+1 and linenum % 2 != 0:
        tmp = str(line)
        genNum()
        while removal > 0:
            if num%10 == 1:
                num = revCoins(num)
                num = removeCoin(num)
            else:
                num = removeCoin(num)
            length = length - 1
            removal = removal - 1
            onesNtwos(length)
        headcount()
        print(hcount)
    linenum = linenum + 1