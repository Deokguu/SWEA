from collections import deque

def dijkstra():
    queue = deque()
    queue.append((0, 0))
    distances = [[10e10] * N for _ in range(N)]
    distances[0][0] = 0

    while queue:
        ti, tj = queue.popleft()

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = ti + dr, tj + dc

            if 0<=ni<N and 0<=nj<N:
                if distances[ni][nj] > distances[ti][tj] + arr[ni][nj]:
                    distances[ni][nj] = distances[ti][tj] + arr[ni][nj]
                    queue.append((ni, nj))
    return distances[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = dijkstra()
    print(f'#{tc} {result}')