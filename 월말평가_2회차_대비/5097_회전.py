T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    arr = list(map(int, input().split()))

    for _ in range(M):
        if arr:
            t = arr.pop(0)
            arr.append(t)
    print(f'#{tc} {arr[0]}')