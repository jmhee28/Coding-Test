infolist = []
querylist = []
dict = {}
n = 0
def solution(info, query):
    global n
    answer = [] 
    n = len(info)
    for i in info:
        parsed = i.split(" ")
        score = int(parsed[-1])
        parsed[-1] = score
        infolist.append(parsed)
    infolist.sort(key = lambda x: x[-1])
    makeDict()
    makeGroup()
    for key, val in dict.items():
        val.sort(key = lambda x: x[-1])
        
    for q in query:
        parsed = [word for word in q.split(" ") if word != "and"]
        cnt = qCnt(parsed)
        answer.append(cnt)
    return answer

def makeDict():
    langs = ["cpp", "java", "python", "-"]
    jobs = ["backend", "frontend", "-"]
    exps = ["junior", "senior", "-"]
    sfoods = ["chicken", "pizza", "-"]
    
    for lang in langs:
        for job in jobs:
            for exp in exps:
                for food in sfoods:
                    key = (lang, job, exp, food)
                    val = []
                    dict[key] = val
def makeGroup():
    global n
    for info in infolist:
        clang, cjob, cexp, cfood = info[:4]
        key = ['-', '-', '-', '-']
        langs = [clang, '-']
        jobs = [cjob, '-']
        exps = [cexp, '-']
        foods = [cfood, '-']
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        key = (langs[a], jobs[b], exps[c], foods[d])
                        dict[key].append(info)


def bsearch(target, query):
    arr = dict[query]
    arrlen = len(arr)
    start = 0
    end = arrlen - 1
    while start <= end: 
        mid = (start + end) // 2
        score = arr[mid][-1]
        if  score == target:
            temp = arrlen - mid
            for m in range(mid-1, -1, -1):
                tscore = arr[m][-1]
                if tscore < target:
                    break
                else:
                    temp+= 1
                    
            return temp
        elif score > target:
            end = mid - 1
        else:
            start = mid + 1
    result = arrlen - start        
    return result

def qCnt(parsed):
    global n
    result = 0 
    score = int(parsed[-1])
    lang, job, exp, food = parsed[:4]
    query = (lang, job, exp, food)
    result = bsearch(score, query)
    return result
    