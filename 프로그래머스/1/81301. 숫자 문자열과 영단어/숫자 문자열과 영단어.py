vocas = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
answer = ''
def solution(s):
    global answer
    solve(s)
    return int(answer)

def solve(val):
    global answer
    if len(val) == 0:
        return
    if '0' <= val[0] <= '9':
        answer += val[0]
        val = val[1:]
    else:
        for i in range(10):
            if val.startswith(vocas[i]):
                val = val[len(vocas[i]):]
                answer+= str(i)
    solve(val)