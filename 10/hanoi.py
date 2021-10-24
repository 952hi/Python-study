def solution(answers):
    answer = [0,0,0]
    score =[]
    m1 = [1,2,3,4,5]
    m2 = [2,1,2,3,2,4,2,5]
    m3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answer[i] == m1[i%len(m1)]: 
            answer[0] += 1
        if answer[i] == m2[i%len(m2)]: 
            answer[1] += 1
        if answer[i] == m3[i%len(m3)]: 
            answer[2] += 1
    
    k = max(a[0],a[1],a[2])
    if answer[0] == k:
        score.append(k)
    if answer[1] == k:
        score.append(k) 
    if answer[2] == k:
        score.append(k)
    score.sort()
    return score

print(solution([1,2,3,4,5]))