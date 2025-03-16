def post_order(root_idx):
    if root_idx <= N:
        post_order(root_idx*2)
        post_order(root_idx*2+1)
        tree[root_idx] += tree[root_idx*2] + tree[root_idx*2+1]



T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N*N)
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    post_order(1)
    print(f'#{tc} {tree[L]}')
    '''
    tree의 일부분이 만들어져 있고,
    내가 만들어서 완성시켜야 하는 경우
    '''

