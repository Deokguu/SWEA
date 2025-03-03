def lettuce_bfs(arr, N, M, row, col):
    queue = []
    queue.append([row, col])
    visited[row][col] = True

    while queue:
        ti, tj = queue.pop(0)
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni = ti + dr
            nj = tj + dc

            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and not visited[ni][nj]:
                queue.append([ni,nj])
                visited[ni][nj] = True

T =int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        col, row = map(int, input().split())
        arr[row][col] = 1

    cnt = 0
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1 and not visited[row][col]:
                lettuce_bfs(arr, N, M, row, col)
                cnt += 1
    print(cnt)
    
'''
M, N, K 순서대로 입력받기
또 입력값 받을 때 제대로 안봐서 시간 낭비... 정신차리자
'''
