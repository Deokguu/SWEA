def in_order(root_idx):
    global c
    if root_idx <= N: #노드번호가 N을 넘지 않게
        in_order(root_idx*2) # 왼쪽 서브트리 방문
        tree[root_idx] = c
        c += 1
        in_order(root_idx*2+1) # 오른족 서브트리 방문

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #완전이진트리 정점 수
    tree = [0] * (N+1)
    c = 1
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
    # N = 9  # 완전이진트리 정점 수
    # tree = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19]  # 정점번호를 인덱스로 하는 배열에 key값 저장
    # pre_order(1)