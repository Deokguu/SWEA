def pre_order(root_idx):
    global cnt
    if root_idx: # root_idx가 0이 아니면, 자식이 존재하면
        cnt += 1
        pre_order(left[root_idx])
        pre_order(right[root_idx])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    
    left = [0] * (V+1)
    right = [0] * (V+1)
    parent = [0] * (V+1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2 +1]
        parent[c] = p

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    pre_order(N)

    print(f'#{tc} {cnt}')

    '''
    tree를 만들 필요가 없는 경우
    '''