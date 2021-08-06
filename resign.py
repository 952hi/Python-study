# 퇴사
# 백준14501 page377

# 문제설명

# 퇴사하는 날 -> N+1
# N+1일에 퇴사하기위해 N일까지 최대한 상담을 진행합니다
# 진행할때 N일까지의 최대 상담금액을 출력하는 문제
# 
# time -> 상담에 필요한 일
# reward -> 상담완료 시 금액
# 입력예시값
# N = 7

# 1   2  3  4  5  6   7  
# 3   5  1  1  2  4   2
# 10 20 10 20 15 40 200

# 1일 상담을 진행하면 걸리는 시간이 3일 이기에 2,3일 상담 진행불가능
# 2일 상담을 진행하면 3,4,5,6일 상담 진행불가능
# N+1일이 8일에는 회사에 없기때문에 6,7일 상담 진행불가능

# 예시값에서 최대값은 1,4,5
# 1일의 상담금액은 1일상담금액 + 4일이후 상담금액 중 최대값
# 4일의 상담금액은 4일상담금액 + 5일이후 상담금액 중 최대값 이므로
# 앞의 값이 뒷값에 의존하기때문에 1일부터계산이 아닌 7일부터계산 



N = int(input())
time = []
reward = []
retire = [0]*(N+1)
comp = 0

for _ in range(N):
    x,y = map(int, input().split())
    time.append(x)
    reward.append(y)

# N이 7일때 7부터 시작 1 마무리
for i in range(N-1,-1,-1):

    # 7일이라면 상담필요시간 2일 + 7일 = 9일
    period = time[i]+i
    
    # 퇴사일전까지 상담이 완료가능한 경우 
    if period <= N:
        retire[i] = max(reward[i]+retire[period], comp)
        comp = retire[i]

    # 기간안에 처리 불가능한 경우 
    else:
        retire[i] = comp

print(comp)

# 느낀점
# 문제를 이해할때 수식을 종이 적으면서 구상하니 쉽게 작성할 수 있었다
#  