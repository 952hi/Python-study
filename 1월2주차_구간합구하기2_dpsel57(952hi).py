'''
https://www.acmicpc.net/problem/10999
구간 합 구하기 2

어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째부터 4번째 수에 6을 더하면 1, 2, 9, 10, 5가 되고, 여기서 2번째부터 5번째까지 합을 구하라고 한다면 26을 출력하면 되는 것이다. 그리고 그 상태에서 1번째부터 3번째 수에 2를 빼고 2번째부터 5번째까지 합을 구하라고 한다면 22가 될 것이다.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 합을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c 또는 a, b, c, d가 주어지는데, a가 1인 경우 b번째 수부터 c번째 수에 d를 더하고, a가 2인 경우에는 b번째 수부터 c번째 수의 합을 구하여 출력하면 된다.
입력으로 주어지는 모든 수는 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 -263보다 크거나 같고, 263-1보다 작거나 같은 정수이다.

입력예시
5 2 2
1
2
3
4
5
1 3 4 6
2 2 5
1 1 3 -2
2 2 5

출력예시
26
22

느낀점
구글링을 통해 알고리즘을 이해하긴했지만
코드를 짜기에는 아직 부족한것 같습니다.
'''
import sys
import math
input = sys.stdin.readline


def get_tree_length():
    if N & (N-1) == 0:
        return 2*N
    else:
        return pow(2, math.ceil(math.log(N, 2)) + 1)


def initialize_segment_tree(index, start, end):
    if start == end:
        segment_tree[index] = nums[start]
        return

    mid = (start + end)//2
    initialize_segment_tree(index*2, start, mid)
    initialize_segment_tree(index*2+1, mid+1, end)
    segment_tree[index] = segment_tree[index*2] + segment_tree[index*2+1]
    
def update_segment_tree(index, start, end, left, right, to_added):
    propagate_segment_tree(index, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        segment_tree[index] += (end - start + 1)*to_added

        if start != end:
            lazy[index*2] += to_added
            lazy[index*2+1] += to_added

        return

    mid = (start + end)//2
    update_segment_tree(index*2, start, mid, left, right, to_added)
    update_segment_tree(index*2+1, mid+1, end, left, right, to_added)
    segment_tree[index] = segment_tree[index*2] + segment_tree[index*2+1]

def query_segment_tree(index, start, end, left, right):
    propagate_segment_tree(index, start, end)

    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return segment_tree[index]

    mid = (start + end)//2
    return query_segment_tree(index*2, start, mid, left, right) + query_segment_tree(index*2+1, mid+1, end, left, right)

def propagate_segment_tree(index, start, end):
    if lazy[index] != 0:
        segment_tree[index] += (end - start + 1)*lazy[index]

        if start != end:
            lazy[index*2] += lazy[index]
            lazy[index*2+1] += lazy[index]

        lazy[index] = 0

N, M, K = map(int, input().split())

nums = [-1] + [int(input()) for _ in range(N)]

tree_length = get_tree_length()
segment_tree = [0]*tree_length
lazy = [0]*tree_length
initialize_segment_tree(1, 1, N)

for _ in range(M+K):
    cur = list(map(int, input().split()))

    if cur[0] == 1:
        _, b, c, d = map(int, cur)
        update_segment_tree(1, 1, N, b, c, d)
        print(segment_tree)
        print(lazy)
    else:
        _, b, c = map(int, cur)
        print(query_segment_tree(1, 1, N, b, c))
        print(segment_tree)
        print(lazy)