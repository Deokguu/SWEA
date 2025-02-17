T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 배열크기 M 분사 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, -1, 1]
    max_v = 0

    for i in range(N):
        for j in range(N):
            sum_flies = arr[i][j]
            sum_cross = arr[i][j]
            for d in range(4): #네 방향
                for length in range(1, M):
                    newR = i + di[d] * length
                    newC = j + dj[d] * length

                    if 0<=newR<N and 0<=newC<N:
                        sum_flies += arr[newR][newC]
            if max_v < sum_flies:
                max_v = sum_flies

            for d in range(4, 8):  # 네 방향
                for length in range(1, M):
                    newR = i + di[d] * length
                    newC = j + dj[d] * length

                    if 0 <= newR < N and 0 <= newC < N:
                        sum_cross += arr[newR][newC]
            if max_v < sum_cross:
                max_v = sum_cross
    print(f'#{tc} {max_v}')