import heapq

q = []

heapq.heappush(q, (1,2,3))
a,b,c = heapq.heappop(q)
print(a,b,c)