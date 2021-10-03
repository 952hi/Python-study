'''
징검다리 https://programmers.co.kr/learn/courses/30/lessons/43236

출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

제거한 바위의 위치	각 바위 사이의   거리	거리의 최솟값
[21, 17]	      [2, 9, 3, 11]	   2
[2, 21]	          [11, 3, 3, 8]    3
[2, 11]	          [14, 3, 4, 4]	   3
[11, 21]	      [2, 12, 3, 8]	   2
[2, 14]	          [11, 6, 4, 4]	   4
위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks,
제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

최소값은 징검다리에 돌이 겹쳐있는 경우는 없기 때문에 1이다. 최대 값은 시작지점과 도착지점사이의 거리인 distance이다. 
이 값을 기준으로 중간값(mid)가 n개의 돌을 제거했을 때 돌 사이의 거리중 최소값이라고 가정해보자.
이 가정하에 돌을 제거했을 때 이 값(mid)보다 작은 거리는 없어야 한다.
즉 돌 사이의 거리를 구했을 때 이 mid 값보다 작으면 제거하고 크면 두는 방식의 전략을 사용해야한다.

느낀점
이분탐색을 어디에 적용할지가 상당히 어렵게 느껴졌다
문제를 이해를 잘못해서 구글링을 참고했지만 그래도 이해가 잘안됐다.
'''

def solution(distance, rocks, n):
    answer = 0
    rocks.sort() 
    
    # 마지막 도착지와 거리계산하기위해 도착거리 추가
    rocks.append(distance)  
    
    # 최소는 0 최대는 도착지점까지의 거리 
    left, right = 0, distance  
    
    while left <= right:
        
        # 거리의 최솟값을 mid (거리가 mid 이하이면 삭제)
        mid = (left + right) // 2 
        
        # 각 mid 에서 최솟값 비교 변수
        min_distance = float('inf')  
        
        # 현재 위치
        current = 0  
        
        # 바위를 제거한 개수
        remove_cnt = 0  
        
        # 거리 재기 스타트
        for rock in rocks:
            
            # 바위와 현재 위치 사이의 거리
            diff = rock - current  
            
            # mid 보다 거리가 짧으면 바위 제거
            if diff < mid:  
                remove_cnt += 1
                
            # mid 보다 거리가 길거나 같으면 바위 그대로 두고
            else:  
                
                # 현재 위치를 그 바위로 옮기고
                current = rock  
                
                # 최소거리인지 체크
                min_distance = min(min_distance, diff)  
        
        # mid를 설정하는 단계
        # 바위를 너무 많이 제거한 경우mid를 줄여서 바위 제거개수 조정
        if remove_cnt > n:  
            right = mid - 1
            
        # 바위를 너무 적게 제거했거나 딱 맞을 경우. mid를 늘려서 가능한지 확인
        else:  
            answer = min_distance
            left = mid + 1

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))