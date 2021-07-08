input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0]))- int(ord('a')) +1
cal = 0

moves = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2)]
print(col)


for move in moves:
    nextR = row + move[0]
    nextC = col + move[1]
    if nextR>=1 and nextR <=8:
        if nextC >=1 and nextC <=8:
            cal = cal + 1
        
print(cal) 

