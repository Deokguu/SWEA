def score(arr, N, M):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_v = 0
    for row in range(N):
        for col in range(M):
            total = arr[row][col]

            for d in range(4):
                newR = row + dr[d]
                newC = col + dc[d]

                if 0<=newR<N and 0<=newC<M:
                    total += arr[newR][newC]
            if max_v < total:
                max_v = total
    return max_v
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행 M열
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {score(arr, N, M)}')
