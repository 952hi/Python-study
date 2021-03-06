# 외벽 점검
# page 335
# https://programmers.co.kr/learn/courses/30/lessons/60062

# 원형의 길이 n
# 취약점의 배열 weak
# 친구들의 시간당 이동거리 배열 dist
# 위의 정보를 통해 보내야 하는 친구들의 최소의 숫자를 출력하기
# 
# 제한조건
# n은 1 이상 200 이하인 자연수입니다.
# weak의 길이는 1 이상 15 이하입니다.
# 서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
# 취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
# weak의 원소는 0 이상 n - 1 이하인 정수입니다.
# dist의 길이는 1 이상 8 이하입니다.
# dist의 원소는 1 이상 100 이하인 자연수입니다.
# 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.

# 문제설명
# 레스토랑을 운영하고 있는 "스카피"는 레스토랑 내부가 너무 낡아 친구들과 함께 직접 리모델링 하기로 했습니다. 
# 레스토랑이 있는 곳은 스노우타운으로 매우 추운 지역이어서 내부 공사를 하는 도중에 주기적으로 외벽의 상태를 점검해야 할 필요가 있습니다.
# 레스토랑의 구조는 완전히 동그란 모양이고 외벽의 총 둘레는 n미터이며, 외벽의 몇몇 지점은 추위가 심할 경우 손상될 수도 있는 취약한 지점들이 있습니다. 
# 따라서 내부 공사 도중에도 외벽의 취약 지점들이 손상되지 않았는 지, 주기적으로 친구들을 보내서 점검을 하기로 했습니다. 다만, 빠른 공사 진행을 위해 점검 시간을 1시간으로 제한했습니다. 
# 친구들이 1시간 동안 이동할 수 있는 거리는 제각각이기 때문에, 최소한의 친구들을 투입해 취약 지점을 점검하고 나머지 친구들은 내부 공사를 돕도록 하려고 합니다. 
# 편의 상 레스토랑의 정북 방향 지점을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타냅니다. 
# 또, 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동합니다. 
# 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때, 
# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return 하도록 solution 함수를 완성해주세요.




import itertools
import math

def solution(n, weak, dist):
    
    # 취약점 갯수
    weaksize = len(weak)
    
    # 0번째 위치 다음 취약점 위치를 더하여 계산을 용이하게함
    for i in weak:
        weak = weak + [n+i]

    
    # 최소값 비교를 위한  .inf 사용 
    mincheck = math.inf

    # 취약점 처음 부터 끝까지 비교
    for start in range(weaksize):

        # 모든 순서 수열을 만들기 위해 itertools의 permutation 사용
        # ex) 1234 1243 ... 4312 4321
        # 4321 일때는 4번째 취약점 부터 친구들 대입
        # permutations(리스트, 뽑아올수)

        for d in itertools.permutations(dist, len(dist)):
            
            cnt = 1
            pos = start

            for i in range(1, weaksize):
                nextpos = start + i
                diff = weak[nextpos] - weak[pos]

                # 차이값이 더 크면 다음 취약점에 도달하지못한것이기 떄문에
                # 첫번째 이동구간에서 다시 시작하는것이 아닌 다음 취약점부터 
                # 새로운 친구를 출동시킴
                if diff > d[cnt-1]:
                    pos = nextpos
                    cnt = cnt + 1
                    
                    # 처음받은 사람의 수보다 많이 필요하다면
                    # 그것은 한시간내에 해결할수 없다는 말이다
                    if cnt > len(dist):
                        break
            
            # 처음받은 사람의 수보다 작다면
            # 최솟값을 통해 데이터 업데이트
            if cnt <= len(dist):
                mincheck = min(mincheck, cnt)
                
    # mincheck가 무한대라면 주어진 친구들로 해결할 수 없는 상황
    if mincheck == math.inf:
        return -1
    
    return mincheck

# 느낀점
# DFS와 비슷한 면이 있다고 느꼈지만 그냥 처음부터 끝까지 반복이 아니라
# 각 경우마다 값이 다르기 때문에 1234와 
# itertools.permutations의 수열을 만드는 함수를 몰라 힘들었다