def solution(id_list, report, k):
    answer = []
    reportCnt = {i:0 for i in id_list}
    reportInfo = {}
    
    for r in report:
        r = r.split()
        
        if r[0] in reportInfo:
            if r[1] not in reportInfo[r[0]]:
                reportInfo[r[0]].append(r[1])
                reportCnt[r[1]] += 1
        else:
            reportInfo[r[0]] = [r[1]]
            reportCnt[r[1]] += 1
    
    stop_list = set([ n for n, v in reportCnt.items() if v >= k ])
    
    
    return [len(set(reportInfo[j])&stop_list) if j in reportInfo else 0 for j in id_list]


# 더 간단히 고쳐보기... 근데 이 코드가 더 시간은 오래 걸린다...
def solution(id_list, report, k):
    reportCnt = {i:0 for i in id_list}
    answer = [0] * len(id_list)
    
    for r in set(report):
        a, b = r.split()
        reportCnt[b] += 1
    
    for r in set(report):
        a, b = r.split()
        if (reportCnt[b] >= k):
            answer[id_list.index(a)] += 1
    
    return answer