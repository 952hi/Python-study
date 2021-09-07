'''
page 180 성적이 낮은 순서로 학생 출력하기
이름과 성적을 입력받아 성적이 낮은순으로 한줄에 출력하는 문제

느낀점
이차원배열에서 sort()함수를 사용할때는 첫번째 원소 [한글][55] , [55][한글] 앞원소 기준 정렬
'''
student = int(input())

grade = []

for j in range(student):
    a,b = input().split()
    grade.append((int(b),a))


grade.sort()

for i in range(student):
    print(grade[i][1],end=" ")


