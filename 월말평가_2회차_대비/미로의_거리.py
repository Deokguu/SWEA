def finding(arr, N):
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                return row, col
def destination(arr, N):
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 3:
                return row, col

def bfs(arr, si, sj, ei, ej, N):
    queue = []
    visited = [[0] * N for _ in range(N)]
    queue.append([si, sj])
    visited[si][sj] = 1

    while queue:
        ti, tj = queue.pop(0)

        for d in range(4):
            newR = ti + dr[d]
            newC = tj + dc[d]

            if 0<=newR<N and 0<=newC<N:
                if arr[newR][newC] != 1 and not visited[newR][newC]:
                    queue.append([newR, newC])
                    visited[newR][newC] = visited[ti][tj] + 1
    
    if visited[ei][ej] == 0:
        return 0
    else:
        return visited[ei][ej] - 2
    
    


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    si, sj = finding(arr, N)
    ei, ej = destination(arr, N)

    print(f'#{tc} {bfs(arr, si, sj, ei, ej, N)}')
