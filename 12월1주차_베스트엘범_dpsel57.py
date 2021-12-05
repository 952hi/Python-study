'''
https://programmers.co.kr/learn/courses/30/lessons/42579
베스트 앨범

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

입출력 예시
genres	
["classic", "pop", "classic", "classic", "pop"]	

plays	
[500, 600, 150, 800, 2500]

return
[4, 1, 3, 0]

느끼점
문제보고 딕셔너리를 사용해야겠다고 생각이 들긴했지만
딕셔너리가 익숙하지않아서 함수를 많이 찾아보면서 풀었습니다.
'''

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

answer = []

#장르별 재생횟수 리스트
playdigit = {}

#장르별 인덱스별 재생횟수 리스트
allplay = {}

for i in range(len(genres)):
    a = genres[i]
    b = plays[i]
    playdigit[a]= playdigit.get(a,0) + b
    allplay[a] = allplay.get(a,[]) + [(b, i)]

playdigit_sort = sorted(playdigit.items(), key = lambda x : x[1], reverse=True)

for (a,b) in playdigit_sort:
    
    # 장르별 재생횟수는 내림차순 인덱스는 오름차순
    allplay[a] = sorted(allplay[a], key = lambda x : (-x[0], x[1]))
    answer += [idx for (play, idx) in allplay[a][:2]]

print(answer)