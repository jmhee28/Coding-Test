def solution(id_list, report, k):
    answer = []
    idDict = {}
    reporteeDict = {}
    reportCnt = {}
    mailCnt = {}
    for id in id_list:
        idDict[id] = []
        reporteeDict[id] = []
        reportCnt[id] = 0
        mailCnt[id] = 0
    for i in range(len(report)):
        curReport = report[i].split()
        reporter = curReport[0]
        reportee = curReport[1]
        if reportee not in idDict[reporter]:
            reporteeDict[reportee].append(reporter)
            idDict[reporter].append(reportee)
            reportCnt[reportee] += 1
            
    for key, val in reportCnt.items():
        if val >= k:
            for r in reporteeDict[key]:
                mailCnt[r] += 1
                
    for id in id_list:
        c = mailCnt[id]
        answer.append(c)
    return answer