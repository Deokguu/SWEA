T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    max_v = 0
    min_v = 10e10
    for i in range(N):
        for j in range(N):
            sum_v = arr[i][j]
            for d in range(4):
                for length in range(1, N):
                    newR = i + dr[d] * length
                    newC = j + dc[d] * length
                    if 0<=newR<N and 0<=newC<N:
                        sum_v += arr[newR][newC]
            if max_v < sum_v:
                max_v = sum_v

            if min_v > sum_v:
                min_v = sum_v
    print(f'#{tc} {max_v - min_v}')



