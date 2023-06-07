def solution(s, skip, index):
    answer = ""
    strs = list(s)
    skiplist = list(skip)
    limit = ord("z")
    for str in strs:
        alpha = ord(str)
        for i in range(index):
            while 1:
                alpha += 1
                if alpha <= limit and chr(alpha) not in skiplist:
                    break
                if alpha > limit:
                    alpha = ord("a")
                if chr(alpha) in skiplist:
                    alpha += 1
                if alpha <= limit and chr(alpha) not in skiplist:
                    break

            # if chr(alpha) in skiplist:
            #     alpha += 1
            #     if alpha > limit:
            #         alpha = ord("a")
        answer += chr(alpha)
    # print(answer)
    return answer