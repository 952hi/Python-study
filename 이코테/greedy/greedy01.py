# 연습문제 3-1
# 화폐를 거슬러줄때 화폐사용량을 최소로하는 문제

# 입력예시 1260원 
n = 1260

curr = [500,100,50,10]
hap =0
for i in range(4):
    if n//curr[i] >= 1:
        a= n//curr[i]
        n= n- curr[i]*a
        hap = hap + a
print(hap)