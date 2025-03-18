'''
level = N개의 행
branch = N개의 열
'''
def dfs(depth, total):
    global min_v
    if total >= min_v: # 가지치기
        return min_v

    if depth == N:
        if min_v > total:
            min_v = total
        return min_v

    for col in range(N):
        if visited[col]:
            continue
        visited[col] = 1 # 방문한 열 표시
        dfs(depth + 1, total + arr[depth][col])
        visited[col] = 0
    return min_v


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_v = 10e10
    print(f'#{tc} {dfs(0, 0)}')



