import sys
input = sys.stdin.readline
s = input()

s_max = ''
s_min = ''
m = 0

for i in range(len(s)):
    if s[i] == 'M':
        m += 1
    elif s[i] == 'K':
        if m:
            s_max += str(5 * (10 ** m))
            s_min += str(10 ** m + 5)
        else:
            s_max += '5'
            s_min += '5'
        m = 0
if m:
    s_min += str(10 ** (m-1))
    while m:
        s_max += '1'
        m -= 1
print(s_max)
print(s_min)