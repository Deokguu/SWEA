T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    cnt = 0

    for j in range(N):
        if arr[0][j] != arr[1][j]:
            cnt += 1
            for d in range(N-j):
                newC = j + d
                if arr[0][newC] == 0:
                    arr[0][newC] = 1
                elif arr[0][newC] == 1:
                    arr[0][newC] = 0
        else:
            continue
    print(f'#{tc} {cnt}') 
