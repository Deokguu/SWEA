dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

from collections import deque

def dijkstra():
    Q = deque()# (위치)
    distances = [[1e10] * N for _ in range(N)]

    Q.append((0,0))
    distances[0][0] = 0

    while Q:
        ti, tj = Q.popleft()

        for d in range(4):
            ni, nj = ti + dr[d], tj + dc[d]

            if 0<=ni<N and 0<=nj<N:
                diff = max(arr[ni][nj]-arr[ti][tj], 0) + 1
                if distances[ni][nj] > distances[ti][tj] + diff:
                    distances[ni][nj] = distances[ti][tj] + diff
                    Q.append((ni, nj))

    return distances[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra()

    print(f'#{tc} {result}')