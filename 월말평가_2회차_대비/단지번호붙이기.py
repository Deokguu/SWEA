dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(arr, N, i, j):
    global visited
    queue = []
    queue.append([i, j])
    visited[i][j] = 1
    cnt = 0

    while queue:
        ti, tj = queue.pop(0)
        cnt += 1
        for d in range(4):
            ni, nj = ti + dr[d], tj + dc[d]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = 1
    return cnt
N = int(input())

Household = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
HH_cnt = 0
HH_lst = []
for row in range(N):
    for col in range(N):
        if Household[row][col] == 1 and visited[row][col] == 0:
            HH_lst.append(bfs(Household, N, row, col))
            HH_cnt += 1
HH_lst.sort()

print(HH_cnt)
for i in HH_lst:
    print(i)
