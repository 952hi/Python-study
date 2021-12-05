'''
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
완주하지못한선수 문제
참여자와 완료자 리스트를 입력받아

완료하지못한 참여자 1명을 찾아 출력하는 문제
참여자와 완료자의 길이의 차이는 -> 1이다

'''

# 1차 시도 문제정답 but 효율성체크 탈락
# def solution(participant, completion):
#     for case in completion:
#         participant.remove(case)
#     return participant

# a = ["marina", "josipa", "nikola", "vinko", "filipa"]
# b = ["josipa", "filipa", "marina", "nikola"]

# solution(a,b)

# 2차시 성공
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for x,y in zip(participant,completion):
        if x != y:
            return x
    return participant.pop()

a = ["marina", "josipa", "nikola", "vinko", "filipa"]
b = ["josipa", "filipa", "marina", "nikola"]

print(solution(a,b))