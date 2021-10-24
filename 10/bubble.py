'''
# 1회차 
# 시간초과 3% 
def swap(a,b):
    a , b = b , a
    return a,b

n = int(input())
sort = list(map(int, input().split()))
cnt = 0

for i in range(n-1,-1,-1):
    for j in range(i):
        if sort[j] > sort[j+1]:
            swap(sort[j], sort[j+1])
            cnt += 1
print(cnt)
'''

'''
# 2회차 
# 시간초과 3%

n = int(input())
sort = list(map(int, input().split()))
cnt = 0

for i in range(n-1,-1,-1):
    for j in range(i):
        if sort[j] > sort[j+1]:
            sort[j] , sort[j+1] = sort[j+1], sort[j]
            cnt += 1

print(cnt)
'''

'''
# 3회차
# 시간초과 7프로
n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n - 1, 0, -1):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                cnt += 1
        if not swapped:
            break
print(cnt)
'''
'''
# 4회차
# 시간초과 7프로
n = int(input())
arr = list(map(int, input().split()))
cnt = 0

end = n-1
while end > 0:
    last_swap = 0
    for i in range(end):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            last_swap = i
            cnt += 1
    end = last_swap
print(cnt)
'''
'''
https://www.acmicpc.net/problem/1517
버블소트

정렬 중 스왑이 일어나는 횟수를 출력하기

'''

def mergeSort(start, end):
    global cnt
    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)

        a = start
        b = mid + 1
        tmp = []
        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                tmp.append(arr[a])
                a += 1

            else:
                tmp.append(arr[b])
                b += 1
                cnt += (mid - a + 1)
                  
        
            

        for i in range(len(tmp)):
            arr[start + i] = tmp[i]


cnt = 0
n = int(input())
arr = list(map(int, input().split()))
mergeSort(0, n-1)
print(cnt)