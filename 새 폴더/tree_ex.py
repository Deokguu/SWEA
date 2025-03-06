'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T): #전위순회, 방문한 정점(부모) 먼저 처리
    if T: # 0이 아니면 (존재하는 정점이면)
        # visit(T) T에서 할 일 처리
        print(T)
        pre_order(left[T]) #왼쪽자식(서브트리)로 이동
        pre_order(right[T]) #오른쪼자식(서브트리)로 이동

def in_order(T): #전위순회, 방문한 정점(부모) 먼저 처리
    if T: # 0이 아니면 (존재하는 정점이면)
        # visit(T) T에서 할 일 처리
        in_order(left[T]) #왼쪽자식(서브트리)로 이동
        print(T)
        in_order(right[T]) #오른쪼자식(서브트리)로 이동

def post_order(T): #전위순회, 방문한 정점(부모) 먼저 처리
    if T: # 0이 아니면 (존재하는 정점이면)
        # visit(T) T에서 할 일 처리
        post_order(left[T]) #왼쪽자식(서브트리)로 이동
        post_order(right[T]) #오른쪼자식(서브트리)로 이동
        print(T)

#부모 인덱스로 자식번호 저장
N = int(input()) #1부터 N번까지인 정점
E = N - 1 # 간선 수
arr = list(map(int, input().split()))

left = [0] * (N+1) #부모를 인덱스로 왼쪽자식 저장
right = [0] * (N+1) #부모를 인덱스로 오른쪽자식 저장
parent = [0] * (N+1) # 자식을 인덱스로 부모 저장

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    parent[c] = p # 자식을 인덱스로 부모 저장
# for i in range(0, E*2, 2):
#     p, c = arr[i], arr[i+1]
    if left[p] == 0: #왼쪽자식이 아직 없으면
        left[p] = c
    else: #왼쪽자식이 있는 경우
        right[p] = c

print(left)
print(right)

root = 1
for i in range(1, N+1):
    if parent[i] == 0: # 부모 정점이 없으면 루트
        root = i
        break
pre_order(root)
# post_order(1)

c =N
while True:
    pass
