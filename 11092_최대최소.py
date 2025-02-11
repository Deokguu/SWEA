T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = 0
    max_idx = 0
    min_v = 10
    min_idx = 0

    for idx in range(N):
        if max_v <= arr[idx]:
            max_v = arr[idx]
            max_idx = idx
        
        if min_v > arr[idx]:
            min_v = arr[idx]
            min_idx = idx
    answer = abs(max_idx - min_idx)

    print(f'#{tc} {answer}')
        

    