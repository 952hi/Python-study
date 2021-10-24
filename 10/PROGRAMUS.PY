def solution(array, commands):
    answer = []
    a=[]
    b = 0
    for i in range(len(commands)):
        a= array[commands[i][0]-1:commands[i][1]]
        a.sort()
        b = commands[i][2] - 1
        answer.append(a[b])
        
    return answer
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))