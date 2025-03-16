def in_order(root_idx):
    global c
    if root_idx <= N:
        in_order(root_idx*2)
        tree[root_idx] = c
        c += 1
        in_order(root_idx*2 + 1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] *(N+1)
    c = 1
    in_order(1)
    
    print(f'#{tc} {tree[1]} {tree[N//2]}')

    '''
    내가 tree를 만들어야 하는 경우
    '''