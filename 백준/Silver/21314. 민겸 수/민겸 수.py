s = input()
s = list(s)
n = len(s)

def getMax(s, n):
    ans =''
    idx = 0
    while idx < n :
        mcnt = 0
        if s[idx] == 'M':
            while idx < n and s[idx] == 'M':
                idx += 1
                mcnt += 1
            if idx < n and s[idx] == 'K':
                idx += 1
                x = 5 * (10 ** (mcnt))
                ans += str(x)
            elif idx == n and s[idx-1] == 'M':
                for i in range(mcnt):
                    ans += '1'
        else:
            ans += '5'
            idx += 1
    return ans
def getMin(s, n):
    ans = ''
    idx = 0
    
    while idx < n:
        mcnt = 0
        if s[idx] == 'M':
            while idx < n and s[idx] == 'M':
                idx += 1
                mcnt += 1
            ans += str(10 ** (mcnt-1))
        else:
            idx+=1
            ans += '5'
    return ans
print(getMax(s, n))
print(getMin(s, n))

