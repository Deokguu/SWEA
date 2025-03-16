def enque(n):
    global last
    last += 1 #마지막 정점 증가
    tree[last] = n #마지막 정점에 값 넣기
    
    child = last #부모랑 값 비교 하기 위해
    parent = child // 2 

    while parent > 0 and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0
    for i in arr:
        enque(i)
    sum_ancestor = 0

    while last >0:
        last = last // 2
        sum_ancestor += tree[last]
    
    print(f'#{tc} {sum_ancestor}')

    '''
    내가 트리를 만들어야 하는 경우
    최소힙에 맞춰서
    '''