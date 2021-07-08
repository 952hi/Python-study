# 임의의 정수 X를 1로 만들기


# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지다
# X가 5으로 나누어 떨어지면 5으로 나눈다.
# X가 3으로 나누어 떨어지면 3으로 나눈다.
# X가 2로 나누어 떨어지면 2로 나눈다.
# X에서 1을 뺀다

# 문제설명 
# 1<= X <= 30000
# 1 -> 0
# 2 -> 0
# 3 -> 1
# 4 -> 1
# 5 -> 2
#    ···
# 10 -> 2
# 16 -> ?
# f(n) = 1 + min( f(n/5) , f(n/3) , f(n/2) ,f(n-1) )

# 느낀점 아직까지는 고민을 하다보면 문제가 풀린다

def solve():
    x = int(input())
    arr = [0,0,1,1,2]
    for i in range(5, x+1):
        one = arr[i-1]
        two, three, four = 30001,30001,30001

        if i%5 == 0:
            two = arr[i//5]
        if i%3 == 0:
            three = arr[i//3]
        if i%2 == 0 :
            four =  arr[i//2]
        
        arr.append(1+min(one,two,three,four))

    print(arr[x])

solve()

