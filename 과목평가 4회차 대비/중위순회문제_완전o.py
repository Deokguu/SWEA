def in_order(root_idx):
    global word
    if root_idx <= N:
        in_order(root_idx*2)
        word += tree[root_idx]
        in_order(root_idx*2+1)

T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        arr = input().split()
        tree[int(arr[0])] = arr[1]
    word = ''
    in_order(1)
    print(f'#{tc} {word}') 

    '''
    tree가 이미 만들어져 주어진 경우
    '''

            
    


