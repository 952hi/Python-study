'''
백준 1991 https://www.acmicpc.net/problem/1991
트리순회
진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성

첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
자식 노드가 없는 경우에는 .으로 표현한다.

입력 예시
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

느낀점
일차원리스트로 해결하려고하니 매우복잡 했다.
딕셔너리로 입력받아 처리하니 쉽게 해결할 수 있었다.
'''
def preO(node):
    if node == '.':
        return
    print(node,end="")
    preO(tree[node][0])
    preO(tree[node][1])

def inO(node):
    if node == '.':
        return
    inO(tree[node][0])
    print(node,end="")
    inO(tree[node][1])
    
def postO(node):
    if node == '.':
        return
    postO(tree[node][0])
    postO(tree[node][1])
    print(node,end="")

N = int(input())
tree = {}

for _ in range(N):
    root, left,right = input().split()
    tree[root] = (left,right)
    
preO("A")
print()
inO("A")
print()
postO("A")


