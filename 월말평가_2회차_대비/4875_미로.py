dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find_s(arr, N):
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 2:
                return row, col
    return -1, -1

def dfs(maze, N, si, sj):
    if si == -1 and sj == -1:
        return 'error'
    stack = []
    visited = [[False] * N for _ in range(N)]
    stack.append((si, sj))
    visited[si][sj] = True

    while stack:
        ti, tj = stack.pop()
        if maze[ti][tj] == 3:
            return 1
        
        for d in range(4):
            ni = ti + dr[d]
            nj = tj + dc[d]

            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and not visited[ni][nj]:
                stack.append((ni, nj))
                visited[ni][nj] = True
    return 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    si, sj = find_s(maze, N)
    print(maze)

    print(f'#{tc} {dfs(maze, N, si, sj)}')
