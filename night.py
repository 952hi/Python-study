# 왕실의 나이트

# 임의의 체스판에서 나이트가 이동할수있는 경우의수를 나타내라  
# 입력되는 값은 a1처럼 가로값은 알파벳a~h 세로값은 정수 1~8

# 느낀점 알파벳을 숫자로 바꾸는것이 생각이 나지않아 애를먹었다
# ord 잊지못할것같다

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

