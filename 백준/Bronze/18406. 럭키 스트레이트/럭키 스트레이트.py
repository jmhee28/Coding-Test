N = input()
n = len(N)//2
fs = 0
ss = 0
for i in range(n):
    fs += ord(N[i]) - ord('0')
for j in range(n, len(N)):
    ss += ord(N[j]) - ord('0')

if ss == fs:
    print('LUCKY')
else:
    print('READY')