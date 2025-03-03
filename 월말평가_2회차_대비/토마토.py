dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def fermented(arr, N, M):
    lst = []
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1:
                lst.append([row, col])
    return lst

def bfs(arr, N, M, start_tomato):
    global visited
    if arr == [[1] * M for _ in range(N)]: #다 익어있는 상태태
        return 0
    
    queue = []
    for si, sj in start_tomato:
        queue.append([si, sj])
        visited[si][sj] = 1
        arr[si][sj] = 1

    while queue:
        ti, tj = queue.pop(0)

        for d in range(4):
            ni = ti + dr[d]
            nj = tj + dc[d]

            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = visited[ti][tj] + 1
                arr[ni][nj] = 1
      
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
    max_v = 0
    for i in range(N):
        for j in range(M):
            if max_v < visited[i][j]:
                max_v = visited[i][j]
    return max_v -1 
    


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
fermented_lst = fermented(tomato, N, M)
# print(fermented_lst)
print(bfs(tomato, N, M, fermented_lst))
