def hanoi(N, start, to, via):
    
    if N == 1:
        print(start, to)
    else:
        hanoi(N-1, start, via, to)
        print(start, to)
        hanoi(N-1, via, to, start)
    

N = int(input())

print(2**N-1)
hanoi(N, 1, 3, 2)

