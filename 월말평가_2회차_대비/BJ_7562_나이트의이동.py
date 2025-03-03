def bfs(arr, I, si, sj):
    queue = []
    visited = [[0] * I for _ in range(I)]
    queue.append([si,sj])
    visited[si][sj] = 1

    while queue:
        ti, tj = queue.pop(0)
        if arr[ti][tj] == arr[ei][ej]:
            return visited[ei][ej] - 1
        for dr, dc in [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]:
            ni = ti + dr
            nj = tj + dc

            if 0<=ni<I and 0<=nj<I and visited[ni][nj] == 0:
                queue.append([ni,nj])
                visited[ni][nj] = visited[ti][tj] + 1

T = int(input())

for tc in range(1, T+1):
    I = int(input()) # 체스판 크기
    arr = [[0] * I for _ in range(I)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    arr[si][sj] = 2
    arr[ei][ej] = 3
    print(bfs(arr, I, si, sj))