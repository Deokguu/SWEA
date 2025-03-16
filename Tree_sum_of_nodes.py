def post_order(root_idx):
    global tree
    if root_idx <= N: #노드번호가 N을 넘지 않게
        post_order(root_idx*2) # 왼쪽 서브트리 방문
        post_order(root_idx*2+1) # 오른쪽쪽 서브트리 방문
        tree[root_idx] += tree[root_idx*2] + tree[root_idx*2+1]
    

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (3*N)
    for _ in range(M):
        node, num = map(int,input().split())
        tree[node] = num
    
    post_order(1)
    print(f"#{tc} {tree[L]}")
    # print(tree) 
