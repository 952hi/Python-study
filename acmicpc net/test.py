import math
def solution(n):
    if int(math.sqrt(n)) ** 2 == n :
        answer = int((math.sqrt(n)+1)) ** 2
    else:
        answer = -1
    return answer

print(solution(144))