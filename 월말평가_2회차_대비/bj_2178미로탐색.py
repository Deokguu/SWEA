dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(arr, N, M, si, sj):
    queue = []
    visited = [[0] * M for _ in range(N)]
    queue.append([si, sj])
    visited[si][sj] = 1

    while queue:
        ti, tj = queue.pop(0)
        if ti == ei and tj == ej:
            return visited[ei][ej]
        
        for d in range(4):
            ni , nj = ti + dr[d], tj + dc[d]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append([ni,nj])
                visited[ni][nj] = visited[ti][tj] + 1
    return 0


N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)] #배열
si, sj = 0, 0
ei, ej = N-1, M-1
print(bfs(maze, N, M, si, sj))

