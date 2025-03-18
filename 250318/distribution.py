'''
level = N개의 행
branch = N개의 열
'''
def dfs(depth, total):
    global max_v
    if total <= max_v: # 가지치기
        return

    if depth == N:
        if max_v < total:
            max_v = total
        return

    for col in range(N):
        if visited[col]:
            continue
        visited[col] = 1 # 방문한 열 표시
        dfs(depth + 1, total * arr[depth][col] / 100)
        visited[col] = 0
    return



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_v = 0
    dfs(0, 1)
    print(f'#{tc} {max_v*100:.6f}')

