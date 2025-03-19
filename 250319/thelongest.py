def dfs(n, cnt):
    global maxV
    visited[n] = 1  # 방문 처리
    maxV = max(maxV, cnt)  # 최댓값 갱신

    for i in graph[n]:  # 인접 노드 탐색
        if not visited[i]:  # 방문하지 않은 노드만 탐색
            dfs(i, cnt + 1)

    visited[n] = 0  # 백트래킹 (방문 해제)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    maxV = 0

    for i in range(1, N + 1):  # 모든 정점에서 DFS 실행
        visited = [0] * (N + 1)  # 방문 배열 초기화
        dfs(i, 1)  # 시작 노드를 포함하여 길이 1부터 시작

    print(f'#{tc} {maxV}')  # 최장 경로 출력
