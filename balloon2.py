T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    dc = [0, 1, 0, -1]
    dr= [1, 0, -1, 0]
    max_v = 0

    for i in range(N):
        for j in range(M):
            sum_v = arr[i][j]
            for d in range(4):
                newR = i + dr[d]
                newC = j + dc[d]


                if 0 <= newR < N and 0 <= newC < M:
                     sum_v += arr[newR][newC]

            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')



