'''
https://programmers.co.kr/learn/courses/30/lessons/42628
이중우선순위 큐
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때,
모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

입력예시
["I 7","I 5","I -5","D -1"]
출력예시
[7,5]

느낀점
파이썬 힙 라이브러리의 힙은 최소힙을 기준으로 하는데
최대값을 제거할수있는 heapq.nlargest의 함수르 알게되었다
heapq.nlargest의 함수는 최대값을 리스트형태로 반환해줘서 끝에 [0]을 붙여 값만 추출해서 사용했습니다.
'''
# 큐를 사용하지않는방법
# operations = ["I 7","I 5","I -5","D -1"]
# answer = []

# for i in operations:
#     a,b = i.split()
    
#     if a == "I":
#         answer.append(int(b))
    
#     answer.sort()
        
#     if a == "D":
#         if len(answer) == 0:
#             continue
#         elif int(b) > 0 :
#             answer.pop()
#         else:
#             answer.pop(0)

# if len(answer) == 0:
#     answer = [0,0]
# else:
#     answer = [max(answer),min(answer)]

# print(answer)

#큐를 사용하는방법
import heapq

def solution(operations):
    answer = []
    min_heap = []
    for i in operations:
        a,b = i.split()
    
        if a == "I":
            heapq.heappush(min_heap, int(b))
    
        if len(min_heap) != 0 :
            if a == "D":
                if int(b) > 0:
                    min_heap.pop(min_heap.index(heapq.nlargest(1, min_heap)[0]))
                else:
                    heapq.heappop(min_heap)
        
    if min_heap:
        answer = [heapq.nlargest(1, min_heap)[0],heapq.heappop(min_heap)]
    else:
        answer = [0,0]
          
    return answer

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))


    
