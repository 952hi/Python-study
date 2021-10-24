'''
별찍기 10 https://www.acmicpc.net/problem/2447

크기를 받아와 규칙에 맞는 별을 찍기

규칙 
크기 3일때 별
***
* *
***

입력예제 
27

27, 9 , 3 , 1
1 -> *
3 -> ***, * *, ***
9 -> *********, * ** ** *, *********, ***   ***. * *   * *, *********
27 -> * 3

#느낀점
규칙을 이해하는게 어려웠다
재귀는 항상 어려운것 같다...
'''
import sys 
sys.setrecursionlimit(10**6)

def append_star(LEN):
    
    if LEN == 1:
        return ['*']
    Stars = append_star(LEN//3)
    
    L = []
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)
    return L 

n = int(sys.stdin.readline().strip())

print("\n".join(append_star(n)))